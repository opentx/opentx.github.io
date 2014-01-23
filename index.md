---
layout: page
title: Welcome to OpenTX
tagline: Improving yourTx
---
{% include JB/setup %}

## This is the home of OpenTX  
The OpenTX team is currently hard at work preparing the next major release of OpenTX firmware and OpenTX Companion.  
Both will be announced here when they are finished.  
In the mean time the old home page is available and functional. We intend to keep it that way until we are done with the move. 

## ![OpenTX Logo](/assets/images/opentx-logo.png) Radio Firmware
The OpenTX team develops software for a range of different RC radio transmitters. This kind of software is often referred to as Firmware.
The transmitter firmware differs depending on which radio it is running in. The firmware can be configured in many ways. Regardless of radio and configuration, the firmware is always called ***OpenTX***.  
Read more about [which radios are supported](radios.html).  


## ![OpenTX Logo](/assets/images/opentx-companion-logo.png)
The team also develops transmitter support software that runs on a computer. This software be used for many different tasks like downloading firmware, transfer firmware  to your radio or backing up your model configurations.  
The supporting software is called ***OpenTX Companion*** and is based on the popular companion9x.  
OpenTX Companion is available for Windows, Apple OSX and Linux.

## Installation
The first step to upgrade your radio with the latest OpenTX version is to install OpenTX Companion on your computer.  
Then you select the firmware configuration you want and let OpenTX Companion download and install it to your radio.  
You find the latest OpenTX Companion versions in [Downloads](downloads.html).
    
## [News](news.html)
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
