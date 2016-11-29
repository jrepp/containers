### About

This is a scratchpad area for learning about docker concepts. 

### Getting Started

* Install docker toolkit
* Make sure you have a default machine
* Make the default machine active '. scripts/defaultenv.sh'
* Build etcd image 'docker build etcd -t jrepp/etcd:latest'

### Notes

#### etcd

[static clustering guide](https://github.com/coreos/etcd/blob/master/Documentation/op-guide/clustering.md#static)
[client python API guide](https://github.com/jplana/python-etcd)

#### docker

Some common and useful commands:
docker ps
docker images
docker run
docker-machine ip
