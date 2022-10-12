#! /bin/bash

VOL_NAME=dataexchangews_db_data
if docker volume ls | grep -q $VOL_NAME; then
  read -p "A stale volume is found. Stop containers and press Y to continue" -n 1 -r
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    docker volume rm $VOL_NAME
    echo Volume $VOL_NAME has been deleted.
  else
    exit 0
  fi
else
  echo No orphaned volume is found.
fi

PSW_WEB=$(openssl rand -base64 29 | tr -d "=+/@\\\:" | cut -c1-20)
PSW_DBU=$(openssl rand -base64 29 | tr -d "=+/@\\\:" | cut -c1-20)
PSW_DBR=$(openssl rand -base64 29 | tr -d "=+/@\\\:" | cut -c1-20)
sed -e 's/wspassword/'"$PSW_WEB"'/g; s/wsdbpassword/'"$PSW_DBU"'/g' backend/.main.yaml.tpl > backend/dataexchange-ws/main.yaml
echo $PSW_DBU > .db_password.txt 
echo $PSW_DBR > .db_root_password.txt 
echo Credentials have been reset
echo "Now you can run: docker compose up"
