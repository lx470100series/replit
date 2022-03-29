from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World I love programming, and so should you!!'

app.run(host='0.0.0.0', port=8080)
