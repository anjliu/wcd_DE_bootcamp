FROM python:3.11

# set working dir - this will be in the docker image
ENV BASE_DIR='/dk'
WORKDIR $BASE_DIR

# build environment
RUN pip install pandas==2.0.2

# files and volumes
ADD py_script.py $BASE_DIR

ENV INPUT_DIR=$BASE_DIR\/input
ENV OUTPUT_DIR=$BASE_DIR\/output

VOLUME $INPUT_DIR
VOLUME $OUTPUT_DIR

# keep container running
CMD tail -f /dev/null
