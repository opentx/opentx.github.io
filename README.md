# Maintaining the openTX Web
The openTX web is published and maintained using Jekyll-Bootstrap.
Maintaining it is done primarily be editing markdown wiki pages and issuing Bootstrap commands. 

## What is Jekyll-Bootstrap?
Jekyll is the default page parsing and serving engine of Github. Files checked into the opentx.github.io git repository are checked out by Jekyll and parsed into _static_ web pages. These are then served as part of the opentx web.
The advantage of using Jekyll is that some advanced features like comment fields can be maintained without the need of maintaining active web code or a database. The downside is that the format is somewhat limited.

Bootstrap is a layer on top of Jekyll which adds some maintainance features. The result of using Bootstrap is owever always Jekyll formatted pages.

Jekyll-Bootstrap was made for maintaining blogs, which is not really what the openTX website is. The result is that some of the Bootstrap theming mechanism has been bypassed. Do not switch Bootstrap theme! That would break the site.

## Fetch the site
In order to maintain the site, you need to clone the opentx.github.io repository.
Make the changes locally and commit and push them back when you are done.  
It is a good idea to install Jekyll-Bootstrap on your local machine, so that you can test the changes.

## Adding a Post
In order to keep the site feeling alive it is important to add information about changes to the site. This information may be regarding a new release, added documentation, site updates etc. The standard way to add information is to create a blog post.  
We have chosen to organize the posts by tagging them as either Documents, News or Releases.  
Documents and Releases post should contain a link to a document or release as well as some descriptive information .   
Create a post by issuing the following ruby command in the root directory of the site:
```text
rake post title="XXX" tags=[XXX]
```
This creates an empty blog post file with all the default formatting of the site in place. In addition to the title, the post is marked with a date.  
You will find your new post in the _posts subdirectory. It is possible to update the date. To change the title of the post you have to edit the title variable inside the document.   
I you do not like to use Ruby commands, you can insted copy end edit an existing post. Be very carefull about the so called YAML code at the strat of the post. It has to be correct for the Jekyll parser to work. To add a post it is enough to add a file in the _post directory, everything else is automatic.  
The post is in wiki markdown format.  
Edit the post file to add some content.  
Test your changes and commit+push the new files to the remote repository.  
The publication is now done automatically by github!  

### Make a OpenTX Companion Release Post
All binaries are hosted on googlecode, rather than on github. The reason is that googlecode has better online editing tools, which makes it easier for non-developers to contribute. You find the googlecode repository [here](https://code.google.com/p/opentx/downloads).  
Start by adding the file to the OpenTX googlecode repository.
Then add a post in the following format.
```text
rake post title="OpenTX Companion vX.X" tags=[Releases]
```
The post should contain information about what is new in the release and a link to the binary file.

### Make an OpenTX Release Post
OpenTX firmware is available thrugh OpenTX Companion and the binaries are typically not available for download. This means that the release post needs only to contain information about what is new in the release. 
```text
rake post title="OpenTX vX.X" tags=[Releases]
```
The post should contain information about what is new in the release.

### Add a Document Post
All binary documents are hosted on googlecode, rather than on github. The reason is that googlecode has better online editing tools, which makes it easier for non-developers to contribute. You find the googlecode repository [here](https://code.google.com/p/opentx/downloads).  
Start by adding the document to the OpenTX googlecode repository.  
Then add a post in the following format.
```text
rake post title="Document Title" tags=[Documents]
```
The post should contain relevant document information and a link to the document.

## Jekyll-Bootstrap Documentation and help.
For all JekyllBootstrap documentation please see: <http://jekyllbootstrap.com>  
The documentation website at <http://jekyllbootstrap.com> is maintained at https://github.com/plusjade/jekyllbootstrap.com  
Jekyll-Bootstrap License: [MIT](http://opensource.org/licenses/MIT) 
