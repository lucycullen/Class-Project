from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/results', methods=["GET", "POST"])
def results():
    data = dict(request.form)
    response = model.calculate_song(data)
    return render_template('results.html', response=response)
    
@app.route('/badges')
def badges():
    return render_template('badges.html')
