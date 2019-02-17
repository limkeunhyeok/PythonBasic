# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:46:56 2019

@author: USERPC
"""

"""
Routes and views for the flask application.
"""

from flask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return "Hello world!"

@app.route('/contact')
def contact():
    return "contact"

@app.route('/about')
def about():
    """Renders the about page."""
    return "about"
