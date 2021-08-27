---
layout: section
title: Historical Biographical
order: 2
number: II
name: Historisch-biografische daten 
translations:
  - english: historical-biographical data
---

# {{ page.title }}
[Back to Literature]({{ site.baseurl }}#literature)
![old book place holder]({{ site.baseurl }}/public/images/old_book_placeholder.jpg)

{% assign items = site.historical-biographical | sort: 'number' %}
{% include section.html %}