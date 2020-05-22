#!/usr/bin/env bash

pip install -r requirements.txt

jupyter notebook --ip=0.0.0.0 --port=3000 &

pass=$(jupyter notebook list | grep token | cut -d'=' -f2 | cut -d' ' -f1)


jupyter notebook list
echo ""
echo ""
echo $pass
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
