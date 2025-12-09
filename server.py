from flask import Flask

app = Flask(__name__)

@app.route('/') #root = route
def index():
    return f'<h1>Hello, World!</h1>'

@app.route('/name')
def name():
  return f'<h1>Wuttichai Buralek</h1>'

# if __name__ == '__main__': ##ใช้สำหรับรันของ python
#   app.run(debug=True)