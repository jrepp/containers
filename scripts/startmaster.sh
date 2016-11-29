docker-machine create \
    -d virtualbox \
    --swarm --swarm-master \
    --swarm-discovery="etc://$(docker-machine ip default):2380" \
    --engine-opt="cluster-store=etcd://$(docker-machine ip mh-keystore):8500" \
    --engine-opt="cluster-advertise=eth1:2376" \
    mhs-demo0
