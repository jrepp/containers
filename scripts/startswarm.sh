#
# Add the swarm container to the host, requires startetcd.sh
#
docker run \
    -d swarm:latest \
    join \
    --addr="$(docker-machine ip default):2375" \
    "etcd://$(docker-machine ip default):2379/swarm"
