---
layout: page
title: Documents
header: Documents
group: navigation
---
{% include JB/setup %}


<ul class="posts">
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
