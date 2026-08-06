---
layout: home
title: "Derivation of Value"
subtitle: "A working program in mechanism design"
eyebrow: "An anthology in progress"
---

Each protocol stakes something. Bitcoin stakes energy; proof of stake systems substitute capital; proof of useful work proposes work whose product is itself valuable. This program asks the question hiding inside all of them: *what must be at stake for a ledger to mean what it says?*

The work below proposes that the next generation of consensus mechanisms will derive their staked quantity rather than borrow it — that the substrate of trust can be the structural agreement of many witnesses, the resistance of order to entropy, the dimensional integrity of value itself. The anthology takes up the derivations in turn. The worked example, *Proof of Coherence*, is in active development.

<!-- Generated from the _papers collection. To add a document, drop a file in
     _papers/ with the front matter below; set `hidden: true` to keep one off
     this list while still publishing its page.

     Documents are grouped by `label`, not by `order`. `order` remains the
     CHRONOLOGICAL record — the sequence in which things were written — and is
     used to sort within each track. It is deliberately not the reading order:
     several documents are mutually dependent (Volume V and Sign and Work;
     The Multiplicity Freedom and Sign and Work; Proof of Coherence and
     A Consistent Fiction), and no single linear sequence expresses that. -->

{% assign papers = site.papers | sort: "order" %}

<section class="track">
  <h2 class="track-heading">Start here</h2>
  <p class="track-note">There are two doors. For the argument, begin with <em>Volume I</em> below and read the anthology in order. For the mechanism, begin here — this is the front door to the whitepaper, and it assumes nothing.</p>
  <ul class="contents">
  {% for paper in papers %}{% unless paper.hidden %}{% if paper.label == "Companion" %}
    {% include entry.html paper=paper %}
  {% endif %}{% endunless %}{% endfor %}
  </ul>
</section>

<section class="track">
  <h2 class="track-heading">The anthology</h2>
  <p class="track-note">Five volumes, essayistic. Each names something to stake and then tests whether it survives being staked. Volume V deflates the four before it.</p>
  <ul class="contents">
  {% for paper in papers %}{% unless paper.hidden %}{% if paper.label contains "Volume" %}
    {% include entry.html paper=paper %}
  {% endif %}{% endunless %}{% endfor %}
  </ul>
</section>

<section class="track">
  <h2 class="track-heading">The framework</h2>
  <p class="track-note">The formal spine. Dense, and not the place to begin.</p>
  <ul class="contents">
  {% for paper in papers %}{% unless paper.hidden %}{% if paper.label == "Framework" or paper.label == "Whitepaper" %}
    {% include entry.html paper=paper %}
  {% endif %}{% endunless %}{% endfor %}
  </ul>
</section>

<section class="track">
  <h2 class="track-heading">The papers</h2>
  <p class="track-note">Technical papers, each closing an open problem named elsewhere in the corpus — or failing to, and saying so. Listed in the order they were written, which is not the order they depend on each other: <em>Sign and Work</em> is cited by more of the corpus than any other document and was written sixteenth.</p>
  <ul class="contents">
  {% for paper in papers %}{% unless paper.hidden %}{% if paper.label contains "Paper" and paper.label != "Whitepaper" %}
    {% include entry.html paper=paper %}
  {% endif %}{% endunless %}{% endfor %}
  </ul>
</section>
