#!/bin/bash
HOST="/data/Docker/CiscoBanfi"  # write here the path of mounted volume
export APPLOGS="${HOST}/logs"
export RESOURCE_PATH="${HOST}/resources"
export APP_SOR_FILES="${HOST}/SOR"
export APP_JPG_FILES="${HOST}/JPG"
export SUPERVISOR_LOGS="${APPLOGS}/supervisord"

# must be identical to the one in CosmWeb-config.yaml
export DATABASE_PATH="/app/database"  

mkdir -p ${HOST}

mkdir -p ${APPLOGS}
mkdir -p ${RESOURCE_PATH}
mkdir -p ${APP_SOR_FILES} 
mkdir -p ${APP_JPG_FILES} 
mkdir -p ${SUPERVISOR_LOGS}

echo "docker run -d \
             --restart always \
             -v $HOST:/app/host \
             --name BanfiBot cisco-banfi"             
             
docker run -d \
             --restart always \
             -v $HOST:/app/host \
             --name BanfiBot cisco-banfi
