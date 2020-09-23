FROM ubuntu:latest

WORKDIR /tmp

ENV GOVERSION 1.15.2
ENV RTSVERSION 0.9.15
ENV GOPATH /root/.go

RUN apt-get -yqq update \
    && apt-get clean \
    && apt-get install -yqq build-essential wget

RUN cd /tmp && wget https://golang.org/dl/go${GOVERSION}.linux-amd64.tar.gz &&\
    tar -C /usr/local -xzf go${GOVERSION}.linux-amd64.tar.gz && rm go${GOVERSION}.linux-amd64.tar.gz && \
    echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc && bash -- &&\
    mkdir $GOPATH


RUN cd /tmp && wget https://github.com/aler9/rtsp-simple-server/archive/v${RTSVERSION}.tar.gz &&\
    tar -C . -xzf v${RTSVERSION}.tar.gz 
    
WORKDIR /tmp/rtsp-simple-server-${RTSVERSION}

ENV PATH=/usr/local/go/bin:$PATH

CMD [ "go", "run", "." ]