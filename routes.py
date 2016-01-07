from flask import Flask, request, render_template, url_for
from app import app


@app.route('/')
def index():
    return 'Welcome!'
