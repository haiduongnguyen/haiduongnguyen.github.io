---
title: "Why This Site Explains Decisions Instead of Listing Skills"
title_vi: "Vì sao website này giải thích quyết định thay vì liệt kê kỹ năng"
title_en: "Why This Site Explains Decisions Instead of Listing Skills"
description: I use this site to record how I approach banking-data and machine-learning problems, including what I learn from real datasets.
description_vi: Tôi dùng website này để ghi lại cách tiếp cận bài toán dữ liệu ngân hàng và machine learning, cùng những điều học được từ dữ liệu thực tế.
description_en: I use this site to record how I approach banking-data and machine-learning problems, including what I learn from real datasets.
date: 2026-01-29
writing_topic: notes
permalink: /first-post.html
---

{% capture article_en %}
# Why This Site Explains Decisions Instead of Listing Skills

A CV can list data analytics, machine learning, or time-series forecasting, but it cannot show how I approach a problem. I created this website to document that reasoning through the work itself.

## Each article should show how I think

The useful parts of a project are usually the decisions behind it:

- How I define the problem before choosing a model.
- How I work with incomplete or noisy data.
- Why I choose one method over another.
- What I learn when the first approach is not enough.

This is why the site includes both concepts I am learning and problems drawn from real data work.

## The topics come from my work and study

I write about:

- Data-analysis projects in banking.
- Machine-learning foundations such as regression, trees, clustering, and boosting.
- Time-series forecasting.
- Lessons from real datasets.

The first longer project on this site follows [anomaly detection in logs and metrics](/anomaly_detection/landing_page.html), from synthetic data and model notes to the scope of my master's thesis.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
# Vì sao website này giải thích quyết định thay vì liệt kê kỹ năng

CV có thể liệt kê data analytics, machine learning hay time-series forecasting, nhưng không thể hiện được cách tôi tiếp cận một vấn đề. Tôi tạo website này để ghi lại quá trình suy luận đó thông qua chính các công việc đã làm.

## Mỗi bài viết cần thể hiện cách tôi tư duy

Phần hữu ích của một project thường nằm ở những quyết định phía sau nó:

- Tôi định nghĩa vấn đề thế nào trước khi chọn model.
- Tôi xử lý dữ liệu thiếu hoặc nhiễu ra sao.
- Vì sao tôi chọn một method thay vì method khác.
- Tôi học được gì khi cách tiếp cận đầu tiên chưa đủ tốt.

Vì vậy, website có cả những concept tôi đang học và những bài toán đến từ công việc thực tế với dữ liệu.

## Chủ đề đến từ công việc và quá trình học của tôi

Tôi viết về:

- Các project phân tích dữ liệu trong ngân hàng.
- Nền tảng machine learning như regression, tree, clustering và boosting.
- Time-series forecasting.
- Những bài học từ dữ liệu thực tế.

Project dài đầu tiên trên website theo sát bài toán [anomaly detection trong log và metric](/anomaly_detection/landing_page.html), từ synthetic data và model note đến phạm vi luận văn thạc sĩ của tôi.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
