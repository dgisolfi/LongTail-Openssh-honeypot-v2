# OpenSSH-Honeypot


### Authors

**Eric Wedaa** - *Original Longtail Creation* - [wedaa](https://github.com/wedaa)

**Daniel Gisolfi** - *Docker implementation and TCP Stream Addition* - [dgisolfi](https://github.com/dgisolfi)

## Overview

This honeypot is a custom implementation of 2 OpenSSH servers which have been modified to always reject username and password attempts but logs the attempts. Building on what Eric Wedaa created I have added a TCP Stream to capture attacks in realtime from the honeypot and forward them to a python server for parsing, analyzing, etc. Additionally, I have created a Docker image for the honeypot to allow for quick deployment on a server.