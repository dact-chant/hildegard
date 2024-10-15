---
layout: section
title: General
order: 4
number: IV
name: Allgemeines, besonders die verschiedene beurteilung der heil. Hildegard
translations:
  - english: general, particularly the various assessment[s] of the holy Hildegard
---

# {{ page.title }}
[Back to Literature]({{ site.baseurl }}/#literature)

<figure>
<img src = "{{site.baseurl}}/public/images/hildegardis-lower-res.jpg"
alt = "Image of Hildegard from a fifteenth century book">
<figcaption> Image of Hildegard from Hartmann Schedel, Liber chronicarum ab O.C. (Nuremberg: Koberger, 1493) fol. 201v</figcaption>

</figure>

{% assign items = site.general | sort: 'number' %}
{% include section.html %}
