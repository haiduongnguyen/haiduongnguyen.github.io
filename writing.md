---
title: Writing
title_vi: Bài viết
title_en: Writing
description: All projects and notes on statistics, machine learning, anomaly detection, and analytics engineering.
description_vi: Toàn bộ dự án và bài viết về thống kê, machine learning, anomaly detection và analytics engineering.
description_en: All projects and notes on statistics, machine learning, anomaly detection, and analytics engineering.
permalink: /writing/
---

<header class="page-intro">
  <h1><span data-lang="en">Writing</span><span data-lang="vi">Bài viết</span></h1>
</header>

{% assign projects = site.pages | where: "writing_topic", "projects" | sort: "project_order" %}
{% assign foundations = site.pages | where: "writing_topic", "foundations" | sort: "date" | reverse %}
{% assign statistics = site.pages | where: "writing_topic", "statistics" | sort: "date" | reverse %}
{% assign anomaly = site.pages | where: "writing_topic", "anomaly" | sort: "date" | reverse %}
{% assign notes = site.pages | where: "writing_topic", "notes" | sort: "date" | reverse %}
{% assign topic_groups = "projects,foundations,statistics,anomaly,notes" | split: "," %}

{% for topic in topic_groups %}
  {% case topic %}
    {% when "projects" %}{% assign articles = projects %}
    {% when "foundations" %}{% assign articles = foundations %}
    {% when "statistics" %}{% assign articles = statistics %}
    {% when "anomaly" %}{% assign articles = anomaly %}
    {% when "notes" %}{% assign articles = notes %}
  {% endcase %}
  <section class="writing-topic" id="{{ topic }}">
    <header class="writing-topic__heading">
      {% case topic %}
        {% when "projects" %}
          <div data-lang="en"><h2>Projects</h2></div>
          <div data-lang="vi"><h2>Dự án</h2></div>
        {% when "foundations" %}
          <div data-lang="en"><h2>Machine learning</h2></div>
          <div data-lang="vi"><h2>Machine learning</h2></div>
        {% when "statistics" %}
          <div data-lang="en"><h2>Statistics</h2></div>
          <div data-lang="vi"><h2>Thống kê</h2></div>
        {% when "anomaly" %}
          <div data-lang="en"><h2>Anomaly detection</h2></div>
          <div data-lang="vi"><h2>Phát hiện bất thường</h2></div>
        {% when "notes" %}
          <div data-lang="en"><h2>Analytics &amp; notes</h2></div>
          <div data-lang="vi"><h2>Analytics &amp; ghi chép</h2></div>
      {% endcase %}
    </header>
    <div class="card-grid card-grid--two">
      {% for article in articles %}
        <article class="card article-card">
          {% if article.date %}
            <div class="article-card__meta">
              <time datetime="{{ article.date | date: '%Y-%m-%d' }}">
                <span data-lang="en">{{ article.date | date: "%b %d, %Y" }}</span>
                <span data-lang="vi">{{ article.date | date: "%d/%m/%Y" }}</span>
              </time>
            </div>
          {% endif %}
          <div data-lang="en">
            <h3>{{ article.title_en | default: article.title }}</h3>
            <p>{{ article.description_en | default: article.description }}</p>
            <a class="card__link" href="{{ article.url | relative_url }}">Read article →</a>
          </div>
          <div data-lang="vi">
            <h3>{{ article.title_vi | default: article.title }}</h3>
            <p>{{ article.description_vi | default: article.description }}</p>
            <a class="card__link" href="{{ article.url | relative_url }}">Đọc bài viết →</a>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>
{% endfor %}
