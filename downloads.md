---
layout: page
title: Downloads
header: Downloads
group: navigation
---
{% include JB/setup %}

## OpenTX downloads

### OpenTX 2.2 branch

Latest OpenTX major version with added support for the FrSky Horus and Taranis Q X7 radios. Please read [this page](http://www.open-tx.org/2017/05/30/opentx-2.2.0) for more details about other changes. As usual with each major release new sound packs are needed, information is on the page.

<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.Releases22 %}
  <div class="post_info">
    <li>
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>

### Nightly builds

The nightly builds are automatic builds that are build every day. As
during development, critical bugs might be introduced, these versions
**should not be used for flying**. Additionally a backup of EEPROM
should be done before flashing these firmware. The nightly builds are
only intented to verify if bugfixes/new features work as expected. We
provide no changelogs for these builds. To get a rough idea about the
changes you can look at the
[git commit log](https://github.com/opentx/opentx/commits/2.2).

[macOS nightly builds](http://downloads.open-tx.org/2.2/nightlies/companion/macosx/),
[Windows nightly builds](http://downloads.open-tx.org/2.2/nightlies/companion/windows/)
and
[Linux nightly builds](http://downloads.open-tx.org/2.2/nightlies/companion/linux/)

[SD Card contents for nightly builds](http://downloads.open-tx.org/2.2/nightlies/sdcard/)



### OpenTX 2.1 branch

Previous major version, now stable and still supported for normal use, but no new features or bugfixes will be implemented. 2.1 introduced completely new telemetry handling compared to 2.0, and also requires a different sound pack (see below). The original upgrade notes from 2.0 to 2.1 can be found [here](http://www.openrcforums.com/forum/viewtopic.php?f=45&t=7239).

This branch is the first to support the FrSky Taranis X9E (tray version).

<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.Releases21 %}
  <div class="post_info">
    <li>
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>


### OpenTX 2.0 branch

Deprecated, no more support will be given but firmware downloads are still available for the time being. 2.0 introduced the Virtual Inputs system.
This branch is the first to support the FrSky Taranis X9D+ and the Turnigy 9XR-Pro.

<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.Releases20 %}
  <div class="post_info">
    <li>
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>

### OpenTX 1.x branch

This branch is the first to support the original FrSky Taranis X9D, and is now deprecated. Firmware downloads are not possible anymore, the below companion is only provided for reference.

<ul class="posts">

<!-- Insert Fixed List Items Here -->

{% for post in site.tags.Releases1x %}
  <div class="post_info">
    <li>
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>

Firmware downloads are exclusively available from within OpenTX Companion's "Download" dialog. OpenTX Companion needs to be configured for the proper radio type and with the firmware options you choose, so that a customised firmware file with these options can be prepared for you by our build server and downloaded to your PC. OpenTX Companion is then used to load the firmware to your radio.  
**PLEASE NOTE** that the firmware you run on the radio and companion you use on the PC to edit settings must be of the same branch!

### Sound packs

Sound packs can be downloaded either through companion (the Download dialog will point you to the correct directory for the selected radio type), or from the links below:

[Sound packs for OpenTX 2.0](http://voices-20.open-tx.org)  
[Sound packs for OpenTX 2.1](http://voices-21.open-tx.org)  
[SD card contents for OpenTX 2.2, with sound packs](https://downloads.open-tx.org/2.2/sdcard/)


## About OpenTX versions
OpenTX versions are delivered as sets of major and minor releases. Major releases represent big steps with lots of feature changes and new functionality, which require changes in the way model data is stored and thus breaks compatibility with the previous one. Minor releases within a major one will fix bugs, correct functionality that needs changes, add new functionality that doesn't require breaking compatibility, or remove features that are deemed useless. 

As we are dependent on user feedback, a major release will start as "unstable" and will go through several rounds of refinement based on the gathered user experiences, which can initially cause radical changes in the way a feature operates between minor versions. Once things have settled and we have decent documentation available that major version will become "stable" i.e. its features will be frozen, and from that moment on any new minor versions would only be released to fix bugs that may be discovered. 

We recommend "normal users" not to jump on a new major revision straight away as following the minor revisions of an unstable branch requires careful attention to the changelog to find out about things that may have changed and could potentially break existing setups, and documentation is usually not ready yet. They should thus stick with "stable" versions. Advanced users who want to be on the bleeding edge, want to provide feedback and/or suggest modifications, can find their way without documentation and can follow the evolution closely are welcome to do so during the unstable period, of course at their own risk. 

Currently, the supported major versions of OpenTX are:
<ul>
<li>OpenTX 2.1</li>
<li>OpenTX 2.2</li>
</ul>

Major releases are independent, OpenTX companion 2.0.x will download firmware 2.0.x, OpenTX companion 2.1.x will download firmware 2.1.x etc. Updates between major versions are manual, you need to download the required companion yourself, no updates will be automatically offered. When upgrading from one major version to the next it is recommended to backup both your current firmware and settings, and to thoroughly check all of your models' functions still operate correctly after the built-in upgrade procedure has completed. Downgrading models and settings is not possible, so should you want to switch back to an older major version you will need to either reload your backup or start from scratch again.
 
You can check the release history of OpenTX [on this page](https://github.com/opentx/opentx/releases).


## For Taranis users
Please note that your radio has been delivered with a firmware that is customised and exclusive to FrSky, and is not part of the OpenTX team's offerings and development cycle. It is supposed to be used on its own, exclusively on the radio (no companion), and is supported directly by FrSky which means that should something not work or any feature request should be expressed directly to them. It is stable and suitable for most usage cases, and is the preferred version that most Taranis owners should likely be using. 

Switching to the OpenTX team's releases and using tools like companion should be considered an "advanced" usage scenario that will require some computer knowledge, a bunch of reading to find out about the differences and may cause headaches if things don't go as expected. Be sure to read the paragraph below about how OpenTX versioning works, and to always use matching combinations of companion and firmware.
<ul>
<li>The Taranis X9D comes with a version derived from OpenTX 1.0</li>
<li>Taranis X9D+ comes with a version derived from OpenTX 2.0</li>
<li>Taranis X9E comes with a version derived from OpenTX 2.1</li>
<li>Taranis Q X7 comes with a version derived from OpenTX 2.2</li>
</ul>
If you want to switch your firmware to OpenTX and keep the known behavior you should stick to those major versions.
<ul>
  <li>The Taranis Plus will not work with OpenTX versions older than 2.0.10</li>
  <li>Taranis X9E will not work with OpenTX versions older than 2.1.0. </li>
  <li>The FrSKY Horus X12S and Taranis Q X7 will not work with OpenTX versions older than 2.2.</li>
</ul>


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
<li><a href="icons-taranis.html">Taranis Model Icons (Not for X7)</a></li>
<li><a href="screens-taranis.html">Taranis Start Screens (Not for X7)</a></li>
<li><a href="screens-9x.html">128x64 LCD Start Screens (9X/9XR/AR9X and Taranis Q X7)</a></li>
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

For users wanting to upgrade a Taranis from a pre-2.0 version (either OpenTX or the FrSky firmware) who can't get the DFU driver installed with Zadig but have a working "DfuSe Demonstration" flashing setup (as per FrSky instructions), a copy of OpenTX 2.0.5 packaged in a .dfu file is available [here](http://downloads.open-tx.org/2.0/companion/opentx-taranis-en-2.0.5.dfu). Flash this using the FrSky method, then upgrade to the latest available version using the bootloader.


<b>Except for the FrSKY Horus X12S all FrSKY Transmitters purchased new do not require a seperate Zadig or DFU driver install.</b>
