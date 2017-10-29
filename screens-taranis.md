---
layout: page
title: Taranis Start Screens 
header: Taranis Start Screens
group:
---
{% include JB/setup %}
These start screens are checked by the OpenTX team and work well in the Taranis X9D, X9D+ and X9E. Click to download those that you want. Then use Companion to load the image to your radio along with the firmware.

<ul>
{% for pic in site.data.screens-taranis %}
<a href="assets/images/screens-taranis/{{ pic.name }}" download="{{ pic.name }}" title="{{ pic.name }}">
   <img src="assets/images/screens-taranis/{{ pic.name }}" alt="{{ pic.name }}" style="border:1px solid black" width="212" height="64" />
</a> 
{% endfor %}
</ul>
 
