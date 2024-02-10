FROM mcr.microsoft.com/devcontainers/python:latest
# See https://mcr.microsoft.com/en-us/product/devcontainers/python/about
# https://hub.docker.com/_/microsoft-devcontainers-python

RUN apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
  && pip install --upgrade pip \
  && pip install jupyterlab \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/cache/apt/* /var/lib/apt/lists/

CMD [ "/bin/bash" ]
