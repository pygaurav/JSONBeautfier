"""
********************************************************************************************
Created on : January, 31st, 2018
Developer : Gaurav Bhardwaj
Website: www.ittwist.com
********************************************************************************************
THE BELOW CODE CONTAINS THE SERVER SIDE CODE OR PYTHON/FLASK CODE
FEEL FREE TO USE THE CODE
"""

from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    """This code is the heart of the project. This will return the formatted JSON Back to user
    
    Returns:
        Updated JSON : String
        Error Message if any
    """
    
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
                ErrorName="Error While Parsing JSON"
            else:
                ErrorName=""
        else:
            ErrorName="Please Enter Something"
    return render_template('index.html',req_text=req_text,res_text=res_text,ErrorName=ErrorName)


@app.route("/response",methods=['GET', 'POST'])
def response():
    """This code is the heart of the project. This will return the formatted JSON Back to user
    
    Returns:
        Updated JSON : String
        Error Message if any
    """
    
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
                ErrorName="Error While Parsing JSON"
            else:
                ErrorName=""
        else:
            ErrorName="Please Enter Something"
    return render_template('response.html',req_text=req_text,res_text=res_text,ErrorName=ErrorName)
        


def formatJson(req_text,res_text):
    """This code will accept the request text and convert it to JSON
       and returns to the user the beautified JSON Stream.
    
    Arguments:
        req_text {str} -- [Requested Text - Unformatted JSON]
        res_text {str} -- [Response Text - Emptied]
    
    Returns:
        [res_text] -- [Response Text - Formatted JSON]
        [HasError] -- [Provides the flag for the error message]
    """

    try:
        json_req_form=json.loads(req_text)
        res_text=json.dumps(json_req_form, sort_keys=True, indent=4)
        HasError=False
    except Exception:
        HasError=True
        res_text=""
    return res_text,HasError

if __name__ == "__main__":
    app.run(debug=True)
