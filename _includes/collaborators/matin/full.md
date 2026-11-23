{% include collaborators/matin/short.md %}

<div class="collab-photo"><img src="/assets/img/collaborators/matin.jpeg" alt="Matin Shams"></div>

*{% include universities/oxford.md %}*
{: .collab-affil}{% if include.date %}

<dl class="collab-details">
<dt>Date</dt><dd>{{ include.date }}</dd>{% if include.cosupervisor %}
<dt>Co-supervisor</dt><dd>{{ include.cosupervisor | markdownify | remove: '<p>' | remove: '</p>' | strip }}</dd>{% endif %}{% if include.project %}
<dt>Project</dt><dd>{{ include.project }}</dd>{% endif %}
</dl>{% endif %}

- {: .pub-preprint} [Strongly enstrophy-stable integrators for the incompressible Navier–Stokes equations](/publications/enstrophy/)
{: .collab-pubs}