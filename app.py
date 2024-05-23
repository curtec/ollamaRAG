from flask import Flask

#Create app
app = Flask(__name__)

# Create end points - routes
@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)