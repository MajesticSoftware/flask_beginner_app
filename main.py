from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Regine and Robin"

if __name__ == '__main__':
    app.run(debug=False)