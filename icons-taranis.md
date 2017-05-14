---
layout: page
title: Taranis Model Icons 
header: Taranis Model Icons
group:
---
{% include JB/setup %}
These model icons are checked by the OpenTX team and work well in the Taranis. Click to download those that you need and place them on your Taranis SD-card in one of the following folders:

- "BMP" OpenTX versions prior to 2.2
- "IMAGES" OpenTX version 2.2

<ul>
{% for item in site.data.icons-taranis %}
  {% if item.type == 'title' %}
<br><br><strong>{{item.name}}</strong><br>
  {% else %}
  <a href="{{ item.url }}" download="{{ item.name }}" title="{{ item.name }}">
     <img src="{{ item.url }}" alt="{{ item.name }}" style="border:1px solid black" width="64" height="32" />
  </a>
  {% endif %} 
{% endfor %}
</ul>

