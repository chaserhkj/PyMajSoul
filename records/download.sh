#!/bin/bash
[[ -z $BASEURL ]] && BASEURL="https://mj-srv-3.majsoul.com:7343/majsoul/game_record/"

for ID in `ls summary/`
do
    if [[ ! -e "content/$ID" ]]
    then
        wget -O "content/$ID" "$BASEURL/$ID"
        if [[ $? != 0 ]]
        then
            rm -f "content/$ID"
            echo $ID >> failed_fetch
        fi
    fi
done
