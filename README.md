# README

This repo builds the dockers as part of shifting firefox to run on orin-nx.

Build docker image

- Install dronekit python package that fix for use on python 3.10

## Backup
Using deploy reloaded to backup the project


# Build
```bash
# build
docker build -f .devcontainer/arm/Dockerfile -t firefox_nx:aarch64 .
docker build -f .devcontainer/amd/Dockerfile -t firefox_nx:x86_64 .
# save
docker image save -o firefox_nx_aarch64.tar firefox_nx:aarch64
docker image save -o firefox_nx_x86_64.tar firefox_nx:x86_64
```