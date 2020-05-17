from flask import *
from chat import *
import nltk
import csv
import random
from extracting_pdf import *
from queryClassifier import *
from tagging_with_spacy import *
from techBot import *

app = Flask(__name__)  
f=''
ff=''
@app.route('/')  
def upload():  
    return render_template("test.html")  
 
@app.route('/home', methods = ['POST'])  
def success():
    global f,ff
    if request.method == 'POST':  
        f = request.files['file']
        print(f)
        print(type(f))
        fn=str(f)
        fn=fn[15:]
        ff=fn[:-22]
        print(ff)
        f.save(f.filename)
        pdfparser(ff)
        tagging(ff)
        return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    query_type=mainQuery(userText)
    if query_type=="generic":
        return str(genericResponse(userText))
    elif query_type=="tech":
        return str(techChat(userText))
    else:
        return "Sorry.No idea..."
  
if __name__ == '__main__':  
    app.run() 
