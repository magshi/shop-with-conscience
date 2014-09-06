from flask import Flask, request, render_template, g, redirect, url_for, flash, stream_with_context, Response, jsonify
from jinja2 import Template
import requests
import os
from werkzeug.contrib.cache import SimpleCache
from pprint import pprint
import re

cache = SimpleCache()
app = Flask(__name__)

from example import example

goodguide_ratings = {
	'Patagonia': {
		'health': None,
		'environment': 8.9,
		'society': 7.6,
		'average': 6.9
	},
	'Nike': {
		'health': None,
		'environment': 7.4,
		'society': 6.4,
		'average': 6.9
	},
	'Adidas': {
		'health': None,
		'environment': 7.2,
		'society': 5.9,
		'average': 6.5
	},
	'Michael Kors': {
		'health:': 0,
		'environment': 6.2,
		'society': 5.7,
		'average': 3.9
	},
	'Reebok': {
		'health': None,
		'environment': 7.2,
		'society': 5.9,
		'average': 6.5
	},
	'Calvin Klein': {
		'health': None,
		'environment': 5.5,
		'society': 5.6,
		'average': 5.5
	},
	'Puma': {
		'health': 6.0,
		'environment': 6.1,
		'society': 5.8,
		'average': 6.0
	},
	'Ralph Lauren': {
		'health': 6.0,
		'environment': 5.7,
		'society': 5.4,
		'average': 5.7
	},
	'Style&co.': {
		'health': None,
		'environment': 5.4,
		'society': 5.0,
		'average': 5.2
	},
	'The North Face': {
		'health': None,
		'environment': 6.2,
		'society': 4.9,
		'average': 5.6
	}
}

search_data = [
	example['product'][0],
	example['product'][0],
	example['product'][0],
]

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/search')
def search():
	# request.form['search']
	# user searches for a product, i.e., 'sweater' or 'hat'
	# make a call to the Macy's API and return a certain number of results for the query
	# for each of the products returned, refer to the goodguide_data dictionary and retrieve that company/brand's scores (health, environment, society) + the average of those scores, and append it to the page alongside the results
	# display product name, brand, scores, image, price, and a link to the macy's.com product page if the user wants to buy it
	products = [1574297, 841315, 1493858, 1521058, 1493910, 1493858, 1573194, 1426103, 1668993, 1528466, 1481637, 921111]

	product_data = []

	for product_id in products:
		# requestUri = 'http://api.macys.com/v4/catalog/product/%s(productdetails(price,summary,availability),promotions)?retrieveallupcs=true' % (product_id)
		requestUri = 'http://api.macys.com/v3/catalog/product/%s' % (product_id)
		r = requests.get(requestUri, headers={'Accept':'application/json', 'X-Macys-Webservice-Client-Id': 'neohack14'}, stream=False)
		product_data.append(r.json()['product'][0])

	search_data = product_data

	for index, product in enumerate(search_data):
		product_name = product['summary']['name']
		for brand, scores in goodguide_ratings.iteritems():	
			brand_match = re.search(brand, product_name)
			if brand_match:
				brand = brand_match.group()
				search_data[index]['brand'] = brand
				search_data[index]['scores'] = goodguide_ratings[brand]

	return render_template("index.html", products = search_data)

if __name__ == '__main__':
	app.run(debug=True)

	# render all the content beforehand
	# hide it
	# when the button is pressed, show it
	# http://api.macys.com/v3/catalog/category/index?category=118&depth=1
