---
layout: page
title: Taranis Start Screens 
header: Taranis Start Screens
group:
---
{% include JB/setup %}
These start screens are checked by the OpenTX team and work well in the Taranis. Click to download those that you want. Then use Companion to load the image to your radio along with the firmware.

<ul>
{% directory path: assets/images/screens-taranis %}  
<a href="{{ file.url }}" download="{{ file.name }}" title="{{ file.name }}"><img src="{{ file.url }}" alt="{{ file.name }}" style="border:1px solid black" /></a> 
{% enddirectory %}
</ul>
