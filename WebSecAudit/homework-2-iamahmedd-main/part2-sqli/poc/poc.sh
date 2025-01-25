#!/bin/bash
#added ">dev/null 2>&1" to not show the dependencies downloading and only show the flag output value
sudo apt-get update -qq > /dev/null 2>&1
sudo apt-get install -y python3-pip > /dev/null 2>&1
pip3 install requests beautifulsoup4 > /dev/null 2>&1
python3 myscript.py
