---
layout: section
title: Monographical
order: 1
number: I
name: Monografisches
translations:
  - english: monographical
---

# {{ page.title }}
[Back to Literature]({{ site.baseurl }}/#literature)
![old book place holder]({{ site.baseurl }}/public/images/old_book_placeholder.jpg)

{% assign items = site.monographical | sort: 'number' %}
{% include section.html %}


