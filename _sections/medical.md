---
layout: section
title: Medical
order: 5
number: V
name: Medicinisches
translations:
  - english: medical
---

# {{ page.title }}
[Back to Literature]({{ site.baseurl }}/#literature)
![old book place holder]({{ site.baseurl }}/public/images/apotheke.png)

{% assign items = site.medical | sort: 'number' %}
{% include section.html %}
