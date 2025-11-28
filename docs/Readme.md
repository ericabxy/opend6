---
permalink: /
---

OpenD6 is a tabletop role-playing game system designed for versatility by providing rigid rules where they are needed and loose rules for adoption, rejection, and adaptation. The core game mechanic involves a tiered hierarchy of traits.

1. [Attributes](Attribute)
2. [Skills](Skill)
3. [Specializations](Specialization)

Genre System
------------

This project details a unified [Genre System](GenreSystem) accomplished by close examination of _D6 Adventure_, _D6 Space_, and _D6 Fantasy_. The combination is meant as a guide to creating new game systems in the same way the genre books adapted and built upon the _D6 System Book_.

New Systems
-----------

- [Children of Gaia](GaiaSystem.md) - superhuman setting
- [Dungeon System](DungeonSystem.md) - experimental mapping of OpenD6 attributes to the D20 SRD
- [Magus Experiment](MagusSystem.md) - low fantasy wizardry setting
- [Sample Game System](SimpleSystem.md) - a simple cinematic system found in _System Book_
- [Solar Frontier](SolarSystem.md) - sci-fi system with themes of science, exploration, and political intrigue

<table>
  <tr>
    <th colspan='2'>Collections</th>
  </tr>
  {% for collection in site.collections %}
    <tr>
      <th>{{ collection.label }}</th>
      <td>
        {% for doc in collection.docs %}
          <a href="{{ site.url }}{{ site.baseurl }}{{ doc.url }}">{{ doc.title }}</a> &bull;
        {% endfor %}
      </td>
    </tr>
  {% endfor %}
</table>
