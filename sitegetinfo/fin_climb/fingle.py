#!/usr/bin/env python
#encoding=utf-8

import os,sys,time,string,Queue
import re,codecs,socket,httplib
import threading

from datetime import datetime
from urlparse import Ip_Identify


E_time  = time.strftime('%Y-%m-%d',time.localtime(time.time()))
E_stat  = 999
E_server= 'unknown'
E_tit   = 'Exception Link!'


def climb_url(url_str):
	url_ = Ip_Identify(url_str)
	url_.url_identify()


