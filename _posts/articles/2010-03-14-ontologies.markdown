---
layout: article
title: Ontologies
category: article
---

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
