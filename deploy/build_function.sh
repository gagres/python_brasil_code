#!/usr/bin/env bash
set -e

pythonV="python3.6"

if [ -e ./requirements.txt ]
then
  python3 -m venv env
  source ./env/bin/activate
  echo "pythonV ${pythonV}"
  pip install -U pip
  mkdir "build"
  mkdir "build/site-packages"
  echo "Installing requirements to env..."
  pip install -U spacy
  python -m spacy download pt
  echo "copy env to site-packages folder (AWS python package needed)"
  pip install -r ./requirements.txt -U --no-cache -t build/site-packages
  # Check if destination folder of the model exists
  test -d build/site-packages/pt_core_news_sm/ || mkdir build/site-packages/pt_core_news_sm/
  cp -R ./env/lib/${pythonV}/site-packages/pt_core_news_sm/* build/site-packages/pt_core_news_sm/
  cp ./*.py build/
  # Remove some packages of spaCy that we don't use
  # spacyDir="${path}/target/site-packages/spacy/lang"
  # echo "Removing some spacy packages (see list on build_functions script)"
  # rm -rf "${spacyDir}/tr" "${spacyDir}/de" "${spacyDir}/es" "${spacyDir}/fa" "${spacyDir}/fi" "${spacyDir}/fr"
  # rm -rf "${spacyDir}/hu" "${spacyDir}/id" "${spacyDir}/it" "${spacyDir}/ja" "${spacyDir}/sv"
  # Logs of files created
  ls -lia build
  ls -lia build/site-packages
  deactivate
fi
