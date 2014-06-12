---
layout: page
title: Taranis Model Icons 
header: Taranis Model Icons
group:
---
{% include JB/setup %}
These model icons are checked by the OpenTX team and work well in the Taranis. Click to download those that you need and place them in a folder called "BMP" on your Taranis SD-card.

<ul>
{% for pic in site.data.icons-taranis %}
<a href="assets/images/icons-taranis/{{ pic.name }}" download="{{ pic.name }}" title="{{ pic.name }}">
   <img src="assets/images/icons-taranis/{{ pic.name }}" alt="{{ pic.name }}" style="border:1px solid black" />
</a> 
{% endfor %}
</ul>

