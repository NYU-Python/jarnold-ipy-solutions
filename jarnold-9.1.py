#!/usr/bin/env python


from flask import Flask
import os
import urllib


app = Flask(__name__) 


@app.route('/')
def index():
    return flask.render_template('flask_home.html')
    

# Pulling in stock prices

@app.route('/get_stock', methods=['POST'])
def get_stock():
	my_ticker = flask.request.form['ticker']
	stock_price = get_web_address(my_ticker)
	return flask.render_template('flask_stock_price.html', ticker = my_ticker, price = stock_price)

def get_web_address(my_ticker):
	stock_api = 'http://finance.yahoo.com/d/quotes.csv?s={}&f=a'
	base_link = stock_api.format(my_ticker)
	stock_price = urllib.urlopen(base_link).read().rstrip('\n')
	return stock_price
	


if __name__ == '__main__':
    app.run(debug=True)    # app starts serving in debug mode
