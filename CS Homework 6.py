from flask import Flask
__name__ =  "__main__"
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! My name is Oliver and this is my website."

if __name__ == "__main__":
    app.run(host="192.168.0.12", port=5000)
