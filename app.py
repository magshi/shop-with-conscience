from flask import Flask, request, render_template, g, redirect, url_for, flash
from jinja2 import Template
app = Flask(__name__)

from example import example

goodguide_data = {
	'Patagonia': {
		'environment': 8.9,
		'society': 7.6
	},
	'nike': {},
	'dockers': {},
}

example_product = {
	'name': 'swater',
	'price': '25.99',
	'color': 'red'
}
 
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/product')
def product():
	return render_template("product.html", product = example['product'][0])

def search():
	# user searches for a product, i.e., 'sweater' or 'hat'
	# make a call to the Macy's API and return a certain number of results for the query
	# for each of the products returned, refer to the goodguide_data dictionary and retrieve that company/brand's scores (health, environment, society) + the average of those scores, and append it to the page alongside the results
	# display product name, brand, scores, image, price, and a link to the macy's.com product page if the user wants to buy it
	pass

if __name__ == '__main__':
	app.run()
