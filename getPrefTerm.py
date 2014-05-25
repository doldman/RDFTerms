#!/usr/bin/env python
print("Content-Type: text/html")     # HTML is following
print()                               # blank line, end of headers

__author__ = 'dominic'

import material
import cgi


#form = cgi.FieldStorage()
#search = form["keyword"].value
search = "a"

myJsonTerms = material.getPrefTermsbyName(search)
for result in myJsonTerms["results"]["bindings"]:
    print(result["term"]["value"])

