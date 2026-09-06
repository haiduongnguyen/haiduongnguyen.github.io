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

A CV can list data analytics, machine learning, or time-series forecasting, but it cannot show where the data was incomplete, why one method was selected, or what would make the result fail. This website records those decisions through the work itself.

## Each article should show how I think

The useful parts of a project are usually the decisions behind it:

- How I define the problem before choosing a model.
- How I work with incomplete or noisy data.
- Why I choose one method over another.
- What I learn when the first approach is not enough.

This is why the site includes both concepts I am learning and problems drawn from real data work.

## Each useful note needs evidence or a decision

I use a simple publishing rule. A technical article should contain at least one of:

- A real data constraint that changed the approach.
- A method selected with an alternative and trade-off.
- A reproducible calculation, artifact, or experiment.
- A failure mode or limitation that affects deployment.
- An evaluation design tied to the decision being made.

A definition copied from a textbook is not enough. When an article explains a foundation such as K-means or a t-test, the explanation should still show where a practitioner can make the wrong decision.

## The topics come from my work and study

I write about:

- Data-analysis projects in banking.
- Machine-learning foundations such as regression, trees, clustering, and boosting.
- Time-series forecasting.
- Lessons from real datasets.

The first longer project on this site follows [anomaly detection in logs and metrics](/anomaly_detection/landing_page.html), from synthetic data and model notes to the scope of my master's thesis.

The [school-fee payment project](/company_projects/school_fee/) follows a different type of problem: identifying the correct transactions before forecasting them. The [K-means banking note](/data_post/kmeans/) explains why a mathematically valid cluster still needs a stable, interpretable customer profile.

These articles do not publish customer data or claim results that the available evidence cannot support. Their purpose is narrower: preserve the reasoning that a skills list leaves out, including what remains unresolved.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
# Vì sao website này giải thích quyết định thay vì liệt kê kỹ năng

CV có thể liệt kê data analytics, machine learning hay time-series forecasting, nhưng không cho thấy dữ liệu thiếu ở đâu, vì sao một method được chọn hoặc điều gì có thể làm kết quả thất bại. Website này ghi lại những quyết định đó thông qua chính các công việc đã làm.

## Mỗi bài viết cần thể hiện cách tôi tư duy

Phần hữu ích của một project thường nằm ở những quyết định phía sau nó:

- Tôi định nghĩa vấn đề thế nào trước khi chọn model.
- Tôi xử lý dữ liệu thiếu hoặc nhiễu ra sao.
- Vì sao tôi chọn một method thay vì method khác.
- Tôi học được gì khi cách tiếp cận đầu tiên chưa đủ tốt.

Vì vậy, website có cả những concept tôi đang học và những bài toán đến từ công việc thực tế với dữ liệu.

## Mỗi ghi chú hữu ích cần evidence hoặc một quyết định

Tôi dùng một publishing rule đơn giản. Một bài kỹ thuật phải có ít nhất một trong các nội dung sau:

- Một data constraint thực tế đã làm thay đổi cách tiếp cận.
- Một method được chọn cùng alternative và trade-off.
- Một calculation, artifact hoặc experiment có thể reproduce.
- Một failure mode hoặc limitation ảnh hưởng đến deployment.
- Một evaluation design gắn với quyết định cần đưa ra.

Định nghĩa chép lại từ textbook là chưa đủ. Khi một bài giải thích nền tảng như K-means hoặc t-test, nó vẫn phải chỉ ra practitioner có thể đưa ra quyết định sai ở đâu.

## Chủ đề đến từ công việc và quá trình học của tôi

Tôi viết về:

- Các project phân tích dữ liệu trong ngân hàng.
- Nền tảng machine learning như regression, tree, clustering và boosting.
- Time-series forecasting.
- Những bài học từ dữ liệu thực tế.

Project dài đầu tiên trên website theo sát bài toán [anomaly detection trong log và metric](/anomaly_detection/landing_page.html), từ synthetic data và model note đến phạm vi luận văn thạc sĩ của tôi.

[Project thanh toán học phí](/company_projects/school_fee/) đi theo một dạng bài toán khác: nhận diện đúng giao dịch trước khi forecast. [Ghi chú K-means trong ngân hàng](/data_post/kmeans/) giải thích vì sao một cluster hợp lệ về mặt toán học vẫn cần customer profile ổn định và có thể diễn giải.

Các bài viết không công bố customer data hoặc claim kết quả vượt quá evidence hiện có. Mục tiêu hẹp hơn: lưu lại phần reasoning mà skills list không thể hiện, bao gồm cả những câu hỏi chưa được giải quyết.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
