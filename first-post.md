---
title: Why I Started This Website
title_vi: Vì sao tôi bắt đầu website này
title_en: Why I started this website
description: The purpose and editorial direction of Hai Duong Nguyen's data blog.
description_vi: Mục đích và định hướng nội dung của blog dữ liệu của Hải Dương Nguyễn.
description_en: The purpose and editorial direction of Hai Duong Nguyen's data blog.
date: 2026-01-29
writing_topic: notes
permalink: /first-post.html
---

<section class="reading-page original-source" data-original-source="true" data-lang="en">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}

# Why I started this website

I created this website to document my learning journey in data analytics
and machine learning.

Instead of listing skills on a CV, I want to explain:
- how I think
- how I solve real problems
- what I learned from real data

## What I will write about

- Data analysis projects in banking
- Machine learning concepts (PCA, trees, boosting)
- Time series forecasting
- Lessons learned from real datasets

## Next step

My next post will document a real project:
**Metrics Anomaly Detection in Banking Systems**.
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
<header class="page-intro">
<p class="eyebrow">Editorial note</p>
<h1>Vì sao tôi bắt đầu website này</h1>
<p>Tôi muốn cho thấy cách mình suy nghĩ và giải quyết vấn đề, thay vì chỉ liệt kê kỹ năng trên CV.</p>
</header>
<p>Blog ghi lại ba loại nội dung: case study từ dữ liệu thực tế đã được ẩn danh; ghi chép kỹ thuật có ví dụ và nguồn; nhật ký về những thử nghiệm chưa thành công và điều cần sửa.</p>
<p>Tiêu chuẩn tôi hướng tới cho mỗi bài là: nêu rõ câu hỏi, assumptions, cách kiểm chứng và giới hạn. Khi một bài chỉ là ghi chú đang học, tôi sẽ nói rõ điều đó.</p>
<h2>Cam kết biên tập</h2>
<p>Để người đọc biết nên tin một kết luận đến mức nào, tôi sẽ phân biệt rõ ba mức bằng chứng:</p>
<ul>
<li><strong>Learning note:</strong> cách hiểu của tôi tại thời điểm viết; có thể chưa bao quát hết lý thuyết hoặc trường hợp biên.</li>
<li><strong>Reproducible experiment:</strong> có dữ liệu mẫu, code, metric và cách chạy đủ để người khác kiểm tra lại.</li>
<li><strong>Production case study:</strong> mô tả quyết định thực tế, ràng buộc vận hành và kết quả quan sát được; dữ liệu nhạy cảm phải được ẩn danh hoặc thay bằng dữ liệu tổng hợp.</li>
</ul>
<p>Nếu phát hiện lỗi, tôi sẽ sửa ngay trong bài và ghi chú nội dung nào đã thay đổi khi sự thay đổi ảnh hưởng tới kết luận. Tôi sẽ không biến một kết quả thử nghiệm thành tuyên bố production, và cũng không công bố dữ liệu khách hàng, credential, endpoint nội bộ hay chi tiết có thể nhận diện tổ chức.</p>
<h2>Lộ trình nội dung</h2>
<p>Các bài tiếp theo sẽ nối kiến thức nền với bài toán thực tế: từ regression, classification và clustering tới phát hiện bất thường, phân tích nguyên nhân gốc và giám sát model. Mỗi bài nên trả lời được bốn câu hỏi: bài toán là gì, baseline nào cần vượt qua, điều gì có thể làm kết quả sai, và người dùng sẽ hành động ra sao từ đầu ra của model.</p>
<p>Bài case study đầu tiên là <a href="/company_projects/school_fee/">mô hình hóa giao dịch học phí</a>.</p>
</article>
<article class="reading-page" data-lang="en">
<header class="page-intro">
<p class="eyebrow">Editorial note</p>
<h1>Why I started this website</h1>
<p>I want to show how I think and solve problems instead of listing skills on a résumé.</p>
</header>
<p>The blog contains three kinds of writing: anonymized real-world case studies, technical notes with examples and sources, and honest journals about experiments that did not work.</p>
<p>My standard for each article is to state the question, assumptions, validation method, and limitations. When something is only a learning note, I will label it clearly.</p>
<h2>Editorial contract</h2>
<p>To help readers judge how much confidence a conclusion deserves, I will distinguish three levels of evidence:</p>
<ul>
<li><strong>Learning note:</strong> my understanding at the time of writing; it may not yet cover the full theory or every edge case.</li>
<li><strong>Reproducible experiment:</strong> sample data, code, metrics, and run instructions are sufficient for another person to check the result.</li>
<li><strong>Production case study:</strong> the article describes a real decision, operational constraints, and observed outcomes; sensitive data is anonymized or replaced with synthetic data.</li>
</ul>
<p>If I find an error, I will correct it in the article and note material changes when they affect the conclusion. I will not present an experiment as a production result, and I will not publish customer data, credentials, internal endpoints, or details that could identify an organization.</p>
<h2>Content roadmap</h2>
<p>Future posts will connect foundations to real systems: from regression, classification, and clustering to anomaly detection, root-cause analysis, and model monitoring. Each article should answer four questions: What is the problem? Which baseline must we beat? What could make the result wrong? How will a user act on the model output?</p>
<p>The first full case study is <a href="/company_projects/school_fee/">modeling school-fee payments</a>.</p>
</article>
