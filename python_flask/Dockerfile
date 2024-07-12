FROM python:3.9.5-slim

RUN pip install flask

WORKDIR /src
ENV FLASK=app.py

COPY app.py /src/app.py

EXPOSE 5000

CMD ["flask","run","-h","0.0.0.0"]