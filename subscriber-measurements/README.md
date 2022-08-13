
Description:
Service that is listening a events in redis and send data to api manager of measurements

It listes events in Redis and send post request to api of measurements manager

generate venv
python -m venv venv

activate venv for windows os
venv/Scripts/activate

install dependencies:
python -m pip install -r requirements.txt

to execute run:
python main.py