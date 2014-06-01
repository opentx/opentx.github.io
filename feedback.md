---
layout: page
title: Feedback 
header: Feedback
group: navigation
---
{% include JB/setup %}
From time to time we receive words of appreciation. We would like to share some of these on this page.

<ul class="posts">
{% for post in site.tags.Feedback %}
  <div class="post_info">
    <li>
         <span>{{ post.date | date:"%Y-%m-%d " }}<b>{{ post.title }}</b> {{ post.content }}</span>
    </li>
    </div>
{% endfor %}
</ul>




