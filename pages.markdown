---
layout: default
title: Pages
---

### {{ page.title }}

<p>
  {% for post in site.categories.article %} 
    <span>{{ post.date | date_to_string }}</span> » <a href="{{ post.url }}">{{ post.title }}</a><br>
  {% endfor %}
</p>
	