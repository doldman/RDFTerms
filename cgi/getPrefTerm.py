#!/usr/bin/env python
print("Content-Type: application/json")     # HTML is following
print()                               # blank line, end of headers

__author__ = 'dominic'

import sys
import json
import cgi, cgitb

cgitb.enable()
#form = cgi.FieldStorage()

#print(form.keys())
#print(form['auto'].value)
#print("animal,fish")
print('{"name":"animal"}')

#def myTest(data):#
#
#    myJson = json.loads(data)
#    return str(myJson)#
#
#data = sys.stdin.read()
#myResults = myTest(data)
#print(myResults)

