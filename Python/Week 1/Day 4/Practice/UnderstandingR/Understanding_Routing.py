from flask import Flask  
app = Flask(__name__)

@app.route('/')          
def hello_world():

    return 'Hello World!'  

@app.route('/dojo')
def mention():
  
   return 'Dojo!'    

@app.route('/say/flask')
def greeting_flask():
   return "Hi Flask!"

@app.route('/say/michael')
def greeting_michael():
    return "Hi michael!"

@app.route('/say/<name>')
def greeting_john():
    return "Hi john!"

@app.route('/repeat/<int:count>/<message>')
def repeat_message(count,message='hello'):
    repeated_message = count * message
    
    return  repeated_message




if __name__=="__main__":   
    app.run(debug=True)    



