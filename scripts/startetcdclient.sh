# Start the local etcd client container
docker run -it \
    --rm \
    -e "ETCDCTL_API=3" \
    -e "ETCDCTL_ENDPOINTS=etcd-master:2379" \
    -h "etcd-client" \
    -v "/home/jrepp/containers/etcdclient:/code" \
    --link etcd-master \
    --name etcd-client \
    jrepp/etcdclient:latest

