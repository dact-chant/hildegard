---
layout: default
title: Search
---

<p id="search-results-header"></p>
<ul id="search-results-list"></ul>

<script>
{
let sections={
{% for document in site.documents -%}
{% if document.layout == "section" -%}
{% assign document_name=document.path|strip_html|strip_newlines|split : "/" | last -%}
{% assign document_name=document_name |split : "." | first -%}
"{{document_name}}":{ "number": {{document.number|strip_html|strip_newlines|jsonify}},"url":{{document.url|strip_html|strip_newlines|jsonify}} },
{% endif -%}
{% endfor -%}
};

let itemIndex={
{% assign maxComments=0 -%}
{% assign maxTranslations=0 -%}
{% for document in site.documents -%}
  {% if document.layout == "item" -%}
    {% assign section_name=document.path|strip_html|strip_newlines|split : "/" | first -%}
    {% assign section_name=section_name|slice:1,section_name.size -%}
    {% if document.comments.size > maxComments -%}
    {% assign maxComments=document.comments.size -%}
    {% endif -%}
    {% if document.translations.size > maxTranslations -%}
    {% assign maxTranslations=document.translations.size -%}
    {% endif -%}
    
    "{{ document.url |slugify }}":{
    "number": {{ document.number|strip_html|strip_newlines|jsonify }},
    "url":"{{site.baseurl}}{{ document.url}}",
    "section-key":{{ section_name|jsonify }},
    "content":{{ document.content | strip_html | strip_newlines | jsonify }}, 
    "comments":[
    {% for comment in document.comments -%}
    {"author":{{ comment.author|strip_html|strip_newlines|jsonify }},"date":"{{comment.date}}","text":{{ comment.comment|strip_html|strip_newlines|jsonify }} }
    {% unless forloop.last %},{% endunless -%}
    {% endfor -%}
    ],
    "translations":[
    {% for translation in document.translations -%}
    { "language" : {{ translation[0] |strip_html|strip_newlines|jsonify }}, "text":{{ translation[1]|strip_html|strip_newlines|jsonify }} }
    {% unless forloop.last -%},{% endunless -%}
    {% endfor -%}
    ]
    }
    {% unless forloop.last -%},{% endunless -%}
  {% endif -%}
{% endfor -%}
};

let maxComments={{maxComments}};
let maxTranslations={{maxTranslations}};

runSearch(itemIndex,sections,maxComments,maxTranslations);
}
</script>
