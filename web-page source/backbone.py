# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, flash, redirect, url_for
from os.path import join
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gdictionary import rusgrab
import uuid
from werkzeug import secure_filename
from ast import literal_eval
import json

app = Flask(__name__)
app.secret_key = 'zaliznyak'
UPLOAD_FOLDER = "static"

# Route for the main page
@app.route("/")
def index():
    return render_template("index.html")

# Route for personal page:
@app.route("/kira")
def kira():
    return render_template("kira.html")
# Routes for personal page:
@app.route("/nadin")
def nadin():
    return render_template("nadin.html")
# Routes for personal page:
@app.route("/ilya")
def ilya():
    return render_template("ilya.html")

# Route for page with predictions:
@app.route("/prediction")
def prediction():
    return render_template("prediction.html",  query="", result="")

# Prediction from form input: send to morpho-module, get back output
@app.route("/prediction/form", methods=['GET', 'POST'])
def form_analyze():
    PATH_TO_DIC = os.path.abspath('examples.json') #insert path to examples.json here
    dic = json.loads(open(PATH_TO_DIC, encoding='utf8').read())
    query = request.values.get("message", "")
    result = rusgrab.main(query)
    # check for length
    if result == 1:
        flash("No more than 50 words!")
        return redirect(url_for('prediction'))
    # remove the header
    result = result[1:]
    result = [item.strip().split(",") for item in result]
    result = [[item[0], " ".join(item[1:])] for item in result]
    # get text for popups
    exp = []
    for item in result:
        gram = item[-1]
        g = ' '.join(list(reversed(gram.replace("о", "").split())))
        if g in dic:
            exp.append(dic[g])
        else:
            exp.append("No examples")
    return render_template("prediction.html", query=query, result=result, popup=exp)

# Analyze a file
@app.route("/prediction/file", methods=['GET', 'POST'])
def file_analyze():
    if request.method == 'POST':
        errors = []
        infile = request.files['file']
        infile.seek(0, os.SEEK_END)
        file_length = infile.tell()
        infile.seek(0)
        # check filesize
        if file_length > 20 * 1024 * 1024 + 1:
            errors.append("Filesize should be under 20Mb!")
        # rename file to avoid harmful ones
        filename = secure_filename(infile.filename)
        # check extension
        if '.' in filename and filename.rsplit('.', 1)[1] in ["txt"]:
            pass
        else:
            errors.append("File should have the .txt extension!")
        if errors:
            for error in errors:
                flash(error)
            return redirect(url_for('prediction'))
        # check encoding: utf-8 or win1251
        try:
            query = infile.read().decode('utf-8')
        except UnicodeDecodeError:
            try:
                query = infile.read().decode('cp1251')
            except UnicodeDecodeError:
                flash("Encoding should be UTF-8 or Win-1251!")
                return redirect(url_for('prediction'))
        # if everything is fine, read contents and send them for analysis
        result = rusgrab.main("###"+query)
        filename = str(uuid.uuid4())+'.txt'
        # save file with results on server and offer for download
        with open(join(UPLOAD_FOLDER, filename), 'wb') as out:
            out.write("".join(result).encode('utf8'))
    return render_template("prediction.html", result="", filename=filename)

# Write feedback results to a file
@app.route("/feedback/send/<result>", methods=['GET', 'POST'])
def send(result):
    result = literal_eval(result)
    for value in request.values:
        with open("feedback.csv", 'a+', encoding='utf8') as out:
            out.write(','.join([",".join(result[int(value)]), 
                str(request.values.get(value, ''))]) + '\n')
    return "Thank you for your feedback!"

# Suggest the user to give feedback
@app.route("/feedback/<result>")
def feedback(result):
    return render_template("feedback.html", result=literal_eval(result))

if __name__ == "__main__":
    app.run(debug=True)
