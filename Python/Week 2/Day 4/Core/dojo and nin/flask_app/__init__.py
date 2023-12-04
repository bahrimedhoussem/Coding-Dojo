from flask import Flask
app = Flask(__name__)
app.secret_key = "hsjhs"
DATABASE = "recipes_db"