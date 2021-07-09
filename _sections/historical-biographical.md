---
layout: default
title: Home
order: 2
number: II
name: Historisch-biografische daten 
translations:
  - english: historical-biographical data
---

{% assign items = site.historical-biographical | sort: 'number' %}
{% include section.html %}