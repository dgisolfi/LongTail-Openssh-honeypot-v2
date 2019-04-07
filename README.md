# OpenSSH-Honeypot


### Authors

**Eric Wedaa** - *Original Longtail Creation* - [wedaa](https://github.com/wedaa)

**Daniel Gisolfi** - *Docker implementation and TCP Stream Addition* - [dgisolfi](https://github.com/dgisolfi)

## Overview

This honeypot is a custom implementation of 2 OpenSSH servers which have been modified to always reject username and password attempts but logs the attempts. Building on what Eric Wedaa created I have added a TCP Stream to capture attacks in realtime from the honeypot and forward them to a python server for parsing, analyzing, etc. Additionally, I have created a Docker image for the honeypot to allow for quick deployment on a server.

## Deployment

To deploy the honeypot using docker the included make file can be used. Run `make` in the root of the repository to clean, build and run the honeypot from source. To use the prebuilt docker image the honeypot can be pulled from Docker Hub, to do so use one of the following methods.

### Docker

```bash
docker run -it --rm --name ssh_honeypot -p22:22 -p2222:2222 dgisolfi/ssh_honeypot:latest
```

### Docker Compose

Move the `docker-compose.yaml` file found in the root of the directory to the host machine and run:

```
docker-compose up
```

