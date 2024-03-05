from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from users import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def dashboard():
    all_users = User.get_all()
    print(f"ALL: {all_users}")
    return render_template("index.html", users=all_users)
@app.route('/users/new')
def new():
    return render_template("new_users.html")
@app.route('/users/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')


@app.route('/users/delete/<int:user_id>')
def delete(user_id):
    data={
        'id':user_id
    }
    User.remove(data)
    return redirect('/users')


@app.route('/user/show/<int:user_id>')
def show(user_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    user=User.get_one(user_id)
    return render_template("show_user.html",user=user)

@app.route('/users/update/<int:user_id>',methods=['POST'])
def update(user_id):
    data= {
        'id' : user_id,
        **request.form
    }
    User.edit(data)
    return redirect('/')

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    
    user = User.get_one(user_id)
    return render_template ('Edit.html' , user = user)



if __name__ == "__main__":
    app.run(debug=True, port=5001)





