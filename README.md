# Maintaining the openTX Web
The OpenTX web is hosted on github. The site is built using Jekyll, which is the default page parsing and serving engine of Github. Maintaining it is done primarily be editing html and markdown wiki pages. 

## Helping Maintain The Site
First time contributors should first introduce themselves on [![Join the chat at https://chat.open-tx.org](https://camo.githubusercontent.com/3d659054abd6ce21c0e47cf3b83a51bda69ca282/68747470733a2f2f64656d6f2e726f636b65742e636861742f696d616765732f6a6f696e2d636861742e737667)](https://opentx.rocket.chat)

## Create A Site Fork (You are not a collaborator)
To make contributions and help maintain the site you will need a GitHub account.
* Login to GitHub
* Goto https://github.com/opentx/opentx.github.io
* Click on "Fork" located top right (Video https://www.youtube.com/watch?v=yr6IzOGoMsQ&feature=youtu.be)
* Make and preview your changes (read documentation below)
* Make a "Pull Request"
* Over time keep your fork in sync with the master (Video https://www.youtube.com/watch?v=C5WxrnRVmuY)

## Fetch the site (Your are a collaborator)
In order to maintain the site, you need to clone the opentx.github.io repository. Make the changes locally and commit and push them back when you are done. It is a good idea to install Jekyll-Bootstrap on your local machine, so that you can test the changes.

## Site Structure
The site consists of pages in the root folder and posts in the _posts folder. The rest of the site is include files and will only need to be changed to alter the appearance and function, not to add content.  
Pages on a the top level that has a YAML heading and a group property looking like this: "group: Navigation" are automatically included in the menu of the site.
The normal way of adding content is to add new posts, rather than editing existing pages.

## Adding a Post
* Select an old post in the _posts folder and make a copy of it.
* Change the file name. Please note that the date part MUST have the same format as used by the other posts. The text after the date string has no other meaning than to make the post easy to identify while editing.
* Edit the so yalled YAML part of the post. This is the first few lines which will look something like this.
```text
---  
layout: post  
title: "Modele Magazine article about Open9x (April 2013)"  
description: ""  
category: ""  
tags: [Documents, French, News]  
---  
```
* Edit the title and tags fields. The title is displayed on all site pages as the name of the post.  
The tags are used to determine which pages that shows the post. Any number of tags can be used.  
Current content tags are: **Documents, Downloads, Releases21, Releases20, Releases1x, News**. Current language tags are: **Italian, French, Polish, Czech, German, English, Swedish**  
* Edit the end of the post file to add some content.  
* Test your changes and commit+push the new files to the remote repository.  
* The publication is now done automatically by github!  

## Adding model images or start screens
Jekyll builds static web pages, which means that there is no way to add content on a page based on checked in files. The model icon page and the start screen pages basically consist of lists of image files. Adding static links to each individual image would be error prone and boring. A python script has been developed to handle this task.
To update the model icon page or the start screen pages the python script is started. The script browses through the image directories and builds three index files. The index files are then checked into github along with any new or modified image files. Do like this:
* Add the new image files to the proper directories (assets/images/...)
* Update image file names (if needed)
* Run the script from the root directory of the page. This is where all your .md pages are: "python update-indexes.py"
* Commit and push the changes to the github repository

## Jekyll-Bootstrap Documentation and help.
For all JekyllBootstrap documentation please see: <http://jekyllbootstrap.com>  
The documentation website at <http://jekyllbootstrap.com> is maintained at https://github.com/plusjade/jekyllbootstrap.com  
Jekyll-Bootstrap License: [MIT](http://opensource.org/licenses/MIT) 
