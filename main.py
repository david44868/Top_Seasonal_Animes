from flask import Flask, render_template, url_for, request, redirect
from api_connection import get_list
# import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    season = request.form.get('season')
    year = request.form.get('year')
    return redirect(url_for('display', season=season, year=year))

@app.route('/display')
def display():
    season = request.args.get('season', None)
    year = request.args.get('year', None)
    titles, imgs, genres = get_list(season, year, client_id)
    return render_template('display.html', titles=titles, imgs=imgs, len=len(titles), season=season, year=year, genres=genres)

if __name__ == "__main__":
    app.run(debug=True)
