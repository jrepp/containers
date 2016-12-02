FROM jrepp/base
MAINTAINER Jacob Repp <jacobrepp@gmail.com>

RUN apt-get install -y \
    binutils-gold \
    ccache \
    clang \
    cmake \
    distcc \
    git \
    ninja-build \
    make \
    vim \
    wget

WORKDIR /root
ADD ../rcfiles/gitconfig .gitconfig
ADD ../rcfiles/vimrc .vimrc

ENTRYPOINT ["/bin/bash"]
