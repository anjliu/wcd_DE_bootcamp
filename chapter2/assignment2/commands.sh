#!/bin/bash

# stop and remove active containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# build and run container
docker build -t assignment2:2.0 .
docker run -d --rm -v /home/ajl/wcd/chapter2/assignment2/input:/dk/input -v /home/ajl/wcd/chapter2/assignment2/output:/dk/output --name assignment2_docker assignment2:2.0

# execute data processing script
docker exec -it assignment2_docker python3 py_script.py