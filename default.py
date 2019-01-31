from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    req_text=""
    res_text=""
    ErrorName=""
    if request.method == 'POST':
        #Code for handling the POST Logic
        req_text=request.form['requested_text']
        res_text=request.form['response_text']
        if req_text.strip()!="":
            res_text,HasError=formatJson(req_text,res_text)
            if HasError:
                ErrorName="Error While Parsing JSON String"
            else:
                ErrorName=""
        else:
            ErrorName="Please Enter Something"
        
    return render_template('index.html',req_text=req_text,res_text=res_text,ErrorName=ErrorName)


def formatJson(req_text,res_text):
    try:
        json_req_form=json.loads(req_text)
        res_text=json.dumps(json_req_form, sort_keys=True, indent=4)
        HasError=False
    except Exception:
        HasError=True
        res_text=""
    return res_text,HasError

if __name__ == "__main__":
    app.run()
