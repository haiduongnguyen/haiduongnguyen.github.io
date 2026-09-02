---
title: Writing
title_vi: Bài viết
title_en: Writing
description: All projects and notes on statistics, machine learning, anomaly detection, and analytics engineering.
description_vi: Toàn bộ dự án và bài viết về thống kê, machine learning, anomaly detection và analytics engineering.
description_en: All projects and notes on statistics, machine learning, anomaly detection, and analytics engineering.
permalink: /writing/
---

<section class="page-intro" data-lang="en">
  <p class="eyebrow">Projects &amp; writing</p>
  <h1>Explore every project and article</h1>
  <p>Browse the complete archive below. Projects are now part of the same topic-based collection, and every item remains visible on this page.</p>
</section>
<section class="page-intro" data-lang="vi">
  <p class="eyebrow">Dự án &amp; bài viết</p>
  <h1>Khám phá toàn bộ dự án và bài viết</h1>
  <p>Dự án nay nằm trong cùng một kho nội dung với các bài viết. Mọi mục đều hiển thị bên dưới; các chủ đề giúp bạn định hướng và quét danh sách nhanh hơn.</p>
</section>

<nav aria-label="Writing topics">
  <ul class="topic-index">
    <li><a href="#projects"><span data-lang="en">Projects</span><span data-lang="vi">Dự án</span></a></li>
    <li><a href="#foundations"><span data-lang="en">Machine learning</span><span data-lang="vi">Machine learning</span></a></li>
    <li><a href="#statistics"><span data-lang="en">Statistics</span><span data-lang="vi">Thống kê</span></a></li>
    <li><a href="#anomaly"><span data-lang="en">Anomaly detection</span><span data-lang="vi">Phát hiện bất thường</span></a></li>
    <li><a href="#notes"><span data-lang="en">Analytics & notes</span><span data-lang="vi">Analytics & ghi chép</span></a></li>
  </ul>
</nav>

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
          <div data-lang="en"><p class="eyebrow">Portfolio</p><h2>Projects</h2><p>Case studies centered on the problem, constraints, evaluation, and practical trade-offs.</p></div>
          <div data-lang="vi"><p class="eyebrow">Portfolio</p><h2>Dự án</h2><p>Các case study tập trung vào bài toán, ràng buộc, cách đánh giá và những đánh đổi trong thực tế.</p></div>
        {% when "foundations" %}
          <div data-lang="en"><p class="eyebrow">Foundations</p><h2>Machine learning</h2><p>Core models explained through intuition, mechanics, evaluation, and limitations.</p></div>
          <div data-lang="vi"><p class="eyebrow">Nền tảng</p><h2>Machine learning</h2><p>Các mô hình cốt lõi qua trực giác, cơ chế, cách đánh giá và giới hạn.</p></div>
        {% when "statistics" %}
          <div data-lang="en"><p class="eyebrow">Inference</p><h2>Statistics</h2><p>Choosing appropriate tests and interpreting their results without overclaiming.</p></div>
          <div data-lang="vi"><p class="eyebrow">Suy luận</p><h2>Thống kê</h2><p>Chọn kiểm định phù hợp và diễn giải kết quả mà không kết luận quá mức.</p></div>
        {% when "anomaly" %}
          <div data-lang="en"><p class="eyebrow">Research journey</p><h2>Anomaly detection</h2><p>Algorithms, evaluation choices, and an open journal of my master’s thesis.</p></div>
          <div data-lang="vi"><p class="eyebrow">Hành trình nghiên cứu</p><h2>Phát hiện bất thường</h2><p>Thuật toán, lựa chọn đánh giá và nhật ký mở về luận văn thạc sĩ của tôi.</p></div>
        {% when "notes" %}
          <div data-lang="en"><p class="eyebrow">Practice</p><h2>Analytics & notes</h2><p>Measurement, analytics engineering, and notes about building this website.</p></div>
          <div data-lang="vi"><p class="eyebrow">Thực hành</p><h2>Analytics & ghi chép</h2><p>Đo lường, analytics engineering và ghi chép về quá trình xây dựng website.</p></div>
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
