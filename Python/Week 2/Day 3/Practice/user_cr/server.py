from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from users import User





@app.route('/')
def dashboard():
    all_users = User.get_all()
    print(f"ALL: {all_users}")
    return render_template("index.html", users=all_users)
@app.route('/users/new')
def new():
    return render_template("create.html")
@app.route('/users/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)





