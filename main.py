import requests
from decouple import config
from flask import Flask, render_template, request

NewsAPIKey = config('NEWS_API_KEY')
country='in'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getNews():
    url = ('http://newsapi.org/v2/top-headlines?'
           'country={}&apiKey={}').format(country,NewsAPIKey)
    news_data = requests.get(url).json()
    articles= news_data['articles']
    return render_template('news.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
