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

<figure>
  <img src = "{{ site.baseurl }}/public/images/scivias-angels-2-lower-res.jpg"
    alt = "Scivias Angel Chorus">
    <figcaption> Hierarchy of angels (Scivias I.6) from the Abtei St-Hildegard facsimile. </figcaption>
</figure>
<!-- ![old book place holder]({{ site.baseurl }}/public/images/old_book_placeholder.jpg) -->

{% assign items = site.monographical | sort: 'number' %}
{% include section.html %}
