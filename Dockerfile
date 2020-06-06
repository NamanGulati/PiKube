FROM arm32v7/python:3

WORKDIR /usr/src/app

COPY blink.py ./

RUN pip install gpiozero flask

RUN chmod +x ./blink.py

CMD ["python","./blink.py"]
