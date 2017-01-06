#!/bin/bash

BASEDIR=$(dirname "$0")
echo "Base directory ${BASEDIR}"

if [ -x docker-machine ]; then 
    export ETCD_ADDR=$(docker-machine ip)
else
    export ETCD_ADDR=$(${BASEDIR}/../scripts/internalip.sh)
fi

export ETCD_PORT=2379

