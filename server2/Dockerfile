FROM python:3.11.4

WORKDIR /server2

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8001


CMD ["python", "server2.py"]