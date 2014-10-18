---
layout: page
title: Downloads
header: Downloads
group: navigation
---
{% include JB/setup %}

## For Taranis users
Please note that your radio has been delivered with a firmware that is customised and exclusive to FrSky, and is not part of the OpenTX team's offerings and development cycle. It is supposed to be used on its own, exclusively on the radio (no companion), and is supported directly by FrSky which means that should something not work or any feature request should be expressed directly to them. 
It is stable and suitable for most usage cases, and is the preferred version that most Taranis owners should likely be using. 
Switching to the OpenTX team's releases should be considered an "advanced" usage scenario that will require some computer knowledge, a bunch of reading to find out about the differences and may cause headaches if things don't go as expected. Be sure to read the paragraph below about how OpenTX versioning works.
The "original" Taranis comes with a version derived from OpenTX r2940, while the Taranis Plus comes with a version derived from OpenTX 2.0. If you want to switch your firmware to OpenTX and keep the known behavior you should stick to those major versions. Besides, the Taranis Plus will not work with OpenTX versions older than 2.0.10.

## About OpenTX versions
OpenTX versions are delivered as sets of major and minor releases. Major releases represent big steps with lots of feature changes and new functionality, which require changes in the way model data is stored and thus breaks compatibility with the previous one. Minor releases within a major one will fix bugs, correct functionality that needs changes, add new functionality that doesn't require breaking compatibility, or remove features that are deemed useless. 

As we are dependent on user feedback, a major release will start as "unstable" and will go through several rounds of refinement based on the gathered user experiences, which can initially cause radical changes in the way a feature operates between minor versions. Once things have settled and we have decent documentation available that major version will become "stable" i.e. its features will be frozen, and from that moment on any new minor versions would only be released to fix bugs that may be discovered. 

We recommend "normal users" not to jump on a new major revision straight away as following the minor revisions of an unstable branch requires careful attention to the changelog to find out about things that may have changed and could potentially break existing setups, and documentation is usually not ready yet. They should thus stick with "stable" versions. Advanced users who want to be on the bleeding edge, want to provide feedback and/or suggest modifications, can find their way without documentation and can follow the evolution closely are welcome to do so during the unstable period, of course at their own risk. 

Currently, the major versions of OpenTX are:
<ul>
<li>companion9x v1.52 - OpenTX firmware r2940 (stable)</li>
<li>OpenTX 2.0 (public, unstable)</li>
<li>OpenTX 2.1 (early development, developers only)</li>
</ul>

Major releases are independent, so companion9x 1.52 will download firmware up to r2940, OpenTX companion 2.0.x will download firmware 2.0.x, OpenTX companion 2.1.x will download firmware 2.1.x etc. Updates between major versions are manual, you need to download the required companion yourself, no updates will be automatically offered. When upgrading from one major version to the next it is recommended to backup both your current firmware and settings, and to thoroughly check all of your models' functions still operate correctly after the built-in upgrade procedure has completed. Downgrading models and settings is not possible, so should you want to switch back to an older major version you will need to either reload your backup or start from scratch again.
 
You can check the release history of OpenTX [on this page](https://github.com/opentx/opentx/releases)
 
## OpenTX Companion downloads

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

## OpenTX firmware downloads

Firmware downloads are exclusively available from within OpenTX companion's "Download" dialog. OpenTX Companion needs to be configured for the proper radio type and with the firmware options you choose, so that a customised firmware file with these options can prepared for you by our build server and downloaded to your PC. OpenTX Companion is then used to load the firmware to your radio.  

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
 
Before using Lua you should read the [Lua Instructions](lua-instructions.html) 

<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.Lua %}
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

For users wanting to upgrade a Taranis from a pre-2.0 version (either OpenTX or the FrSky firmware) who can't get the DFU driver installed with Zadig but have a working "DfuSe Demonstration" flashing setup (as per FrSky instructions), a copy of OpenTX 2.0.5 packaged in a .dfu file is available [here](http://downloads-20.open-tx.org/companion/opentx-taranis-en-2.0.5.dfu). Flash this using the FrSky method, then upgrade to the latest available version using the bootloader.
