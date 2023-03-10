import requests
from flask import Flask, render_template, request
from config import api_key

NewsAPIKey = api_key
country='in'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getNews():
    url = ('http://newsapi.org/v2/top-headlines?'
           'country={}&apiKey={}').format(country,NewsAPIKey)
    news_data = requests.get(url).json()
    articles= news_data['articles']
    return render_template('news.html', articles=articles)
    
@app.route('/search', methods=['GET', 'POST'])
def searchNews():
    if request.method == 'POST':
        keyword = request.form['query']
        url = ('http://newsapi.org/v2/everything?'
               'q={}&apiKey={}').format(keyword,NewsAPIKey)
        searcch_data = requests.get(url).json()
        search_articles= searcch_data['articles']
        return render_template('search.html', search_articles=search_articles, keyword=keyword)

@app.route('/category/<name>', methods=['GET', 'POST'])
def categoryNews(name):
    #take category name from url
    category = name

    if request.method == 'GET':
        url = ('http://newsapi.org/v2/top-headlines?'
               'country={}&category={}&apiKey={}').format(country,category,NewsAPIKey)
        category_data = requests.get(url).json()
        category_articles= category_data['articles']
        if category_articles == []:
                url = ('http://newsapi.org/v2/everything?'
                'q={}&apiKey={}').format(category,NewsAPIKey)
                category_data = requests.get(url).json()
                category_articles= category_data['articles']
                return render_template('category.html', category_articles=category_articles, category=category)
        else:
            return render_template('category.html', category_articles=category_articles, category=category)

if __name__ == '__main__':
    app.run(debug=True)
