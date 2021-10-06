---
layout: post
title: "Windows Companion downloads issue"
description: ""
category: ""
tags: [News]
---
{% include JB/setup %}

Since Sept 30th, 2021 OpenTX Companion for Windows is not able to check for updates / download them or download firmware anymore.  

This is caused by the combination of [the expiration of a Let's Encrypt root certificate](https://letsencrypt.org/docs/dst-root-ca-x3-expiration-september-2021/) and the fact that the OpenSSL library that has been bundled with the Windows version of Companion is too old to support the transition method that Let's Encrypt has used. Companion thus can't reach the download server anymore.  
We have rebuilt Companion 2.3.14 with a newer version of the libraries to fix the problem. Unfortunately since this breaks the auto-update mechanism it's not possible to distribute that fix automatically, so you will have to download and install the fixed installer manually below. Sorry for the inconvenience.  
If you see no improvement check in Companion Help -> About that your version is from Oct. 1st. If not your browser may have served you the old version, clear your browser cache and redownload/reinstall.  
If that still does not work your system might be missing the new root certificate, which you can check [here](https://valid-isrgrootx1.letsencrypt.org/), this will also install it automatically if needed if your system is supported. For out of support OSes like Windows 7 you need to do a manual install, [documentation here](https://docs.certifytheweb.com/docs/kb/kb-202109-letsencrypt/#windows-pcs).  
If you wish to continue using older Companion versions you will have to download the new SSL libraries linked below and drop them in the install folder, replacing the older files.  

### Download links:  

[OpenTX Companion 2.3.14  - Windows Installer](https://downloads.open-tx.org/2.3/release/companion/windows/companion-windows-2.3.14.exe)  
[Replacement ibraries for older companion versions](https://downloads.open-tx.org/tools/openssl-1.0.2u.zip)  

  
![](/assets/images/companion_oct1.png)
  


**Support OpenTX**

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=DJ9MASSKVW8WN" rel="nofollow"><img src="https://camo.githubusercontent.com/11b2f47d7b4af17ef3a803f57c37de3ac82ac039/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f70617970616c2d646f6e6174652d79656c6c6f772e737667" alt="Donate using Paypal" data-canonical-src="https://img.shields.io/badge/paypal-donate-yellow.svg" style="max-width:100%;"></a>

A donation can go a long way to help us move forward !  

If you need help please refer to the great communities e.g. [openrcforums](http://openrcforums.com/forum/viewforum.php?f=45) or [RCGroups](https://www.rcgroups.com/forums/showthread.php?3395177-Official-OpenTX-version-2-3-Discussion-Thread). You can pop in our [chat room](https://discord.gg/CZCwVx2) where other users and/or devs may be available.
