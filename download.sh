#!/bin/bash

for ID in `ls records/`
do
    DATA=`jq -r .data records/$ID`
    if [[ -z $DATA ]]
    then
        DATA_URL=`jq -r .data_url records/$ID`
        CONTENT=`wget -O - $DATA_URL|base64 -w 0`
        jq -r .data=\"$CONTENT\" records/$ID | sponge records/$ID
    else
        echo "$ID data present"
    fi
done
