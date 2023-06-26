#!/bin/bash

# set up environment
sudo apt install python3.10 -y
sudo apt install python3-pip
sudo apt install awscli -y

pip install -r python_lib.txt

# give permission to run script
chmod a+x run.sh

echo "Start the run."

RC1=$?
if [ $RC1 != 0 ]; then
    echo "Run failed."
    echo "Error: ${RC1}"
    exit 1 
fi

echo "Run completed."
exit 0