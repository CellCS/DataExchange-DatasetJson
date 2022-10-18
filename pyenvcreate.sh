#! /bin/bash

python3 -m venv ./localtest/mysql/pylib/.venv
source ./localtest/mysql/pylib/.venv/bin/activate
pip3 install -r ./localtest/mysql/pylib/requirements.txt
deactivate

python3 -m venv ./backend/dataexchange-ws/.venv
source ./backend/dataexchange-ws/.venv/bin/activate
pip3 install -r ./backend/dataexchange-ws/requirements.txt
deactivate