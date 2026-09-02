---
title: How I Label Evidence in Technical Articles
title_vi: Cách tôi phân loại bằng chứng trong bài kỹ thuật
title_en: How I label evidence in technical articles
description: Three evidence levels and four questions used to separate learning notes, reproducible experiments, and production case studies.
description_vi: Ba mức bằng chứng và bốn câu hỏi để phân biệt ghi chú học tập, thí nghiệm tái lập và case study production.
description_en: Three evidence levels and four questions used to separate learning notes, reproducible experiments, and production case studies.
date: 2026-01-29
writing_topic: notes
permalink: /first-post.html
---

<article class="reading-page" data-lang="vi">
<header class="page-intro">
<h1>Cách tôi phân loại bằng chứng trong bài kỹ thuật</h1>
<p>Một kết quả chỉ đáng tin khi người đọc biết dữ liệu đến từ đâu, cách kiểm chứng và giới hạn của kết luận.</p>
</header>
<h2>Ba mức bằng chứng</h2>
<ul>
<li><strong>Learning note:</strong> cách hiểu của tôi tại thời điểm viết; có thể chưa bao quát hết lý thuyết hoặc trường hợp biên.</li>
<li><strong>Reproducible experiment:</strong> có dữ liệu mẫu, code, metric và cách chạy đủ để người khác kiểm tra lại.</li>
<li><strong>Production case study:</strong> mô tả quyết định thực tế, ràng buộc vận hành và kết quả quan sát được; dữ liệu nhạy cảm phải được ẩn danh hoặc thay bằng dữ liệu tổng hợp.</li>
</ul>
<h2>Bốn câu hỏi bắt buộc</h2>
<ol><li>Bài toán và quyết định cần hỗ trợ là gì?</li><li>Baseline nào cần vượt qua?</li><li>Dữ liệu, assumptions hoặc cách đánh giá nào có thể làm kết quả sai?</li><li>Người dùng sẽ hành động thế nào từ đầu ra?</li></ol>
<h2>Quy tắc sửa lỗi và bảo mật</h2>
<p>Thay đổi ảnh hưởng tới kết luận phải được ghi lại trong bài. Kết quả thử nghiệm không được trình bày như kết quả production; dữ liệu khách hàng, credential, endpoint nội bộ và chi tiết nhận diện tổ chức không được công bố.</p>
</article>

<article class="reading-page" data-lang="en">
<header class="page-intro">
<h1>How I label evidence in technical articles</h1>
<p>A result is credible only when readers know where the data came from, how the result was validated, and what limits the conclusion.</p>
</header>
<h2>Three evidence levels</h2>
<ul>
<li><strong>Learning note:</strong> my understanding at the time of writing; it may not yet cover the full theory or every edge case.</li>
<li><strong>Reproducible experiment:</strong> sample data, code, metrics, and run instructions are sufficient for another person to check the result.</li>
<li><strong>Production case study:</strong> the article describes a real decision, operational constraints, and observed outcomes; sensitive data is anonymized or replaced with synthetic data.</li>
</ul>
<h2>Four required questions</h2>
<ol><li>What problem and decision does the work support?</li><li>Which baseline must it beat?</li><li>Which data, assumptions, or evaluation choices could make the result wrong?</li><li>How will a user act on the output?</li></ol>
<h2>Correction and confidentiality rules</h2>
<p>Changes that affect a conclusion must be recorded in the article. Experimental results must not be presented as production outcomes; customer data, credentials, internal endpoints, and organization-identifying details must not be published.</p>
</article>
