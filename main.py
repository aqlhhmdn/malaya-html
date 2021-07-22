from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_restful import Resource, Api, reqparse
import malaya
import json
from pprint import pprint
import numpy as np

app = Flask(__name__)

@app.route('/')
def submit():
    return render_template("index.html")

@app.route('/word2num', methods=['GET','POST'])
def word2num():
    if request.method == "POST":
        word = request.form["w2n"]
        #return redirect(url_for("word", wrd=word))
        num = str(malaya.word2num.word2num(word))
        return render_template("index.html", val_w2n=num)
    else:
        return render_template("index.html")

@app.route('/num2word', methods=['GET','POST'])
def num2word():
    if request.method == "POST":
        num = int(request.form["n2w"])
        word = str(malaya.num2word.to_cardinal(num))
        return render_template("index.html", val_n2w=word)
    else:
        return render_template("index.html")

@app.route('/normalize', methods=['GET','POST'])
def normalize():
    if request.method == "POST":
        text = request.form["nrml"]
        corrector = malaya.spell.probability()
        normalizer = malaya.normalize.normalizer(corrector)
        text_nrml = normalizer.normalize(text)
        y = json.loads(json.dumps(text_nrml))
        txt = y["normalize"]
        return render_template("index.html", val_nrml=txt)
    else:
        return render_template("index.html")

@app.route('/nsfw', methods=['GET','POST'])
def nsfw():
    if request.method == "POST":
        text = request.form["nsfw"]
        lexicon_model = malaya.nsfw.lexicon()
        text_nsfw = str(lexicon_model.predict([text]))
        return render_template("index.html", val_nsfw=text_nsfw)
    else:
        return render_template("index.html")

@app.route('/token', methods=['GET','POST'])
def token():
    if request.method == "POST":
        text = request.form["tkn"]
        tokenizer = malaya.preprocessing.Tokenizer()
        text_tkn = tokenizer.tokenize(text)
        return render_template("index.html", val_tkn=text_tkn)
    else:
        return render_template("index.html")

@app.route('/spell', methods=['GET','POST'])
def spell():
    if request.method == "POST":
        text = request.form["spll"]
        prob_corrector = malaya.spell.probability()
        text_spll = prob_corrector.correct_text(text)
        return render_template("index.html", val_spll=text_spll)
    else:
        return render_template("index.html")

#@app.route("/word2num/<wrd>")
#def word(wrd):
    #num = str(malaya.word2num.word2num(wrd))
    #return render_template("insert.html", value=num)

#app.run(use_reloader=True, debug=False)
