---
layout: page
title: Downloads
header: Downloads
group: navigation
---
{% include JB/setup %}

## OpenTX Firmware - Current: 2.0.2
You use OpenTX Companion to select exactly which options you want to have enabled in your radio. A firmware file with these options is prepared for you by our build server and downloaded to your PC. OpenTX Companion is then used to load the firmware to your radio.  
  
You can check the release history of OpenTX firmware [on this page](https://github.com/opentx/opentx/releases)

## OpenTX Companion - Current: 2.0.2
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


## OpenTX Sound
<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.Sound %}
  <div class="post_info">
    <li>
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>


## OpenTX Images
<ul>
<li><a href="icons-taranis.html">Taranis Model Icons</a></li>
<li><a href="screens-taranis.html">Taranis Start Screens</a></li>
<li><a href="screens-9x.html">9X/9XR Start Screens</a></li>
</ul>


## OpenTX Lua Scripts 
<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.LUA %}
  <div class="post_info">
    <li>
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>


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

