from flask import Flask
from app.models import init_db

app = Flask(__name__)

init_db(app)

from app import views  # sempre no final