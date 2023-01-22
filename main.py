import requests
from flask import Flask, render_template, request

NewsAPIKey = '6d0ef6b9337e4960a7f093652cfa6ce7'
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
        return render_template('search.html', search_articles=search_articles)

if __name__ == '__main__':
    app.run(debug=True)
