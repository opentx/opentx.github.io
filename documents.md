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
         {% if post.tags contains 'Italian' %} <img src="assets/images/flags/it.png"> {% endif %}         
         {% if post.tags contains 'French' %}  <img src="assets/images/flags/fr.png"> {% endif %}
         {% if post.tags contains 'German' %}  <img src="assets/images/flags/fr.png"> {% endif %}
         {% if post.tags contains 'English' %} <img src="assets/images/flags/gb.png"> {% endif %}
         {% if post.tags contains 'Czech' %}   <img src="assets/images/flags/cz.png"> {% endif %}
         {% if post.tags contains 'Polish' %}  <img src="assets/images/flags/pl.png"> {% endif %}

         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
  {% endfor %}
</ul>
