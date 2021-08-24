FROM python:3.8

RUN pip install fastapi uvicorn[standard]

EXPOSE 80

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
