#!/usr/bin/env python

import time

from elasticsearch import Elasticsearch

class Insert_Es():
	def __init__(self,i_id,target,port,title,design,server,status):
		self.i_id	= i_id
		self.target = target
		self.port	= port
		self.title	= title
		self.design	= design
		self.server	= server
		self.status	= str(status)

	def gettime(self):
		current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		return current_time

	def insert(self):
		inserttime = self.gettime()
		try:
			es = Elasticsearch('1.1.1.100:9200')
			s1 = es.index(index='pt_first',doc_type='site_info',id=self.i_id,body={'t_ip':self.target,'t_port':self.port,'t_title':self.title,'flag':self.design,'t_status':self.status,'t_servertype':self.server,'inserttime':inserttime})
			print 'Save ok'
		except Exception,e:
			print '[Exception is]',e
			


