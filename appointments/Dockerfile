
FROM python:3.8-slim



WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY app.py .

EXPOSE 6060


CMD ["python", "app.py"]
