from flask import Flask
app = Flask (__name__)

@app.route('/hello')
def hello():
  return 'Hello World!'

@app.route('/bye')
def the_end():
  return 'The end of the world is nigh!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
