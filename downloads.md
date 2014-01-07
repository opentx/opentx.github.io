---
layout: page
title: Downloads
header: Downloads
group: navigation
---
{% include JB/setup %}

## OpenTX Firmware
You use OpenTX Companion to select exactly which options you want to have enabled in your radio. A firmware file with these options is prepared for you by our build server and downloaded to your PC. OpenTX Companion is then used to load the firmware to your radio.  
  
You can check the release history of OpenTX firmware [on this page](https://github.com/opentx/opentx/releases)

## OpenTX Companion Releases
{% for tag in site.tags %} 
{% if tag[0] == "Releases" %}
  <ul>
    {% assign pages_list = tag[1] %}  
    {% include JB/pages_list %}
  </ul>
{% endif %}
{% endfor %}
You can check the release history of Companion [on this page](https://github.com/opentx/opentx/wiki/Companion-Changelog)

## Other Downloads
{% for tag in site.tags %} 
{% if tag[0] == "Downloads" %}
  <ul>
    {% assign pages_list = tag[1] %}  
    {% include JB/pages_list %}
  </ul>
{% endif %}
{% endfor %}

