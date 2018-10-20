#!/usr/bin/env bash
set -e

if [ -z "$1" ]
  then
    echo "Falta o nome da funcão lambda"
    exit
fi

zip -r upload.zip build/*

aws lambda update-function-code --function-name $1 --zip-file fileb://upload.zip
