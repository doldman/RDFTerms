__author__ = 'dominic'

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://collection.britishmuseum.org/sparql")
sparql.setQuery("""


PREFIX crm: <http://erlangen-crm.org/current/>
PREFIX fts: <http://www.ontotext.com/owlim/fts#>

SELECT DISTINCT ?object
{ ?object crm:P102_has_title ?title .                    #Find the title resource for an object
  ?title rdfs:label ?label .                              #find the label attached to that title
  <Rosetta:Stone> fts:matchIgnoreCase ?label              #match the 'Rosetta' and 'Stone' tokens in the label
                                                          #(N.B. this accesses the OWLIM-specific text/token index)
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["object"]["value"])