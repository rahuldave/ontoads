# ADS Ontologies

## Prelim

### What?

Jay's Proposal:

[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/examples/1991ApJ...376L...5K.rdf](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/examples/1991ApJ...376L...5K.rdf)

### Why?

* Research Portfolios
* Structured Searching
* Faceted Browsing of Publications, Objects, and Observations
* Linked Data, externally indexed. Equivalent of ADS prominence on google.
* Create best practises for publishers, surveys, etc


### How?

Some numbers for ADS:

* citations: 39M (across databases)
* readership: 18M (90-day window)
* fulltext: 5M (journals, arXiv, ADS)
* astronomical objects: 240K (SIMBAD + NED)
* data products: 130K
* bibliographic groups: 200K

So this is hard. Obviously performance will be key.

Thus:

	Should we define first an internal non triple model and then an ads only ontology with equivalences to external ontologies, or should we go all the way and use external ontologies.

NOSQL? Columnstores? Etc?

### The Application

![Faceted Browsing of Pubs](http://docs.google.com/present/File?id=dg4d27sr_91g9ffvgft_b)

![Apod Apps](http://docs.google.com/present/File?id=dg4d27sr_99dms5d3c8_b)

## Ontologies

A way to describe a body of knowledge about the world.

### Owl

A language to describe ontologies and knowledge bases. Based on rdf and rdfs. Has 3 flavors in version 1: Full, DL, and Lite. OWL2 is now out but tools support is not yet mature.

### Why Owl-DL

	Finite Time Inferencing
	
VSTO and SWAN have used this approach.

Important Points: 

* Imports vs namespacing.
* DL vs Full, guarantees vs case-by-case

### Best Practises for Ontology term reuse and documentation?

* How does one document that only certain terms of certain ontologies will be used by us
* Again, do we put these under our own namespace? VSTO has used this approach.
* How do things scale with Ontology breadth?
* And with ontology imports vs the namespacing what are the considerations of hugely expanding the number of key concepts (`AnnotationProperties` issue)

### Keeping it simple: Completeness VS Usability

	Even though in our modelling we'll go all the way down to mathematics terms from SWEET we will never use these in our documents. They exist solely as support infrastructure. And even if we do have such assertions we will not expose them on queries. They are more appropriate for one-off details pages rather than for SPARQL or inferencing.
	
## ADS Labs

### Ontology as the view layer: web services

The results of queries to be made available in rdf (and rdf-in-json). This is not a SPARQL endpoint.
And there is no triple-store.

### Building our first tools

Build on the above.

### User testing

See what paths users take in existing ADS services (Jay) and see what they might take in an ADS Labs experimental interface. Ask young (and older) whippersnappers.

## Base Vocabularies

	1. Dublin Core : Used via namespace trick at multiple spots
	
	2. Dublin Core Terms: Used via namespace trick at multiple spots
	
It would be best to concatenate elements used from `dc` and `dct` into an individual OWL-DL document which is then imported everywhere whilst the actual vocabularies are never imported.

### Base OWL-DL formats

	3. FOAF-essential

	
A SWAN product, slightly hacked by me to be OWL-DL compatible: [view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/foaf-essential.owl](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/foaf-essential.owl)

There are some issues with `foaf:mbox` needing solving here.
	
	4. NASA SWEET formats
	
These are a base. I carefully picked formats so as to be modular, in the notion os an onion like fashion.

[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/sweetSome.owl](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/sweetSome.owl)
	
SWEET is otherwise too interconnected. I left out ontologies which relied on prior astro, physics, chem, and geo stuff. Specifically, I would have liked to have sciInstrument.owl (which wasnt particularly deep) and spaceCoordinates.owl which imported but didnt use astroPlanet. All Sweet ontologies can be seen [here](http://bitbucket.org/adsonto/adsontologies/src/tip/owl/sweet/).

Ed Chaya's ontologies have some Base, observational, and instrumental stuff, but they are not online any more. He reused SWEET where he found appropriate. VSTO defined their own terms, all in one big ontology. 


	5. SKOS-essential
	
[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/skos-essential.owl](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/skos-essential.owl)	

This is not enough for our needs. I am investigating alternatives that allow (a) `OrderedCollections` and (b) allow representing both `Concepts` and `Collections` in `Collections`.



### OWL-DL for existing IVOA SKOS vocabularies

I have transformed AVM and AAKeys to be OWL-DL compatible SKOS and modularized the documents. 

	6. AVM in SKOS-Essential
	
[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/AVM.rdf](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/AVM.rdf)

	7. AAKeys in SKOS-Essential

[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/AAkeys.rdf](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/AAkeys.rdf)

### Agents and Provenance

These also depend on some other SWAN ontologies:
![Dependencies](http://swan.mindinformatics.org/spec/1.2/images/SWAN-Agents-Module.png)

* [Provenance, Authoring and Versioning](http://swan.mindinformatics.org/ontologies/1.2/pav.owl)
* [Collections](http://swan.mindinformatics.org/ontologies/1.2/collections.owl)
* [Reification](http://swan.mindinformatics.org/ontologies/1.2/reification.owl)

![Person Names](http://swan.mindinformatics.org/imgs/agents-fig-1.png)
![mapping to foaf](http://swan.mindinformatics.org/imgs/agents-fig-3.png)
![Reification](http://swan.mindinformatics.org/spec/1.2/images/SWAN-Agents-Aka-Reified.png)

Using these we have:

	8. SWAN Agents
	
[view-source:http://swan.mindinformatics.org/ontologies/1.2/agents.owl](view-source:http://swan.mindinformatics.org/ontologies/1.2/agents.owl)

The SWAN folks are **willing to make changes we might want to these ontologies** to accomodate our needs.

### CiTO and BibO

[Bibo Article](http://bibliontology.com/content/article)

We'll use a OWL-DL version if `bibo` I've created for most of our bibliographic needs.

	9. BIBO Ontology: Modified for OWL-DL
	
[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/bibo.xml.owl](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/bibo.xml.owl)

CITO adds a whole parallel set of terms. So does SWAN. We dont need this. We need to extract just that much which uses SWAN provenance and agents to 'type' citations.

![example](http://swan.mindinformatics.org/imgs/citations-2.png)

We also want to capture provenance from arxiv or elsewhere to journals, and distinguish various levels of publication such as a conference talk for ADASS, non peer-reviews from an A and A article. We'll use SWAN `pav` and `agents` for these too.

This is where some of the effort in the **ADS biblio Ontology** will go.

## Putting it together

An OWL document needs to be delivered for each of the below. What other concepts do you think I have missed?

### ADS Base

Stuff in here must be used by more than one ontology on Biblio, Object, and Observation. This would include co-ordinate systems, units, surveys, funding agencies, collaborations, that we need to build on SWEET and FOAF. Will also include SKOS, SWAN Collections, SWAN reification. This is under construction (V0.1 end March/early April).

### ADS Biblio

ADS extensions for citing to BIBO, reification and provenance of a paper are appropriate here. Will include SKOS thesauri ontologies, SWAN PAV, BIBO, SWAN Agents. This is under construction. 2 SKOS thesauri have been converted to be SKOS-Essential OWL-DL. This effort includes identifying the appropriate SKOS subset. (V0.1 early April/ mid April)

Jay's corpus will be rewritten (April) to use these two ontologies, with other ontologies either namespaced in (where appropriate) or directly imported. (Importing is transitive).

### ADS Observation

This is untouched yet and will start with instrumentation and move to talking about observations, datasets, surveys, instruments and their connections. Who's volunteering?

### ADS Objects

This will be a thin veneer over NED and SIMBAD data models. Will need to talk about datasets (possible refactor into ADS Base). Help is welcome!