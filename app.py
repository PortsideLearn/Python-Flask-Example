# importes
from flask import Flask, render_template, request, redirect, url_for, session
from jinja2 import Template
import random

# settings app
app = Flask(__name__)
app.secret_key = 'your secret key'
app.static_folder = 'static'

# create a main page
@app.route('/')
def index():
    # create random news for html page
    news = random.choice(['Putin dont prisedent', 
                          'Zirinovski is dead', 
                          'Portside is best programmer'])
    return render_template('index.html', news=news) # render html page from directory: /templates/index.html
    # Directory "/templates/" is standart directory in framework "Flask" for rendering html-pages
  
  # start application
  if __name__ == "__main__":
      app.run(debug=True, port=80)
     # port example: "127.0.0.1:port"
     # debug is - if your app returned error, flask return error to web-site
