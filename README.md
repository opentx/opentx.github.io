# Maintaining the openTX Web
The OpenTX web is hosted on github. The site is built using Jekyll, which is the default page parsing and serving engine of Github.
Maintaining it is done primarily be editing html and markdown wiki pages. 

## Fetch the site
In order to maintain the site, you need to clone the opentx.github.io repository.
Make the changes locally and commit and push them back when you are done.  
It is a good idea to install Jekyll-Bootstrap on your local machine, so that you can test the changes.

## Site Structure
The site consists of pages in the root folder and posts in the _posts folder. The rest of the site is include files and will only need to be changed to alter the appearance and function, not to add content.  
All pages with a YAML heading are automatically included in the menu of the site.
The normal way of adding content is to add new posts, rather than editing existing pages.

## Adding a Post
* Select an old post in the _posts folder and make a copy of it.
* Change the file name. Please note that the date part MUST have the same format as used by the other posts. The text after the date string has no other meaning than to make the post easy to identify while editing.
* Edit the so yalled YAML part of the post. This is the first few lines which will look something like this:  
---  
layout: post  
title: "Modele Magazine article about Open9x (April 2013)"  
description: ""  
category: ""  
tags: [Documents, French, News]  
---  
Change the title and tags fields. The title is displayed on the site as the name of the post. The tags are used to determine which pages that shows the post. Any number of tags can be used.  
Current content tags are: Documents, Downloads, Releases, News  
Current language tags are: Italian, French, Polish, Czech, German, English, Swedish  

* Edit the end of the post file to add some content.  
* Test your changes and commit+push the new files to the remote repository.  
* The publication is now done automatically by github!  

## Jekyll-Bootstrap Documentation and help.
For all JekyllBootstrap documentation please see: <http://jekyllbootstrap.com>  
The documentation website at <http://jekyllbootstrap.com> is maintained at https://github.com/plusjade/jekyllbootstrap.com  
Jekyll-Bootstrap License: [MIT](http://opensource.org/licenses/MIT) 
