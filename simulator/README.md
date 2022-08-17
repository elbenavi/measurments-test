
Description:
Servicio que se utiliza para enviar datos de un gps

It has a schema that has:
- longitude
- latitude
- altitude

It send data to Redis

generate venv
python -m venv venv

activate venv for windows os
venv/Scripts/activate

install dependencies:
python -m pip install -r requirements.txt

to execute run:
python main.py

to generate image
docker build -t name-image .
