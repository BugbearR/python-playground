FROM mcr.microsoft.com/devcontainers/python:latest
# See https://mcr.microsoft.com/en-us/product/devcontainers/python/about
# https://hub.docker.com/_/microsoft-devcontainers-python

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
  && pip install --upgrade pip \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/cache/apt/* /var/lib/apt/lists/

# USER $USERNAME
# WORKDIR /home/$USERNAME
# RUN python -m venv .venv
# RUN echo "source /home/$USERNAME/.venv/bin/activate" >> /home/$USERNAME/.bashrc

CMD [ "/bin/bash" ]
