#!/usr/bin/python3
"""Sdsdsd"""
from api.v1.views import app_views
import json

@app_views.route("/status")
def a():
    """mdkjsnkd"""
    return json.dumps({"status": "OK"})