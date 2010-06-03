#a parser of spires and ads bibtexts. we only parse refs. At this point we dont have
#expressions so we output citation objects in n3 form.

#what we prolly ought to do is to instantiate objects if they have a bibcode and use
#cites

#whats our cites policy?W->E and E->E?

preamble="""
@prefix cito: 	<http://purl.org/net/cito/>.
@prefix rdf: 	<http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix rdfs:	<http://www.w3.org/2000/01/rdf-schema#>.
@prefix dc:  	<http://purl.org/dc/elements/1.1/>.
@prefix foaf:	<http://xmlns.com/foaf/0.1/>. 	
@prefix dcterms: <http://purl.org/dc/terms/>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix adsbase: <http://github.com/rahuldave/ontoads/owl/adsbase.owl#>.
@prefix agent: <http://swan.mindinformatics.org/ontologies/1.2/agents/>.
@prefix pav: <http://swan.mindinformatics.org/ontologies/1.2/pav/>.
@prefix adsbib: <http://github.com/rahuldave/ontoads/owl/adsbib.owl#>.
@prefix skos: <http://www.w3.org/2004/02/skos/core#>.
@prefix aakeys: <http://github.com/rahuldave/ontoads/owl/AAKeys.rdf#>.
@prefix pacs: <http://github.com/rahuldave/ontoads/owl/pacs.rdf#>.
#get basic configuration instances from below
@prefix adsconfig: <http://adsadbs.cfa.harvard.edu/ads/adsconfig#>.
@prefix : <http://adsadbs.cfa.harvard.edu/ads/adsbibdata#>

<>  a cito:CitationMetadata ; # work
    a cito:EntityMetadata ; # work
    #add something here for expression versioning
	cito:cites <http://adsabs.harvard.edu/abs/2007PhRvL..98v1601G> ;  
	cito:citesAsSourceDocument <http://adsabs.harvard.edu/abs/2007PhRvL..98v1601G> ;
	pav:importedFromSource  adsconfig:ADS;
	pav:importedBy adsconfig:adsrdf002; #if we had manual data entry how would we model?
	pav:importedOn	"Wed Jun  2 22:23:55 EDT 2010"^^xsd:dateTime ;
	pav:lastUpdateOn	"Wed Jun  2 22:24:41 EDT 2010"^^xsd:dateTime ;
.
"""

print preamble
thedocument="<http://adsabs.harvard.edu/abs/2007PhRvL..98v1601G>"
from pybtex.database.input import bibtex
parser = bibtex.Parser()
bib_data = parser.parse_file('./refs.spires.bbl')
for keyentry in bib_data.entries.keys():
    n3key="__".join(keyentry.split(":"))
    print ":"+n3key,"a adsbib:Citation;"
    print "\tadsbib:citationText \"\"\""
    for item in bib_data.entries[keyentry].fields.keys():
        print "\t\t",item,":",bib_data.entries[keyentry].fields[item]
    print "\t\"\"\";"
    print "\t adsbib:citationFrom",thedocument+";"
    print "."
    print thedocument,"adsbib:hasCitation",":"+n3key,"."
    
    print "#======================="


