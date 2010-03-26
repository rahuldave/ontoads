---
layout: default
title: Pages
---


<p>
  {% for post in site.categories.article %} 
     <a href="/ontoads{{ post.url }}">{{ post.title }}</a><br>
  {% endfor %}
</p>
	
