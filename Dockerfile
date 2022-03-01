FROM python:3
COPY . /device_register
WORKDIR /device_register
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]