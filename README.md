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
