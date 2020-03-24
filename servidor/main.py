from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Mi primer servidor python con flask'

if __name__ == "__main__":
    app.run()