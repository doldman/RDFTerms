__author__ = 'dominic'

from SPARQLWrapper import SPARQLWrapper, JSON

def getPrefTermsbyName(strInput):
    """
    A SPARQL query
    :rtype : json
    :param strInput: A preferred term
    :return: the id and the id of the broader terms
    """
    sparql = SPARQLWrapper("http://collection.britishmuseum.org/sparql")
    sparql.setQuery("""

    PREFIX crm: <http://erlangen-crm.org/current/>
    PREFIX fts: <http://www.ontotext.com/owlim/fts#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX thes: <http://collection.britishmuseum.org/id/thesauri/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT DISTINCT ?id ?term ?broader
    WHERE
    {
      ?id skos:inScheme thes:material .
      ?id skos:prefLabel ?term .
      ?id skos:broader ?broader .
       FILTER regex(str(?term),'^""" + strInput + """','i')
    }

    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    #return results

    for result in results["results"]["bindings"]:
        print(result["term"]["value"]) # + " : " +  result["id"]["value"])

def getTermbyID(id):
    sparql = SPARQLWrapper("http://collection.britishmuseum.org/sparql")
    sparql.setQuery("""

    PREFIX crm: <http://erlangen-crm.org/current/>
    PREFIX fts: <http://www.ontotext.com/owlim/fts#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX thes: <http://collection.britishmuseum.org/id/thesauri/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT DISTINCT ?prefTerm
    WHERE
    {

        """ + id + """skos:prefLabel ?prefTerm .

    }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

    #for result in results["results"]["bindings"]:
    #    print(result["term"]["value"] + " : " +  result["id"]["value"])

def getNarrowbyID(id):
    """

    :param id:
    :return:
    """
    print(id)
    sparql = SPARQLWrapper("http://collection.britishmuseum.org/sparql")
    sparql.setQuery("""

    PREFIX crm: <http://erlangen-crm.org/current/>
    PREFIX fts: <http://www.ontotext.com/owlim/fts#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX thes: <http://collection.britishmuseum.org/id/thesauri/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT DISTINCT ?narrowid
    WHERE
    {

      ?narrowid skos:broader """ + id + """ .

    }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

#results = getPrefTermsbyName("a")
#for result in results["results"]["bindings"]:
#        print(result["term"]["value"]) #+ " : " +  result["id"]["value"])





#myTerm = getPrefTermsbyName('an')
#for result in myTerm["results"]["bindings"]:
#    print("\n" + "preferred term:" + result["term"]["value"] + " , id:" +  result["id"]["value"] + "\n")
#    print("broader: " + result["broader"]["value"])
#    myNarrow = getNarrowbyID("<" + result["broader"]["value"] + ">")
#    for result1 in myNarrow["results"]["bindings"]:
#        print("Narrow: " + result1["narrowid"]["value"])
#        myNarrowTerm = getTermbyID("<" + result1["narrowid"]["value"] + ">")
#        for result2 in myNarrowTerm["results"]["bindings"]:
#            print(result2["prefTerm"]["value"])

