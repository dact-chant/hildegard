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
[Back to Literature]({{ site.baseurl }}/#literature)
<figure>
<img src = "{{site.baseurl}}/public/images/relief-lower-res.jpg"
alt = "A relief depicting Hildegard's profession">
<figcaption> A relief depicting Hildegard's profession, <br>a copy of the relief in the Binger Rochuskapelle by Jakob Busch 1898 </figcaption>
</figure>


{% assign items = site.historical-biographical | sort: 'number' %}
{% include section.html %}
