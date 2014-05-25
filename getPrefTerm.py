__author__ = 'dominic'

import material
import cgi


#form = cgi.FieldStorage()
#form["letters"]


myJsonTerms = material.getPrefTermsbyName("")
for result in myJsonTerms["results"]["bindings"]:
    print(result["term"]["value"])

