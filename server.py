#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
from lib.core.core import Core
import bottle
from bottle import run,route,request,response, error

@route('/')
def index():
	return "<h1>Bienvenido a All Web Services</h1>"

@route('/sentence/<id>/<words>')
def get_sentence(id,words):
	response.content_type = 'application/json'
	c = Core()
	c.makeAnswer(words)
	return json.dumps({"msg": c.getAnswer(), "cacheTime": 10000, "waitResponce": False, "understand": False, "users_ids": [id], } )

@error(404)
def error404(error):
	return json.dumps({"msg": "Error 404. Please, contact with support", "cacheTime": 0, "waitResponce": False, "understand": False, "users_ids": [id], } )

if __name__ == '__main__':
	run(host='localhost',port=8081,reloader=True, debug=True)
