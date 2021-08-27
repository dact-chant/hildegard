---
layout: section
title: Relics
order: 3
number: III
name: Reliquien
translations:
  - english: relics
---

# {{ page.title }}
[Back to Literature]({{ site.baseurl }}#literature)
![old book place holder]({{ site.baseurl }}/public/images/old_book_placeholder.jpg)

{% assign items = site.relics | sort: 'number' %}
{% include section.html %}