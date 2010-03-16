---
layout: article
title: Using Ontologies
category: article
---

This page collects top-level information about the ontologies we will use. More
details are linked in under each heading.

### Base Vocabularies

	1. Dublin Core : Used via namespace trick at multiple spots
	
	2. Dublin Core Terms: Used via namespace trick at multiple spots
	
It would be best to concatenate elements used from `dc` and `dct` into an 
individual OWL-DL document which is then imported everywhere whilst the actual 
vocabularies are never imported.

### Base OWL-DL formats

	3. FOAF-essential

	
A SWAN product, slightly hacked by me to be OWL-DL compatible: 
[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/foaf-essential.owl](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/foaf-essential.owl)

There are some issues with `foaf:mbox` needing solving here.
	
	4. NASA SWEET formats
	
These are a base. I carefully picked formats so as to be modular, in the notion 
of an onion like fashion.

[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/sweetSome.owl](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/sweetSome.owl)
	
SWEET is otherwise too interconnected. I left out ontologies which relied on 
prior astro, physics, chem, and geo stuff. Specifically, I would have liked to 
have sciInstrument.owl (which wasnt particularly deep) and spaceCoordinates.owl 
which imported but didnt use astroPlanet. 
All Sweet ontologies can be seen [here](http://bitbucket.org/adsonto/adsontologies/src/tip/owl/sweet/).

Ed Chaya's ontologies have some Base, observational, and instrumental stuff, 
but they are not online any more. He reused SWEET where he found appropriate. 
VSTO defined their own terms, all in one big ontology. 


	5. SKOS-essential
	
[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/skos-essential.owl](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/skos-essential.owl)	

This is not enough for our needs. I am investigating alternatives that allow 
(a) `OrderedCollections` and (b) allow representing both `Concepts` and 
`Collections` in `Collections`.



### OWL-DL for existing IVOA SKOS vocabularies

I have transformed AVM and AAKeys to be OWL-DL compatible SKOS and modularized 
the documents. 

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

The SWAN folks are **willing to make changes we might want to these ontologies** 
to accomodate our needs.

### CiTO and BibO

[Bibo Article](http://bibliontology.com/content/article)

We'll use a OWL-DL version if `bibo` I've created for most of our bibliographic 
needs.

	9. BIBO Ontology: Modified for OWL-DL
	
[view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/bibo.xml.owl](view-source:http://bitbucket.org/adsonto/adsontologies/raw/6719c72e4944/owl/bibo.xml.owl)

CITO adds a whole parallel set of terms. So does SWAN. We dont need this. We 
need to extract just that much which uses SWAN provenance and agents to 'type' 
citations.

![example](http://swan.mindinformatics.org/imgs/citations-2.png)

We also want to capture provenance from arxiv or elsewhere to journals, and 
distinguish various levels of publication such as a conference talk for ADASS, 
non peer-reviews from an A and A article. We'll use SWAN `pav` and `agents` for 
these too.

This is where some of the effort in the **ADS biblio Ontology** will go.
