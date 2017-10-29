---
layout: page
title: 9x Start Screens 
header: 9x Start Screens
group:
---
{% include JB/setup %}
These start screens are checked by the OpenTX team and work well in 9x/9XR/9XR Pro & Taranis Q X7 series of radios.  Click to download those that you want. Then use Companion to load the image to your radio along with the firmware.

<ul>
{% for pic in site.data.screens-9x %}
<a href="assets/images/screens-9x/{{ pic.name }}" download="{{ pic.name }}" title="{{ pic.name }}">
   <img src="assets/images/screens-9x/{{ pic.name }}" alt="{{ pic.name }}" style="border:1px solid black" width="128" height="64" />
</a> 
{% endfor %}
</ul>
