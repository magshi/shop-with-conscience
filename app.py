from flask import Flask, request, render_template, g, redirect, url_for, flash
from jinja2 import Template
app = Flask(__name__)

goodguide_data = {
	'patagonia': {
		'environment': 8.9,
		'society': 7.6
	},
	'nike': {},
	'dockers': {},
}
 
@app.route('/')
def index():
	return render_template("index.html")

def search():
	pass

if __name__ == '__main__':
	app.run()