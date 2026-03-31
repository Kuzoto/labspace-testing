# Overview

This workshop provides an overview of several useful tools and activities for software testing. The goal of this workshop is for you gain practical experience with traditional and emerging tools and processes for software testing and maintenance, that will hopefully be relevant to software development in practice. This workshop is based on [Docker Labspaces](https://hub.docker.com/extensions/dockersamples/labspace-extension). Please read the instructions for each task carefully for details on what to complete and how to submit your work.

## Launch the Labspace

To launch the Labspace, ensure Docker Desktop is running and run the following command:

```bash
docker compose -f oci://chbrown13/labspace-testing up -d
```
or (specifically for Windows)

```bash
docker compose --project-directory . -f oci://chbrown13/labspace-testing up -d
```

And then open your browser to http://localhost:3030.

