FROM nvcr.io/nvidia/l4t-jetpack:r36.4.0 AS base_arm64

# Install Python and required packages
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        net-tools \
        iputils-ping \
        vim \
        git \
        tmux \
        tcpdump \
        protobuf-compiler \
        libxml2-dev \
        libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Check if "ubuntu" user exists, delete it if it does, then create the desired user
RUN if getent passwd ubuntu > /dev/null 2>&1; then \
        userdel -r ubuntu && \
        echo "Deleted existing ubuntu user"; \
    fi && \
    groupadd --gid $USER_GID $USERNAME && \
    useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo "Created new user $USERNAME"

# Add sudo support for the non-root user
RUN apt-get update && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && rm -rf /var/lib/apt/lists/*


RUN apt-get update && \
    apt-get install -y \
        jq \
        tmux \
        curl \
    && rm -rf /var/lib/apt/lists/*

# gstreamer install by default from jetpack (base image)
    
# Copy requirements.txt and install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r /tmp/requirements.txt

# Copy custom wheels
COPY wheels/* /tmp/
RUN python3 -m pip install /tmp/*.whl

RUN apt-get update && \
    apt-get install -y \
        python-is-python3 \
        tmuxp \
    && rm -rf /var/lib/apt/lists/*

COPY tmux.conf /etc/tmux.conf

RUN apt-get update && \
    apt-get install -y \
        libx11-6 \
        libx11-xcb1 \
        libxcb1 \
        libxcb-xinerama0 \
        libxcb-icccm4 \
        libxcb-image0 \
        libxcb-keysyms1 \
        libxcb-randr0 \
        libxcb-render0 \
        libxcb-shm0 \
        libxcb-shape0 \
        libxcb-sync1 \
        libxcb-xfixes0 \
        libxcb-xkb1 \
        libxrender1 \
        libxext6 \
        libxfixes3 \
        libxrandr2 \
        libxi6 \
        libgl1-mesa-glx \
        libglib2.0-0 \
        libsm6 \
    && rm -rf /var/lib/apt/lists/*