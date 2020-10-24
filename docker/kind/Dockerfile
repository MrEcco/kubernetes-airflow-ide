FROM docker:19.03-dind as builder

ARG KIND_VERSION="0.9.0"

WORKDIR /output
COPY ./manifests ./manifests
COPY ./scripts ./usr/local/bin

RUN chmod +x ./usr/local/bin/*

RUN apk add --no-cache                                 \
        go                                             \
        git                                            \
        git-lfs                                     && \
    GO111MODULE="on" go get sigs.k8s.io/kind@v${KIND_VERSION} && \
    mkdir -p ./usr/local/bin                        && \
    cp /root/go/bin/kind ./usr/local/bin/kind

FROM docker:19.03-dind

USER root

ARG KUBERNETES_VERSION="1.19.2"

RUN apk add --no-cache                                 \
        bash                                           \
        bash-completion                                \
        bind-tools                                     \
        curl                                           \
        jq                                             \
        nano                                           \
        py3-pip                                        \
        python3                                        \
        supervisor                                  && \
    curl https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl \
        -Lo /usr/local/bin/kubectl                  && \
    chmod +x /usr/local/bin/kubectl                 && \
    pip install yq --no-cache --no-cache-dir

COPY --from=builder /output /
