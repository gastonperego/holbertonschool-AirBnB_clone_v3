#!/usr/bin/python3
"""Sdsdsd"""
from api.v1.views import app_views

@app_views.route("/status")
def a():
    """mdkjsnkd"""
    return {"status": "OK"}