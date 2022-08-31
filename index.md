---
layout: single
title: Course Overview
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
author_info: true
---

# Information for CSE 431

**CSE 431: Algorithm Engineering**

Below are the documents and links needed for Fall 2022.

**[Syllabus](syllabus.html)** - provides basic information about the course including how you will be graded.

**[Piazza](piazza.com/msu/fall2022/cse431/home)** a place for asynchronous discussions and Q&A sessions.

**Zoom** will be used for all class sessions.  The Zoom link has been e-mailed to all students and can be found on Piazza.

Below are the week-by-week topics that will be covered.


# Due dates

- Every friday: weekly lecture review
- Homework: 9/14, 9/28, 10/12, 10/26, 11/9, 11/23, 12/7
- Mid-term: Week of October 17th (scheduled individually)
- Final: Week of December 12th (scheduled invidually)

# Current course content

{% for post in site.weeks %}

  {% assign this_week = "now" | date: "%W" | minus: 1 %}
  {% assign last_week = "now" | date: "%W" | minus: 2 %}
  {% assign next_week = "now" | date: "%W" | plus: 0 %}

  {% assign postWeek = post.date | date: "%W" | minus: 0 %}

  {% if postWeek == last_week %}
   <h2>Last week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}

  {% if postWeek == this_week %}
   <h2>This week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}

 {% if postWeek == next_week %}
   <h2>Next week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}


{% endfor %}

# Reference material

## Data structure runtimes table

![Table of big-O time complexities for common operations on various data structures](DataStructureRuntimes.png)
