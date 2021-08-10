FROM python:3.8

RUN pip install kubernetes fastapi uvicorn[standard]

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
