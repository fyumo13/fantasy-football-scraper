from flask import Flask, render_template
from scrape import scrape

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('fantasy-football.html', news=scrape())

if __name__ == "__main__":
    application.run()