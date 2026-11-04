---
title: READING GROUP
permalink: /reading-group/
layout: blank
---

<script defer src="{{ '/assets/js/reading-group.js' | relative_url }}"></script>

# OXFORD FEM READING GROUP

{% include reading-group/intro.md %}

## UPCOMING

{% include reading-group/upcoming/schedule.md %}

{% capture upcoming_refs %}{% include reading-group/upcoming/references.md %}{% endcapture %}
{% if upcoming_refs contains "{: #" %}
<details class="rg-toggle" id="references" markdown="1">
<summary><h3>REFERENCES</h3><span class="rg-hint">Click to <span class="rg-when-closed">view</span><span class="rg-when-open">hide</span> references for upcoming presentations.</span></summary>

{% include reading-group/upcoming/references.md %}

</details>
{% endif %}

<!-- band -->
<details class="rg-toggle" id="past" markdown="1">
<summary><h2>PAST</h2><span class="rg-hint">Click to <span class="rg-when-closed">view</span><span class="rg-when-open">hide</span> the records of past presentations.</span></summary>

{% include reading-group/past/schedule.md %}

<details class="rg-toggle" id="past-references" markdown="1">
<summary><h3>REFERENCES</h3><span class="rg-hint">Click to <span class="rg-when-closed">view</span><span class="rg-when-open">hide</span> references for past presentations.</span></summary>

{% include reading-group/past/references.md %}

</details>

</details>

<!-- ## [SUGGESTED READS](/reading-group/suggested/)

Click [here](/reading-group/suggested/) to view the list of suggested papers. -->
