#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.classes.weatherYahoo import WeatherYahoo

class Core(object):
	_answer = []
	_sqlo = None
	_services = {
		'tiempo': WeatherYahoo,
		}

	def __init__(self):
		pass

	def instanceServices(self, service, args=[]):
		service = self._services[service]
		obj = service()
		if len(args) > 0 :
			obj._args = args
		return obj

	def getAnswer(self):
		return self._answer

	def makeAnswer(self,response):
		response = response.lower()
		array_response = response.split('+')
		if 'tiempo' in array_response:
			indexCommand,wordCommand=array_response.index('tiempo'),'tiempo'

		objServices = self.instanceServices(wordCommand,array_response[indexCommand+1:])
		objServices.execute()
		self._answer = objServices.getResult()
		return True
