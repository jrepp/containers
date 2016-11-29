#!/bin/bash

# Make sure the named container is clenaed up
docker stop etcd-master
docker rm etcd-master

# Start the etcd container
docker run -d \
    -p "2379:2379" \
    -p "2380:2380" \
    -e "ETCD_ADVERTISE_CLIENT_URLS=http://$(docker-machine ip):2379" \
    -h "etcd" \
    --name etcd-master \
    jrepp/etcd:latest
