FROM python:3.10

WORKDIR /authenticator

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python","-m","flask","run","--host=0.0.0.0"]