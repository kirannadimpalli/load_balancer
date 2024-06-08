FROM python:3
RUN pip install flask python-dotenv
COPY ./service/app.py /service/app.py
CMD ["python", "/service/app.py"]