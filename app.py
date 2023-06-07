from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your secret key'
app.static_folder = 'static'

@app.route('/')
def index():
    news = random.choice(['Putin dont prisedent, 
                          'Zirinovski is dead', 
                          'Portside is best programmer'])
    return render_template('index.html', news=news)
  
  
  if __name__ == "__main__":
      app.run(debug=True, port=80)
