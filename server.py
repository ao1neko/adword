# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request
from randomtopic import makelist
from texttopic import maketextlist,maketextlist2
import numpy as np
import random
import gensim
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from pykakasi import kakasi



app = Flask(__name__)

message="投稿がありません"





model = gensim.models.KeyedVectors.load_word2vec_format('word2.vec', binary=False)


kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()



@app.route('/')
def index():
    return render_template('home.html')




@app.route('/page1')
def home():
    return render_template('page1.html',message=message)




@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        text = request.form['text']
        message="投稿がありません"
        key=conv.do(text)
        
        textlist=maketextlist(key,text)

        num=random.randint(0,17)
        ramdomlist=makelist(text)

        text2=model.most_similar([text])[0][0]
        key2=conv.do(text2)

        textlist2=maketextlist2(key2,text2)

        return render_template('page1.html',text =textlist , text2=ramdomlist[num],text3=textlist2,message=message)

    else:
                # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))



def main():
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()