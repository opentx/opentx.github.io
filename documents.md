---
layout: page
title: Documents
header: Documents
group: navigation
---
{% include JB/setup %}

{% for tag in site.tags %} 
{% if tag[0] == "Documents" %}
  <ul>
    {% assign pages_list = tag[1] %}  
    {% include JB/pages_list %}
  </ul>
{% endif %}
{% endfor %}
