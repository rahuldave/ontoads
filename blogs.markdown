---
layout: default
title: Blogs
---

### Posts

<p>
  {% for post in site.categories.blogs %} 
    <span>{{ post.date | date_to_string }}</span> » <a href="{{ post.url }}">{{ post.title }}</a><br>
  {% endfor %}
</p>
	
<h4>World</h4>	