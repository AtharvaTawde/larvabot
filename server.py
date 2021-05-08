from flask import Flask
from threading import Thread
import random
import facts as f

app = Flask('')

@app.route('/')
def home():
    return "<small>Larva Bot is active.</small>"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()