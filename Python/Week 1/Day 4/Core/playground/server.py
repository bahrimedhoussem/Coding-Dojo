from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/play')
def boxes():
   return render_template('index.html')


   
@app.route('/play/<int:num>') 
def boxes2(num):
   return render_template('index2.html',num=num)

@app.route('/play/<int:num>/<color>') 
def boxes3(num,color):
   return render_template('index2.html',num=num,color=color)

if __name__=="__main__":       
    app.run(debug=True)    



