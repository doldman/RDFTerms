#!/usr/bin/env python
print("Content-Type: text/html")     # HTML is following
print()                               # blank line, end of headers

__author__ = 'dominic'

import sys
import json
import cgi, cgitb

form = cgi.FieldStorage()

print(form.keys())
print(form['terms'].value)



#def myTest(data):#
#
#    myJson = json.loads(data)
#    return str(myJson)#
#
#data = sys.stdin.read()
#myResults = myTest(data)
#print(myResults)

