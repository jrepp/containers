### About

This is a scratchpad area for learning about docker concepts. 

### Getting Started

#### Install software

* Install [docker toolkit](https://www.docker.com/products/docker-toolbox) or docker engine (apt-get install docker.io)
* Make sure you have a default docker machine (if using toolkit)
* Make the default machine active '. scripts/defaultenv.sh'

#### Build images

* Build the base image 'docker build -t jrepp/etcd:latest base'
* Build the etcd test image 'docker build -t jrepp/etcd:latest etcd'

### Notes

#### etcd

* [Static clustering guide](https://github.com/coreos/etcd/blob/master/Documentation/op-guide/clustering.md#static)
* [Client python API guide](https://github.com/jplana/python-etcd)

#### docker

Some common and useful commands:
docker ps
docker images
docker run
docker-machine ip
