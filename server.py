from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/fav_player', methods=['GET'])
def login():
    return ""

if __name__ == "__main__":
  app.run()

