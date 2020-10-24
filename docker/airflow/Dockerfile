FROM apache/airflow:1.10.12-python3.7

USER root

# Configure apt sources
RUN apt-get update                                  && \
    apt-get install -y gnupg2 ca-certificates curl  && \
    curl https://dl-ssl.google.com/linux/linux_signing_key.pub | \
            apt-key add -                           && \
    curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
            apt-key add -                           && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > \
            /etc/apt/sources.list.d/pgdg.list       && \
    echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> \
            /etc/apt/sources.list.d/google.list     && \
    apt-get update                                  && \
    apt-get autoremove -y                           && \
    apt-get clean                                   && \
    apt-get autoclean                               && \
    rm -rf ~/.cache /var/lib/apt/lists/* || true

ARG KUBERNETES_VERSION="1.19.2"

RUN apt-get update                                  && \
    apt-get install -y --no-install-recommends         \
        bash                                           \
        bash-completion                                \
        build-essential                                \
        cmake                                          \
        curl                                           \
        g++                                            \
        gcc                                            \
        git                                            \
        git-lfs                                        \
        libpq-dev                                      \
        make                                           \
        nano                                           \
        postgresql-client-12                           \
        python3-dev                                    \
        sudo                                           \
        wget                                        && \
    apt-get autoremove -y                           && \
    apt-get clean                                   && \
    apt-get autoclean                               && \
    rm -rf ~/.cache /var/lib/apt/lists/* || true    && \
    mkdir -p /etc/bash_completion.d                 && \
    wget https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl \
        -O /usr/local/bin/kubectl                   && \
    chmod +x /usr/local/bin/kubectl                 && \
    kubectl completion bash                            \
        >> /etc/bash_completion.d/kubectl.bash      && \
    sed 's@#force_color_prompt=yes@force_color_prompt=yes@g' \
        -i /home/airflow/.bashrc                    && \
    pip3 --no-cache-dir install setuptools          && \
    pip3 --no-cache-dir install jq yq               && \
    echo >> /etc/sudoers                            && \
    echo "airflow ALL=(ALL:ALL) NOPASSWD: ALL"         \
        >> /etc/sudoers

COPY ./requirements.txt /requirements.txt

USER airflow

RUN pip3 install --no-cache --no-cache-dir --user      \
        -r /requirements.txt
