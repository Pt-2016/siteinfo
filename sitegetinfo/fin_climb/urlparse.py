#!/usr/bin/env python
#encoding=utf-8

import os,sys,time,string,Queue
import re,codecs,socket,httplib

from connection import Http_Connection,Https_Connection

class Ip_Identify():
	def __init__(self,url_name):
		self.url_	= url_name
	
	#identify url
	def url_identify(self):
		ip__,port__ = self.url_.split(':')
		port_list = ['80','81','82','7001','7002','8000','8080','8081','8082','8880','9090','9001']

		# there is ftp function
		if port__ == '21':
			print 'ftp server'
		# no develop

		elif port__ == '22':
			print 'ssh server'
		# there is ssh function

		elif port__ == '443' or port__ == '8443':
			httpsserver = Https_Connection(self.url_)
			httpsserver.httpsconnect()
		
		elif port__ in port_list:
			httpserver = Http_Connection(self.url_)	
			httpserver.httpconnect()

		else:
			#there use telnet connection
			# no develop
			print port__
	
	
