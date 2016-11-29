FROM jrepp/base
MAINTAINER Jacob Repp <jacobrepp@gmail.com>

# Install base system dependencies
RUN apt-get install -y \
    net-tools \
    python-minimal \
    software-properties-common

#
# Download etcd, verify signatures
#
WORKDIR /

LABEL "etcdclient" "v1.0"

# Download latest binary components for etcd
ADD https://coreos.com/security/image-signing-key/CoreOS_Image_Signing_Key.asc .
ADD https://coreos.com/dist/pubkeys/app-signing-pubkey.gpg .
ADD https://github.com/coreos/etcd/releases/download/v3.1.0-rc.1/etcd-v3.1.0-rc.1-linux-amd64.tar.gz .
ADD https://github.com/coreos/etcd/releases/download/v3.1.0-rc.1/etcd-v3.1.0-rc.1-linux-amd64.tar.gz.asc .

RUN gpg --import CoreOS_Image_Signing_Key.asc
RUN gpg --import app-signing-pubkey.gpg
RUN gpg --verify etcd-v3.1.0-rc.1-linux-amd64.tar.gz.asc 

# Extract the etc components into the root directory
RUN tar --strip-components=1 --preserve-permissions -zxvf etcd-v3.1.0-rc.1-linux-amd64.tar.gz

# Install setuptools
ADD https://bootstrap.pypa.io/ez_setup.py .
RUN python ez_setup.py

# Download latest python-etcd
ADD https://github.com/jplana/python-etcd/archive/0.4.2.tar.gz python-etcd-0.4.2.tar.gz
RUN tar --preserve-permissions -zxvf python-etcd-0.4.2.tar.gz
RUN cd python-etcd-0.4.2 && python setup.py install

# Cleanup the download artifacts
# TODO: download everything to temp location
# TODO: consder some time of software_cache volume to avoid larger repeat downloads
RUN rm -f *.tar.gz *.gpg *.asc *.zip ez_setup.py

# Cleanup the image
#RUN apt-get remove --purge -y $BUILD_PACKAGES $(apt-mark showauto) && \
#    rm -rf /var/lib/apt/lists/*


ENTRYPOINT ["/bin/bash"]
