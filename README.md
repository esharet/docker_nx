# README

Build docker image

- Install dronekit python package that fix for use on python 3.10

## Backup
Using deploy reloaded to backup the project

---

# Gazebo

Build gazebo-11 docker base

```bash title="build"
docker build -f .devcontainer/Dockerfile.gazebo .
```

```bash title="run"
docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --user user \
    gazebo:11 \
    /bin/bash
```

---
# Releses
## V2
- Add tmuxp

# Build
```bash
# build
docker build -f .devcontainer/Dockerfile -t rome_nx-dev:aarch64 .
# save
docker image save -o rome_nx-dev-aarch64.tar rome_nx-dev:aarch64
```