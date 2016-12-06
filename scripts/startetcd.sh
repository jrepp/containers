#!/bin/bash

# Make sure the named containers are cleaned up
docker stop etcd-master etcd-client
docker rm etcd-master etcd-client

# Start the local etcd listener container
docker run -d \
    -p "2379:2379" \
    -p "2380:2380" \
    -e "ETCD_ADVERTISE_CLIENT_URLS=http://$(docker-machine ip):2379" \
    -h "etcd" \
    --name etcd-master \
    jrepp/etcd:latest

# Start the local etcd client container
docker run -it \
    --rm \
    -h "etcd-client" \
    -v "/home/jrepp/containers/etcdclient:/code" \
    --link etcd-master \
    --name etcd-client \
    jrepp/etcdclient:latest

