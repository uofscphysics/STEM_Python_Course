#!/usr/bin/env bash

pip install -r requirements.txt

jupyter notebook --ip=0.0.0.0 --port=3000
