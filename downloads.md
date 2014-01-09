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
<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.Releases %}
  <div class="post_info">
    <li>
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>

You can check the release history of Companion [on this page](https://github.com/opentx/opentx/wiki/Companion-Changelog)

## Other Downloads
<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.Downloads %}
  <div class="post_info">
    <li>
         {% include display_flags.html %}
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>

