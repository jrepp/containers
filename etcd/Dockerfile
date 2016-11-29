FROM jrepp/base
MAINTAINER Jacob Repp <jacobrepp@gmail.com>

#
# Download etcd, verify signatures
#
WORKDIR /

LABEL "etcd-release" "v3.1.0-rc.1"

ADD https://coreos.com/security/image-signing-key/CoreOS_Image_Signing_Key.asc .
ADD https://coreos.com/dist/pubkeys/app-signing-pubkey.gpg .
ADD https://github.com/coreos/etcd/releases/download/v3.1.0-rc.1/etcd-v3.1.0-rc.1-linux-amd64.tar.gz .
ADD https://github.com/coreos/etcd/releases/download/v3.1.0-rc.1/etcd-v3.1.0-rc.1-linux-amd64.tar.gz.asc .

RUN gpg --import CoreOS_Image_Signing_Key.asc
RUN gpg --import app-signing-pubkey.gpg
RUN gpg --verify etcd-v3.1.0-rc.1-linux-amd64.tar.gz.asc 

# Extract the etc components into the root directory
RUN tar --strip-components=1 --preserve-permissions -zxvf etcd-v3.1.0-rc.1-linux-amd64.tar.gz

# Cleanup the download artifacts
RUN rm -f *.tar.gz *.gpg *.asc

# Cleanup the image
RUN apt-get remove --purge -y $BUILD_PACKAGES $(apt-mark showauto) && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get autoremove

# Expose the etcd service ports
EXPOSE 2379 2380

ENTRYPOINT ["/etcd", "--listen-client-urls=http://0.0.0.0:2379"]
