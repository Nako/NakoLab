'''
Created on 12.07.2011

@author: Nako
'''
#! /usr/bin/python
import sys
import feedparser
import socket

timeout = 120
socket.setdefaulttimeout(timeout)
feed_name = sys.argv[1]
feed_url     = sys.argv[2]
d = feedparser.parse(feed_url) #@UndefinedVariable
for s in d.entries:
    print feed_name + "|" + unicode(s.title).encode("utf-8") + "|" + unicode(s.link).encode("utf-8") + "\n"
