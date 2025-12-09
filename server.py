from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/') #root = route
def index():
    return f"""
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Basic</title>
  </head>
  <body>
    <h1>Home Page</h1>
    <hr>
  </body>
  </html>  
"""

@app.route('/name')
def name():
  return f'<h1>Wuttichai Buralek</h1>'

@app.route('/user/<username>')
def user(username):
  return f'<h1>My name is {username}</h1>'

@app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a, b):
  return f'<h1>{a} + {b} = {a + b}</h1>'

@app.route('/calculator/subtraction/<int:a>/<int:b>')
def subtraction(a, b):
  return f'<h1>{a} - {b} = {a - b}</h1>'

@app.route('/calculator/multiplication/<int:a>/<int:b>')
def multiplication(a, b):
  return f'<h1>{a} * {b} = {a * b}</h1>'

@app.route('/calculator/division/<a>/<b>')
def division(a, b):
  a = float(a)
  b = float(b) 
  return f'<h1>{a} / {b} = {a / b}</h1>'

@app.route('/secretkey/<uuid:sk>')
def my_secret_key(sk):
  return f'<h1>My secret key : {sk}</h1>'

# if __name__ == '__main__': ##ใช้สำหรับรันของ python
#   app.run(debug=True)
