import batch
import priv
import boto3
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("webpage.html")

@app.route("/quote")
def getRandQuote():
    
    idNum = str(random.randint(1,30))
    Quote = priv.table.get_item(Key={"id": idNum})

    return jsonify(Quote.get("Item"))

if __name__ == "__main__":
    app.run(debug=True)








    
    

