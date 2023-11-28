from flask import Flask ,render_template 
app = Flask(__name__)   

@app.route('/')          
def index():
    return render_template("index.html")


@app.route('/<int:num>/<color_one>/<color_two>')
def index2(num,color_one,color_two):
    return render_template("index2.html",num=num,color_one=color_one,color_two=color_two)


if __name__=="__main__":   
    app.run(debug=True)    
