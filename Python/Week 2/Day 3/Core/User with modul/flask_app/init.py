from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from flask_app.models.users_model import User





if __name__ == "__main__":
    app.run(debug=True, port=5001)
