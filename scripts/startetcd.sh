#!/bin/bash

BASEDIR=$(dirname "$0")

NAME=etcd-master
ORG=jrepp
VERSION=latest


# Make sure the named containers are cleaned up
docker stop ${NAME}
docker rm ${NAME}

if [ -x docker-machine ]; then 
     IPADDR=$(docker-machine ip)
else
     IPADDR=$(${BASEDIR}/internalip.sh)
fi

# Start the local etcd listener container, ETCD_* variables are
# used in place of command line arguments
docker run -d \
    -p "2379:2379" \
    -p "2380:2380" \
    -e "ETCD_ADVERTISE_CLIENT_URLS=http://${IPADDR}:2379" \
    -h "etcd" \
    --name ${NAME} \
    ${ORG}/etcd:${VERSION}


