from queue import Empty
import secrets
import base64
from typing import Optional
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPAuthorizationCredentials
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.middleware.cors import CORSMiddleware

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, Response, JSONResponse
from starlette.requests import Request
from sqlalchemy.orm import Session

import uvicorn

from nexusws_lib import schemas, models
from nexusws_lib.database import engine,SessionLocal
from nexusws_lib import lib_function as lib_fun
from nexusws_lib import models as model
from nexusws_lib import apiconfig as apiconf


app = FastAPI()
apisets = apiconf.APIConfigure() 

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#create all database
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

security = HTTPBasic()

def authenticate_user(username: str, password: str):
    if username == '' or password =='':
        return False
    return username == apisets.api_creds_name and password == apisets.api_creds_pwd

class BasicAuth(SecurityBase):
    def __init__(self, scheme_name: str = None, auto_error: bool = True):
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "basic":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
                )
            else:
                return None
        return param

basic_auth = BasicAuth(auto_error=False)

def authenticate_test(auth: BasicAuth = Depends(basic_auth)):
    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
            )
    try:
        decoded = base64.b64decode(auth).decode("ascii")
        username, _, password = decoded.partition(":")
        isLogin = authenticate_user(username, password)
        if isLogin is False:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
                )
        return True
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
            )

@app.get("/broadcast")
async def root():
    return {"message": "Welcome to DataExchange-DatasetJson Hackathon 2022"}

# @app.get("/")
# async def login_basic(isAuth: str = Depends(authenticate_test)):
#     print(isAuth)
#     return {"status": 200,'data':'DataExchange DatasetJson web service'}
    

@app.get('/about')
async def about(isAuth: str = Depends(authenticate_test)):
    return {'data':'DataExchange DatasetJson'}

@app.get('/tests/{fullname}')
async def getExampleFile(fullname:str = '', db: Session=Depends(get_db)):
    responsecontent = db.query(model.ExampleFilesTable).filter(model.ExampleFilesTable.FileFullName == fullname).all()
    db.close()
    results_jsn = lib_fun.modelToJson(responsecontent)
    return results_jsn


@app.get('/testfile/')
async def getExampleFile(filename: str = '', format: str = '', db: Session=Depends(get_db)):
    if filename=="" or format=="":
        results = {"error": "File name and format are required."}
        return results
    fullname = filename + "."+format
    responsecontent = db.query(model.ExampleFilesTable).filter(model.ExampleFilesTable.FileFullName == fullname).all()
    db.close()
    results_jsn = lib_fun.modelToJson(responsecontent)
    return results_jsn

@app.get('/examplefile/{fullname}')
async def getExampleFile(isAuth: str = Depends(authenticate_test), fullname:str = '', db: Session=Depends(get_db)):
    responsecontent = db.query(model.ExampleFilesTable).filter(model.ExampleFilesTable.FileFullName == fullname).all()
    db.close()
    results_jsn = lib_fun.modelToJson(responsecontent)
    return results_jsn

@app.get('/example/')
async def getExampleFile(isAuth: str = Depends(authenticate_test), q: List[str] = Query(default=["", ""]), db: Session=Depends(get_db)):
    if q[0] is Empty or q[1] is Empty:
        results = {"error": "File name and format are required."}
        return results
    fullname = q[0] + q[1]
    responsecontent = db.query(model.ExampleFilesTable).filter(model.ExampleFilesTable.FileFullName == fullname).all()
    db.close()
    results_jsn = lib_fun.modelToJson(responsecontent)
    return results_jsn


if __name__ == "__main__":
    apisets = apiconf.APIConfigure()
    uvicorn.run("main:app", host = apisets.api_host_ip, port = apisets.api_port, reload=True)
