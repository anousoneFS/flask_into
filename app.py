from flask import Flask
from flask import render_template,redirect,url_for
from flask import request

app = Flask(__name__)

news = {
        1:{'id':1,'title':'colona-19 virus','detail':'colona-19 finally end!!'},
        2:{'id':2,'title':'face mask','detail':'recently face mask protect your body from colona-19 virus'},
        3:{'id':3,'title':'man u vs liver','detail':'man u win'}
    }

@app.route('/')

def index():
    name = 'anousone worlakoumman'
    
    return render_template('index.html',name=name, news=news.values())

@app.route("/news/<id>/")
def show_news_item(id):
    new = news[int(id)]
    return render_template('news_item.html',
    title = new['title'],
    detail = new['detail']
    )

def new_news_item(title, body):
    new_id = max(news.keys()) + 1
    return {
        'id':new_id,
        'title':title,
        'detail':body
    }

@app.route("/news/create/", methods=['post'])
def create_news_item():
    # return "title:" + request.form['title'] + "body:" + request.form['body']
    # return "title:" + request.args['title'] + "body:" + request.args['body']
    item = new_news_item(request.form['title'], request.form['body'])
    news[item['id']] = item
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True) 
