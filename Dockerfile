FROM python:3
RUN pip install flask
COPY ./app.py /service/app.py
CMD ["python", "/app/app.py"]