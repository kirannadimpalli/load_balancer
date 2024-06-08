FROM python:3
RUN pip install flask python-dotenv requests
COPY ./service/app.py /service/app.py
CMD ["python", "/service/app.py"]