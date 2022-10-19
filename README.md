# DataExchange-DatasetJson
This project is used to manage the JSON representation for Clinical Datasets (a complement to the Dataset-XML representation) @2022

## APIs using Dataset-JSON

Create FAST-API and MySQL docker containers to provide data requests

Parameters are: filename (like adam/adae), fileformat (json...)

Current files are examples that provided by [cdisc-org DataExchange-DatasetJson](https://github.com/cdisc-org/DataExchange-DatasetJson/branches)

## Steps

**pyenvcreate.sh** will create virtul env for python codes for:
1. FASTAPI
2. Python code to read example files and write into connecrted mysql docker container.

**reset.sh** will generate password for mysql container and FAST-API authorization information. 

**localtest** folder create one mysql container in local machine.

other docker-compose file and dockerfile will deploy into real env. 



#### Testing

Local testing:
<img width="787" alt="image" src="https://user-images.githubusercontent.com/16886624/196528498-7c3b0a41-9a3d-42ba-b5a2-f87ab181228a.png">

GET one dataset (here is adae.json):

<img width="752" alt="Screen Shot 2022-10-18 at 8 12 58 PM" src="https://user-images.githubusercontent.com/16886624/196568095-bdf84f06-d85d-47fb-b068-e085b78a530b.png">

GET one dataset by using file name and file format

<img width="739" alt="Screen Shot 2022-10-18 at 8 50 11 PM" src="https://user-images.githubusercontent.com/16886624/196571897-f92f78bf-5bc7-43b2-acf9-dfe7a6b84963.png">


If API need authorization:

<img width="612" alt="Screen Shot 2022-10-18 at 8 15 19 PM" src="https://user-images.githubusercontent.com/16886624/196568339-e990c479-dd22-4657-b7de-3dfbb6807d89.png">


### Arch

<img width="550" alt="Screen Shot 2022-10-18 at 7 16 25 PM" src="https://user-images.githubusercontent.com/16886624/196576330-2cff503f-0ca2-49ec-996b-2e8a653029c0.png">

