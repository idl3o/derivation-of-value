---
layout: home
title: "Derivation of Value"
subtitle: "A working program in mechanism design"
eyebrow: "An anthology in progress"
---

Each protocol stakes something. Bitcoin stakes energy; proof of stake systems substitute capital; proof of useful work proposes work whose product is itself valuable. This program asks the question hiding inside all of them: *what must be at stake for a ledger to mean what it says?*

The work below proposes that the next generation of consensus mechanisms will derive their staked quantity rather than borrow it — that the substrate of trust can be the structural agreement of many witnesses, the resistance of order to entropy, the dimensional integrity of value itself. The anthology takes up the derivations in turn. The worked example, *Proof of Coherence*, is in active development.

<!-- Generated from the _papers collection. To add a paper, drop a file in
     _papers/ with the front matter fields below; set `hidden: true` to keep
     one off this list while still publishing its page. -->
<ul class="contents">
  {% assign papers = site.papers | sort: "order" %}
  {% for paper in papers %}{% unless paper.hidden %}
  <li>
    <span class="item-label">{{ paper.label }}</span>
    <a class="item-title" href="{{ paper.url | relative_url }}">{{ paper.short_title | default: paper.title }}</a>
    <div class="item-meta">{{ paper.blurb }}</div>
    <span class="item-status">{{ paper.status }}</span>
  </li>
  {% endunless %}{% endfor %}
</ul>
