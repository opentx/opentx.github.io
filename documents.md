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
  <img src="assets/images/flags/gb.png"> <a href="https://opentx.gitbooks.io/manual-for-opentx-2-2/">OpenTX 2.2 manual</a>
  <span>(2017-05-18)</span>
</li>
{% for post in site.tags.Documents %}
    <li>
       {% include display_flags.html %}
       <a href="{{ post.url }}">{{ post.title }}</a>
       <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
{% endfor %}
</ul>
