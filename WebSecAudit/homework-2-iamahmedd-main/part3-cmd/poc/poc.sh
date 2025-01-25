#!/bin/bash
pip3 install requests >/dev/null 2>&1
sudo apt-get update -qq >/dev/null 2>&1
sudo apt-get install -y python3-pip >/dev/null 2>&1
pip3 install flask >/dev/null 2>&1
python3 myscript.py
