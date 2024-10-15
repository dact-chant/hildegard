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

<figure>
  <img src = "{{site.baseurl}}/public/images/Physicas-lower-res.jpg"
  alt="A print copy of Hildegard's Physicas">
  <figcaption> A print copy of Physicas (Strasbourg, 1803) at the Hildegard Museum in Bingen</figcaption>
</figure>

<!--
![old book place holder]({{ site.baseurl }}/public/images/apotheke.png) -->

{% assign items = site.medical | sort: 'number' %}
{% include section.html %}
