from flask import Flask, render_template, session , redirect 
app = Flask(__name__)
app.secret_key="your_secret_key"

@app.route('/')
def count():
    if 'counter' not in session :
        session['counter'] = 1
    
    return render_template("index.html", counter=session['counter'])

@app.route('/destroy_session')
def clear():
    session['counter'] +=1    
    return render_template("index.html",counter=session['counter'])   


@app.route('/reset')
def reset():
    session['counter'] =1
    return redirect('/') 


if __name__=="__main__": 
    app.run(debug=True ) 