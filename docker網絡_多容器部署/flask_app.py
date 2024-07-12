from flask import Flask, render_template
from redis import Redis
import os
import socket


app=Flask(__name__)
redis=Redis(host=os.environ.get('REDIS_HOST','127.0.0.1'),port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    hits=redis.get('hits').decode('utf-8')
    hostname=socket.gethostname()
    return render_template('index.html',hits=hits,hostname=hostname)