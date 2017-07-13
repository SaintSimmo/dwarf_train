from flask import Flask, request, render_template, flash, g, session, redirect, url_for, jsonify, make_response, abort
from flask_socketio import SocketIO, send, emit
import json, logging, time, os

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')

app = Flask(__name__)

socketio = SocketIO(app, message_queue=os.getenv('REDIS_URL'))

@app.route('/')
def root():
    return render_template('test.html')

@app.route('/home')
def home():
    return render_template('main.html')
