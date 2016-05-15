#!/usr/bin/env python

import re,httplib

class Http_Connection():
	def __init__(self,http_url):
		self.link_url = http_url
	
	def handle_title(self,tit):
		if tit.__len__() == 0:
			return tit
		else:
			return tit[0][7:-8]

	def handle_hd(self,head):
		for h in head:
			for l in h:
				if l == 'server':
					return h[1]
				else:
					pass	
	def handle_design(self,hea):
		for m in hea:
			for n in m:
				if n == 'x-powered-by':
					return m[1]
				else:
					pass 
	
	def handle_jump(self,head):
		for x in head:
			for y in x:
				if y == 'location':
					return x[1]
				else:
					pass


	def httpconnect(self):
		url,port = self.link_url.split(':')
		try:
			conn	= httplib.HTTPConnection(url,port,timeout = 5)
			conn.request("GET","/")
			ress	= conn.getresponse()
			stat	= ress.status
			heads	= ress.getheaders()
			content	= ress.read()
			ser_ress= ress.msg
			server_t= re.findall('<title>.*</title>',content)
		
			s_title = self.handle_title(server_t)
			type_ser= self.handle_hd(heads)
			power_by= self.handle_design(heads)
		
			if stat == 302:
				print 302
				jumpurl = self.handle_jump(heads)
				print '\33[34m{0:<20}\33[31m|{1:<18}\33[35m|{2:^}\33[32m{3:<20}'.format(self.link_url,type_ser,s_title,jumpurl)
			elif stat == 404:
				print '%s:Server 404'%self.link_url
			else:
				print 200	
				print '\33[34m{0:<20}\33[31m|{1:<18}\33[35m|{2:^}'.format(self.link_url,type_ser,s_title)


		except Exception,e:
			print '[Exception]',e
			pass



class Https_Connection():
	def __init__(self,https_url):
		self.link_url = https_url
	
	def httpsconnect(self):
		url,port = self.link_url.split(':')
		print url,port



