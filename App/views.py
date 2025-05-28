from flask import Flask, render_template, request, url_for
from App import app


@app.route('/')
def index():
    return render_template('index.html')