---
layout: post
title: "WARNING - X10 ACCESS IXJT Upgrade Module"
description: ""
category: ""
tags: [News]
---
{% include JB/setup %}

FrSky have recently started shipping an upgrade module to give ACCESS capabilities to existing, non-EXPRESS X10/X10S radios (which works on X12 too). This module implements an authentication check that has the purpose of allowing the module to only work with genuine FrSky radios and not with 3rd-party ones.  
OpenTX only got the FrSky-created and supplied code required to answer this authentication request merged in on the day people started receiving the first modules, that is 2019-10-24, which means **only OpenTX 2.3.2 nightly builds starting 2019-10-25 will be able to properly talk to these modules and make them operate correctly.**  

It was expected that the modules would simply not work without valid authentication, but the first owners have reported that they allow binding, give control, but then periodically cause intentional erratic, uncommanded channel movements instead.  

This means that **anyone turning the upgrade module on with an OpenTX build older than mentioned above and binding it to a live model risks having broken servos/linkages, or worse erratic electric motor starts.**

We thus warn everyone to **not use the module on anything other than a harmless bench setup until they have been able to upgrade OpenTX to a version with proper support for the module.**

We also recommend them to contact their FrSky dealer or support contact to enquire about the reason for such dangerous behavior.
