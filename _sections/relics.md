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
[Back to Literature]({{ site.baseurl }}/#literature)

<figure>
  <img src = "{{site.baseurl}}/public/images/hildegard-relics.jpeg"
    alt = "Image of Hildegard shrine at the Katholische Pfarrkirche St. Hildegard, Rüdesheim am Rhein">
    <figcaption> Hildegard shrine at the Katholische Pfarrkirche St. Hildegard, Eibingen.</figcaption>
</figure>


<!--
 ![old book place holder]({{ site.baseurl }}/public/images/old_book_placeholder.jpg) -->

{% assign items = site.relics | sort: 'number' %}
{% include section.html %}
