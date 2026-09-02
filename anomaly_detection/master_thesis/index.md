---
title: Master's Thesis Journal
title_vi: Nhật ký luận văn — phát hiện bất thường đa chiều
title_en: Thesis journal — multidimensional anomaly detection
description: A transparent research journal on defining, building, and evaluating anomaly detection for logs and metrics.
description_vi: Nhật ký nghiên cứu minh bạch về định nghĩa, xây dựng và đánh giá anomaly detection cho logs và metrics.
description_en: A transparent research journal on defining, building, and evaluating anomaly detection for logs and metrics.
date: 2026-02-02
writing_topic: anomaly
permalink: /anomaly_detection/master_thesis/
---

<section class="reading-page original-source" data-original-source="true" data-lang="en">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}
## Anomaly detection

**My master thesis is "Method of applied different algorithms on multidimension data"**

🔙 [Back to Home](/)

## Story

Here is the part that I records my journey where I build this project.  
I choose new plan for this project - for me it will be way of working in future: do by ChatGPT guide.  
But I must note some key point of this:  
- Chat GPT told me that I should code 70%, GPT will help 30%. This ratio will made me do on my own to pass my master defence. 
- Chat GPT will act as a professor to guide me, not work for me


So here is my journey:
1. [Chat GPT first assignment - before coding](/anomaly-detection/thesis/first-assignment/)
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
  <header class="page-intro"><p class="eyebrow">Research journal</p><h1>Phát hiện bất thường đa chiều</h1><p>Nhật ký luận văn của tôi về anomaly detection cho logs và metrics, với trọng tâm là định nghĩa anomaly và thiết kế đánh giá trước khi tối ưu model.</p></header>
  <h2>Nguyên tắc làm việc</h2><ul><li>Tôi chịu trách nhiệm cho câu hỏi nghiên cứu, code, thí nghiệm và kết luận.</li><li>AI được dùng để phản biện, gợi ý tài liệu và review cách diễn đạt; mọi claim quan trọng phải quay về nguồn hoặc thí nghiệm.</li><li>Kết quả âm và giới hạn cũng được ghi lại.</li></ul>
  <h2>Câu hỏi chính</h2><ol><li>Khi logs và metrics thay đổi theo mùa vụ, “bất thường” nên được định nghĩa ra sao?</li><li>Rule-based baseline cạnh tranh thế nào với model không giám sát?</li><li>Đánh giá thế nào khi số incident được gán nhãn rất ít?</li></ol>
  <h2>Phần bổ sung: biến nhật ký thành research record</h2><h3>Không dùng tỷ lệ 70/30 để mô tả AI contribution</h3><p>Phần trăm này không tái lập hoặc kiểm toán được. Mỗi milestone nên ghi cụ thể: câu hỏi do ai đặt, code nào do tôi viết và test, prompt nào được dùng, claim nào đã quay về paper/documentation, và quyết định cuối cùng thuộc về ai. Commit history, experiment config và source citation có giá trị hơn một tỷ lệ ước lượng.</p><h3>Định nghĩa trước đơn vị anomaly</h3><p>Một anomaly có thể là một timestamp, một contiguous event window, một service-host pair hoặc một incident đã được triage. Nếu không chốt đơn vị này, precision/recall và RCA target sẽ thay đổi theo cách aggregation, khiến model không thể so sánh công bằng.</p><h3>Tách detection khỏi root-cause analysis</h3><p>Detection trả lời “khi nào/ở đâu có tín hiệu khác thường”; RCA cố gắng giải thích signal hoặc component nào liên quan. RCA cần ground truth hoặc evaluation protocol riêng. Không nên gọi feature importance là nguyên nhân nếu chưa có causal evidence.</p><h3>Mỗi journal entry cần một cấu trúc cố định</h3><ul><li>Question và hypothesis trước khi chạy.</li><li>Dataset version, time range và split.</li><li>Baseline, model config và random seed.</li><li>Metric cùng uncertainty.</li><li>Kết quả âm, failure mode và quyết định tiếp theo.</li></ul>
  <h2>Mốc đầu tiên</h2><p><a href="/anomaly-detection/thesis/first-assignment/">Định nghĩa scope, pipeline và acceptance criteria trước khi code →</a></p>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><p class="eyebrow">Research journal</p><h1>Multidimensional anomaly detection</h1><p>My thesis journal on anomaly detection for logs and metrics, prioritizing anomaly definitions and evaluation design before model optimization.</p></header>
  <h2>Working principles</h2><ul><li>I remain responsible for the research question, code, experiments, and conclusions.</li><li>AI is used for critique, literature prompts, and editorial review; important claims must return to a source or experiment.</li><li>Negative results and limitations are documented.</li></ul>
  <h2>Main questions</h2><ol><li>How should anomaly be defined when logs and metrics change seasonally?</li><li>How competitive is a rule-based baseline against unsupervised models?</li><li>How can performance be evaluated when very few incidents are labeled?</li></ol>
  <h2>Extension: turn the journal into a research record</h2><h3>Do not describe AI contribution with a 70/30 ratio</h3><p>The percentage is not reproducible or auditable. Each milestone should record who framed the question, which code I wrote and tested, which prompts were used, which claims were traced to papers or documentation, and who made the final decision. Commit history, experiment configurations, and citations are more useful than an estimated ratio.</p><h3>Define the anomaly unit first</h3><p>An anomaly may be a timestamp, a contiguous event window, a service-host pair, or a triaged incident. Without fixing this unit, precision/recall and the RCA target change with aggregation, making model comparisons misleading.</p><h3>Separate detection from root-cause analysis</h3><p>Detection asks when or where a signal is unusual; RCA tries to explain which signal or component is related. RCA needs its own ground truth or evaluation protocol. Feature importance should not be called a cause without causal evidence.</p><h3>Give every journal entry the same structure</h3><ul><li>Question and hypothesis written before the run.</li><li>Dataset version, time range, and split.</li><li>Baseline, model configuration, and random seed.</li><li>Metrics with uncertainty.</li><li>Negative results, failure modes, and the next decision.</li></ul>
  <h2>First milestone</h2><p><a href="/anomaly-detection/thesis/first-assignment/">Define scope, pipeline, and acceptance criteria before coding →</a></p>
</article>
