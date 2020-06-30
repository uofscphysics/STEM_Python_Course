#!/usr/bin/env bash

export PATH=${PATH}:${HOME}/.local/bin

pip install --upgrade pip
pip install -r requirements.txt

mkdir -p /home/runner/.jupyter

cp jupyter_notebook_config.py /home/runner/.jupyter/jupyter_notebook_config.py

jupyter notebook
