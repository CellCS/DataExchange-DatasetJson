from . import string as constants
import yaml

class APIConfigure:
    db_url = ''
    api_port = ''
    api_host_ip = ''
    api_creds_name = ''
    api_creds_pwd = ''

    def __init__(self):
        self.setApiConfig()
    
    def setApiConfig(self):
        with open(constants.CONFIGURE_FILE, 'r') as yamlfile:
            try:
                proConfig=yaml.load(yamlfile, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)
        yamlfile.close()
        self.db_url = proConfig['mysql']['dialect']+"+"+proConfig['mysql']['dbapi']+"://"+proConfig['mysql']['user']+":"+proConfig['mysql']['pass']+"@"+proConfig['mysql']['host']+":"+str(proConfig['mysql']['port'])+"/"+proConfig['mysql']['database']
        self.api_port = proConfig['api']['port']
        self.api_host_ip = str(proConfig['api']['host'])
        self.api_creds_name = list(proConfig['api']['creds'].keys())[0]
        self.api_creds_pwd = str(proConfig['api']['creds'][self.api_creds_name])
