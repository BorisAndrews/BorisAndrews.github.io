{% include collaborators/oscar/short.md %}

<div class="collab-photo"><a href="https://www.linkedin.com/in/oscar-benton-642393254" tabindex="-1"><img src="/assets/img/collaborators/oscar.jpg" alt="Oscar Benton"></a></div>

*{% include universities/oxford.md %}*
{: .collab-affil}{% if include.date %}

<dl class="collab-details">
<dt>Date</dt><dd>{{ include.date }}</dd>{% if include.cosupervisor %}
<dt>Co-supervisor</dt><dd>{{ include.cosupervisor | markdownify | remove: '<p>' | remove: '</p>' | strip }}</dd>{% endif %}{% if include.project %}
<dt>Project</dt><dd>{{ include.project }}</dd>{% endif %}
</dl>{% endif %}