FROM python:3.12

RUN apt-get update && apt-get install \
	-y postgresql postgresql-contrib && apt-get clean

RUN apt-get update && apt-get install \
	-y default-jdk

WORKDIR /

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
