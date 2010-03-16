---
layout: default
title: Why?
---

ADS's semantic web efforts stem from a desire to enable the creation of an easy 
to use, web based application using the IVOA which allows a user to perform:

* Structured Searching of Publications, Astronomical Objects, and Observations
* Faceted Browsing of Publications, Astronomical Objects, and Observations
* Creation of a Research Folders based on the above queries and browsing

See the second image below.

The choice of a semantic substrate, in addition allows publications, objects, 
observations to participate in an infrastructure which allows one to:

* create intelligent applications which can reason and inference with the 
semantic graph
* publish resources as Linked Data, externally indexed. 
* easily aggregate metrics of interest to publishers, funding agencies, etc
* let others build applications on this substrate using SPARQL queries, 
individual resources and appropriate collections

We will be carrying out these efforts as part of ADS Labs.

### Bootstrapping in ADS Labs

ADS Labs is an effort to put out more forward thinking, somewhat unstable 
applications, for intrepid users to try out and help us with feedback. The
applications will be incubated in ADS Labs before being pushed out to ADS users
at large.

1. The results of queries on a bibliographic database will be made available in rdf 
(and rdf-in-json). This is not a SPARQL endpoint, and there is no triple-store.
We will build  a user interface on the above (see first image below).
2. We will switch to a semantic backend with a SPARQL interface
3. Development on Ontologies (which this site details) continues and we will
repeat and rinse this process with Object and Observation Ontologies.
4. Finally we'll combine the databases so as to have one large semantically 
enabled database and an application to browse it as seen in the second image below.


### Examples of Applications

Here are examples of what such applications might look like:

![Faceted Browsing of Pubs](http://docs.google.com/present/File?id=dg4d27sr_91g9ffvgft_b)

![Apod Apps](http://docs.google.com/present/File?id=dg4d27sr_99dms5d3c8_b)
	
	
