#!/bin/bash

export BASE_DIR=$(pwd)
export PY_SCRIPT="get_data.py"

cd ${BASE_DIR}

echo "Run python script."
python3 ${BASE_DIR}/${PY_SCRIPT}

RESP=$?
if [ ${RESP} != 0 ]; then
	echo "Python script failed."
	echo "ERROR: ${RESP}"
	exit 1
fi

echo "Done!"

exit 0