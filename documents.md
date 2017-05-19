---
layout: page
title: Documents
header: Documents
group: navigation
---
{% include JB/setup %}




<ul class="posts">


<!-- Insert Fixed List Items Here -->
<li>
<img src="assets/images/flags/gb.png"> [OpenTX 2.2 manual](https://opentx.gitbooks.io/manual-for-opentx-2-2/)
</li>
{% for post in site.tags.Documents %}
  <div class="post_info">
    <li>
         {% include display_flags.html %}
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
{% endfor %}
</ul>
