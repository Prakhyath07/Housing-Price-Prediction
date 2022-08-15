import logging
from flask import Flask
from housing.logger import logging
from housing.exception import customException
import sys

app=Flask(__name__)



@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("testing exception module")
    except Exception as e:
        housing=customException(e,sys)
        logging.info(housing.error_message)
    logging.info("testing logger module")
    return "Machine Learning project housing price"

if __name__=="__main__":
    app.run(debug=True)