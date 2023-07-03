#!/bin/bash

# directories
export PYTHON_SCRIPT_NAME=$(cat specs.toml | grep 'etl' | awk -F"=" '{print $2}' | tr -d '"') # get the etl script from specs.toml, and remove the quotes
export SCRIPTS_FOLDER=$(pwd)

# run
cd ${SCRIPTS_FOLDER}
source assignment32/bin/activate

echo "Start to run Python Script"
python3 ${SCRIPTS_FOLDER}/${PYTHON_SCRIPT_NAME}


ret=$?
if [ ${ret} != 0 ]; then
	echo "PYTHON RUNNING FAILED"
	echo "[ERROR:] RETURN CODE:  ${ret}"
	exit 1
fi

echo "Finished running program!"

deactivate

exit 0 
