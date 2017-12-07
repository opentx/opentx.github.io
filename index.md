---
layout: page
title: Welcome to OpenTX
tagline: Improving yourTx
redirect_from: "open-tx.org"
---
{% include JB/setup %}

## ![OpenTX Logo](/assets/images/opentx-firmware-logo.png)
OpenTX is open source firmware for RC radio transmitters. The firmware is highly configurable and brings much more features than found in traditional radios. The daily feedback from the thousands of users ensures the continued stability and quality of the firmware.  
Read more about [which radios are supported](radios.html).  

## ![OpenTX Companion Logo](/assets/images/opentx-companion-logo.png)
The team also develops the OpenTX Companion transmitter support software. OpenTX Companion is used for many different tasks like loading OpenTX firmware to the radio, backing up model settings, editing settings and running radio simulators.   
OpenTX Companion is available for Windows, Apple OSX and Linux.

## ![OpenTX Sound Logo](/assets/images/opentx-sound-logo.png)
One of the main features of OpenTX is its customizable sounds and announcements. Announcements are stored on an optional SD Card in sound packs. Sound packs may be downloaded using OpenTX Companion. 

## Installation
The first step to upgrade your radio with the latest OpenTX version is to install OpenTX Companion on your computer.  
Then you select the firmware configuration you want and let OpenTX Companion download and install it to your radio.  
You find the latest OpenTX Companion versions in [Downloads](downloads.html).
    
## News
<ul class="posts">
{% for post in site.tags.News %}
  <div class="post_info">
    <li>
         {% include display_flags.html %}
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>
