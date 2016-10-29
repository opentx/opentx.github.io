---
layout: post
title: "Important safety announcement about recent Turnigy 9X radios"
description: ""
category: ""
tags: [News]
---
{% include JB/setup %}

It has come to our attention that Turnigy 9X radios that have been sold by Hobbyking since some time in Summer 2016 have been found not to use a genuine Atmel ATmega64 or ATmega128 microcontroller like all previous 9X radios, but rather rely on an m128 clone identified as "Green ED040501-H16D".  
According to several reports from users it seems the clone is not a perfect copy and firmware written for the original Atmel chips does not run correctly on it, causing intermittent failure of switch inputs and random reboots among other issues.  
No documentation has been found for that particular chip, meaning that adding correct support for it is not possible at this time and it is unknown whether it will ever be. Documentation was found for clones of other Atmel microcontrollers made by the same manufacturer and showed significant differences with the relevant original part, so trying to guess is not a safe option.

It is thus strongly advised not to flash these radios with OpenTX or other open source firmware, especially as there is no known source for the original firmware these ship to restore them to factory condition.
