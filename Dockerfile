From python:3.9-slim

WORKDIR /app

Copy requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

