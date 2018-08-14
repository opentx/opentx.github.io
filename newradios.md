---
layout: page
title: OpenTX support for new radios
header: OpenTX support for new radios
group:
---
{% include JB/setup %}


## I want to make an OpenTX radio!

We hear you, given the growing popularity of OpenTX-based radios in the past few years we have been contacted by increasing numbers of manufacturers wanting to join the project and be part of the OpenTX ecosystem. Hopefully this page will clarify a bit what that means so that everyone can set proper expectations to proceed.  

### What is OpenTX?

OpenTX is a free and open-source software project that includes:  

* A piece of embedded firmware called OpenTX that is designed to serve as the operating system of a remote control system as is commonly used for hobby RC models and industrial applications, and supports a number of different hardware targets listed on the [Radios](radios.html) page
* A piece of multiplatform comupter software called OpenTX Companion that allows management of hardware devices running OpenTX firmware, e.g. more convenient settings editing on an often more comfortable interface, firmware download and transfer, upgrading and conversion of settings between different OpenTX devices and versions, fleet management and more
* The open-tx.org website
* Server infrastructure dedicated to distributing OpenTX Companion, and on-demand building/distributing of the different OpenTX firmware variants for all the different supported platforms and options
* Obviously - a loosely organised team of independent volunteer developers with varying degrees of knowledge of the different aspects of the project's code and of its management.

OpenTX is licensed under the GPL V2. The firmware is a fork and the evolution of the discontinued gruvin9x project, which itself was a fork of the er9x project. OpenTX Companion is a fork and the evolution of the discontinued companion9x project, which itself was a fork of the eePe project. er9x and eePe have been grouped into the active [mbtx](https://github.com/MikeBland/mbtx) project.

The main goal for OpenTX being forked from its parent projects was a desire to embrace next generation innovative platforms, and increase user-friendliness by maintaining an entire suite of tools together to avoid discrepancies and by providing a user experience that is as consistent as possible across all supported platforms, with differences constrained only by the hardware characteristics of said platforms. As a result, one of the main requirements when adding a new product to the ecosystem is that it is properly integrated into all of our tools.

### Why would I join and how?

Firstly you should know that by the very nature of OpenTX and its license you are free to use all of the code and tools provided in our [Github repository](https://github.com/opentx/opentx) under the terms of the [GPL V2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html) without any authorization or involvement from our team. We will not go into too many details, but here are the main points you need to be aware of should you decide to take the code and make your own version:

* You must distribute the source code of your distribution to anyone who requests it.
* You must differentiate your work from the original one (aka you may not use the OpenTX name, you must change it to your own) to make it clear that there is no influence from the OpenTX team on anything you chose to change on your version, yet must acknowledge the original project and authors (aka must state something like "based on the OpenTX project").

Should you rather desire to become an integral part of the OpenTX family the first step is obviously to contact the OpenTX team and state your inquiries and intentions with project details, the [chat](https://chat.open-tx.org) is a good point of entry where we can provide additional direct contact methods. We are used to dealing with confidential projects and maintaining separation between our different partners during development.

Obviously since you are here you understand that OpenTX is also a brand, and by joining the family you would benefit from the value of a platform well known for its reliability, flexibility, power and popularity gained over 6 years of voluntary work by numerous contributors that certainly can go a long way into reducing your workload to get a product on the market.

That added value does come with contstraints, notably the first requirement to join the family is to share the main values of the project, of which the most relevant is sharing. To benefit from the above you are required to give back something significant to the community and industry that made it possible for the project to reach this level.
In essence, what we are looking for in new cooperations is contributions to:

* Innovation
* Progress
* Diversity

We are for example not interested in copycats or lowballers who only hurt the industry and users by robbing innovators who do real efforts to provide value from the success they deserve. We reserve the right not to integrate a product in our systems or allow the use of the OpenTX name for a project if we do not consider it appropriate or if it is potentially damaging to our brand. 

Additional constraints that come with the OpenTX brand are:

* Although the project is licensed under the GPL V2 which excludes all kinds of responsibility regarding the proper operation of the provided tools or fitness for any purpose, safety of system operation is very highly considered and an important contributor to the value of the OpenTX brand, meaning that proper safety-oriented logic and coding as well as extensive testing is mandatory before a release is made
* As mentioned previously, proper integration within all the tools we provide in order to ensure a consistent user experience is required
* Both the above points mean that your product will be subject to our internal testing and release schedule. Initial general public availability must conincide with a release of ours, which itself is constrained by testing and validation on all the platforms we support. Exceptions can be made only in specific cases and a product launched with at minimum a release candidate status if we have been able to concentrate testing on your platform before others and reached a satisfactory level of confidence, at the sole discretion of the project's core members.

### I do fit in and want to join!

Awesome! At this point the most popular ways to go about actual integration are:

* You do all the work on your own with your own developers, and submit pull requests as per github workflow to the branch you will have been advised by the core team to target. We expect minimal work here, we will review your pull request and advise if changes are needed, which you can do, repeat until deemed satisfactory. With this workflow you are responsible for following activity on our repository and making sure support for your platform continues to work as we progress / providing pull requests if something breaks. If at the time of a release we test your platform and find issues it will be removed from the list of available platforms for that release. 
* You decide to support the project with a recurrent donation discussed with the core team to encourage continued support for your platform. In this scenario we will do our best in a voluntary and non-binding manner to carry over any changes we make to your platform with our usual quality control so that your product always has the latest functions available, subject to adequate hardware support of course.
* You request to hire one or more of our developers for specific tasks on a one-off basis. This is obviously subject to availability.
* A combination of the above, or anything else you might deem appropriate for your project can be discussed.

For all options we require hardware to be provided to us at no cost for either goods, shipping and eventual import taxes for testing and validation (usually 2-4 sets, must include the main product and every accessory that is to be available at that time). 

The timeframe required to add support for a new hardware platform is very variable depending on the characteristics of your hardware and collaboration method, but typically ranges between 4 and 15 months. If you are interested DO contact us as early as possible in your project with as many details as you can for an estimation.

As mentioned previously we are able and used to working in private during the development phase of a product and keeping concurrent developments separate / avoiding conflicts of interest as much as possible to ensure privacy of your unique features until product launch, but as you have certainly understood from the above per the license terms and for practical project management reasons close to the launch of your product all the work that has been done will be made public and available for everyone to use, including your competitors. This is likely what brought you here in the first place, so we believe you understand the value of that process for continued improvement in the industry.

If you have read until this point then it is likely we can work together, so don't hesitate to contact us :)