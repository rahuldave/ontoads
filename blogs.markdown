---
layout: default
title: Posts
---


<p>
  {% for post in site.categories.blog %} 
    <span>{{ post.date | date_to_string }}</span> » <a href="/ontoads{{ post.url }}">{{ post.title }}</a><br>
  {% endfor %}
</p>
	