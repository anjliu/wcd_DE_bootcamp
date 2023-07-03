#!/bin/bash

# installations
sudo apt-get update
sudo apt install python3.11 -y
sudo apt install python3.11-distutils -y 
sudo apt install awscli -y

# virtual environment for python
sudo apt install python3-virtualenv -y
virtualenv --python="/usr/bin/python3.11" assignment32  
source assignment32/bin/activate 

# python libraries
pip install -r py_libs.txt

deactivate # deactivate the virtual environment

chmod a+x run.sh # make run.sh executable