from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()
