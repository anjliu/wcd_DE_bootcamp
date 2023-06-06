#!/bin/bash


# directories used

export BASE_DIR="/home/ajl/wcd/chapter1/project1"
export DOWNLOAD_DIR="${BASE_DIR}/data"
export OUTPUT_DIR="${BASE_DIR}/output"
export SHELL_SCRIPT='download'
# export LOG_FILE = ${SHELL_SCRIPT}.log

# make directory and download data
mkdir -p ${DOWNLOAD_DIR}
cd ${DOWNLOAD_DIR}
echo "Downloaded data will be stored in ${DOWNLOAD_DIR}."

echo "Download data..." 
for year in {2020..2022}; 
do wget -N --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=48549&Year=${year}&Month=2&Day=14&timeframe=1&submit=Download+Data";
done;

echo "Response: "
echo $?

echo "Run concatenation python script..."
cd ${BASE_DIR}
mkdir -p ${OUTPUT_DIR}
python3 concatenate.py

echo "Response: "
echo $?