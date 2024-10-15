---
layout: default
title: Home
---

<figure style="width:50%;float:left;">
  <img src = "{{site.baseurl}}/public/images/Antonius_van_der_Linde,_1874.jpg"
  alt = "Photograph of Antonius van der Linde from 1874">
  <figcaption> Photograph of Antonius van der Linde (by Hanns Hanfstängl, 1874) </figcaption>
</figure>

In 1877 **Antonius van der Linde** (also, *von* der Linde), librarian and author, published a catalogue of manuscripts held at the then-named Königliche Landesbibliothek in Wiesbaden, the state library where he worked. The book describes 78 manuscripts owned by the library, most significantly two including works by Hildegard of Bingen (1098-1179), and another two of works by Elisabeth of Schönau (c.1129-1165). The most important manuscript still owned by that library (now called the Hochschul- und Landesbibliothek RheinMain) is the *Riesencodex* (Handschrift 2) containing most of the works, including the music, of Hildegard.

More than half of the book by van der Linde is devoted to a description of the Riesencodex, but it also includes a rather quirky 15-page, partially annotated bibliography of editions and translations of the works of Hildegard as well as secondary literature about her and about her output. Although other bibliographies have appeared since (listed below), the document itself acts as a compelling witness to the state of research on Hildegard before the 1879 publication of the monumental life and works of Hildegard by J. Ph. Schmelzeis, which was to become the standard reference for studies on Hildegard for many decades.

Since neither van der Linde's bibliography nor the items in it were widely available when I began putting together this database, the purpose of this website is to make the bibliography and its contents more accessible. If digitized copies of items have been found, URLs are provided; for physical copies, the names of libraries holding the item have been included (but this part of the site has not been updated for a number of years, so please check library catalogues yourself). Translations into English are provided for all of the entries and I've included a number of comments about the works or the authors, or about van der Linde's entries, or about pagination particularly when a digitized copy I've provided in a link differs in pagination from van der Linde's citation. I would be very pleased to receive further URLs to digital copies of items, as well as translations into other languages and comments and will add appropriate submissions (properly attributed) to the site. Corrections, of course, are always welcome as well.

**The bibliography is divided into five sections**. Click on the links below to take you to each of these sections in the database.


<a name=literature></a>Litteratur [Literature]:

{% assign sections = site.sections | sort: 'order' %}

<dl style="padding-left:40px">
{% for section in sections %}
  <dt style="float: left">{{ section.number }}.</dt>
  <dd><a href="{{ site.baseurl }}{{ section.url }}">{{ section.name }} [{{ section.translations|map: "english" }}]</a></dd>
{% endfor %}
</dl>


**A number of Hildegard bibliographies are available online or in libraries:**

**Linde, A[ntonius] v[an] d[er]**. 1877. *Die Handschriften der Königlichen Landesbibliothek in Wiesbaden*. Wiesbaden: Hofbuchhandlung von Edmund Rodrian.

**Roth, F. W[ilhelm] E[mil]**. 1886 and 1887. "Zur Bibliographie der hl. Hildegardis, Meisterin des Klosters Rupertsberg bei Bingen O.S.B." *Quartalblätter des historischen Vereins für das Grossherzogtum Hessen* (1886): 221-233 and (1887): 78-88.

**Lauter, Werner**. 1970. *Hildegard-Bibliographie: Wegweiser zur Hildegard-literatur*. Alzey: Verlag der Rheinhessischen Druckwerkstätte.

**Lauter, Werner**. 1984. *Hildegard-Bibliographie: Wegweiser zur Hildegard-literatur*. Vol. II: 1970-1982. Alzey: Verlag der Rheinhessischen Druckwerkstätte.

**Aris, Marc-Aeilko; Embach, Michael; Lauter, Werner; Müller, Irmgard; Staab, Franz; Steinle, Scholastica OSB**. 1998. Hildegard von Bingen. *Internationale wissenschaftliche Bibliographie unter Verwendung der Hildegard-Bibliographie von Werner Lauter*. Quellen und Abhandlungen zur mittelrheinischen Kirchengeschichte, Bd. 84. Mainz: Selbstverlag der Gesellschaft für mittelrheinische Kirchengeschichte.
