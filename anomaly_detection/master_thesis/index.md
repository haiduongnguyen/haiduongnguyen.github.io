---
title: "My Thesis Rule for AI: I Must Own Every Decision"
title_vi: "Nguyên tắc dùng AI trong luận văn: tôi phải làm chủ mọi quyết định"
title_en: "My Thesis Rule for AI: I Must Own Every Decision"
description: How I use ChatGPT to challenge thesis scope and review decisions without delegating the research, experiments, or conclusions.
description_vi: Cách tôi dùng ChatGPT để phản biện scope và review quyết định mà không giao cho AI phần nghiên cứu, experiment hoặc kết luận.
description_en: How I use ChatGPT to challenge thesis scope and review decisions without delegating the research, experiments, or conclusions.
date: 2026-02-02
writing_topic: anomaly
permalink: /anomaly_detection/master_thesis/
---

{% capture article_en %}
🔙 [Back to Home](/)

# My Thesis Rule for AI: I Must Own Every Decision

My master's thesis is **“Method of applied different algorithms on multidimension data.”** I use ChatGPT during the work, but assistance is useful only if I can reproduce, explain, and defend every decision without asking the model to speak for me.

## ChatGPT can challenge the work but cannot own it

I chose to use ChatGPT as a professor-like guide for this project. It can question the scope, suggest reading directions, and review my plan, but it should not make the core decisions or complete the implementation for me.

My working boundary is:

- I write approximately 70% of the code and do the experiments.
- ChatGPT contributes approximately 30% through questions, guidance, and review.

The ratio is not a scientific measurement. It is a reminder that I must understand and defend the work myself during my master's defense.

The stronger rule is ownership, not percentage. I should be able to:

- Explain why each dataset, feature, model, and metric was selected.
- Reproduce every experiment from the repository and recorded configuration.
- Trace factual claims and citations to sources I have read.
- Recognize when a suggestion is technically wrong or outside the thesis scope.
- Describe failed approaches instead of allowing them to disappear from the final narrative.

If I cannot do those things, changing the claimed ratio from 70/30 to 90/10 does not solve the problem.

## The boundary is different for each task

| Task | Appropriate AI role | My responsibility |
| --- | --- | --- |
| Scope | Ask questions and expose an oversized plan | Choose and justify the final research question |
| Literature | Suggest search terms or papers to inspect | Read the sources and verify every citation |
| Code | Review a small implementation or error | Write, run, test, and understand the pipeline |
| Experiments | Suggest controls or failure checks | Define the protocol and execute every run |
| Interpretation | Challenge an unsupported conclusion | Decide what the evidence actually supports |
| Writing | Point out ambiguity or missing context | Produce and defend the final argument |

ChatGPT output is therefore a proposal, not evidence. A fluent answer does not become part of the thesis until it survives source checking or an experiment.

## The journal starts before the first model

The first entry records the questions I had to answer before coding: which data type to start with, how many models to implement, what root-cause analysis should mean, and how small the first end-to-end pipeline should be.

1. [Before coding my thesis, I had to cut the scope](/anomaly-detection/thesis/first-assignment/)

Each later entry should record four things: the decision, the evidence behind it, the alternative rejected, and the test that could prove the decision wrong. That creates a research trail rather than a polished story assembled only after the result is known.

The 70/30 rule remains a personal reminder. The publishable standard is stricter: no unverified citation, no unexplained code, and no conclusion I cannot reproduce from the recorded experiment.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Nguyên tắc dùng AI trong luận văn: tôi phải làm chủ mọi quyết định

Luận văn thạc sĩ của tôi là **“Method of applied different algorithms on multidimension data.”** Tôi sử dụng ChatGPT trong quá trình làm, nhưng sự hỗ trợ chỉ có ích khi tôi có thể tự reproduce, giải thích và bảo vệ mọi quyết định mà không cần model nói thay.

## ChatGPT có thể phản biện nhưng không thể sở hữu công việc

Tôi chọn dùng ChatGPT như một giáo sư hướng dẫn cho dự án. Nó có thể đặt câu hỏi về scope, gợi ý hướng đọc tài liệu và review kế hoạch, nhưng không nên đưa ra quyết định cốt lõi hay hoàn thành implementation thay tôi.

Ranh giới làm việc của tôi là:

- Tôi viết khoảng 70% code và tự thực hiện experiment.
- ChatGPT đóng góp khoảng 30% thông qua câu hỏi, hướng dẫn và review.

Tỉ lệ này không phải một phép đo khoa học. Nó nhắc tôi rằng bản thân phải hiểu và bảo vệ được công việc trong buổi bảo vệ luận văn.

Nguyên tắc mạnh hơn nằm ở ownership, không phải tỷ lệ. Tôi phải có khả năng:

- Giải thích vì sao từng dataset, feature, model và metric được chọn.
- Reproduce mọi experiment từ repository và configuration đã ghi lại.
- Truy ngược factual claim và citation đến source mà tôi đã tự đọc.
- Nhận ra khi một suggestion sai về kỹ thuật hoặc nằm ngoài thesis scope.
- Mô tả những approach thất bại thay vì để chúng biến mất khỏi final narrative.

Nếu tôi không làm được những điều đó, đổi tỷ lệ từ 70/30 thành 90/10 cũng không giải quyết được vấn đề.

## Ranh giới khác nhau theo từng loại công việc

| Công việc | Vai trò AI phù hợp | Trách nhiệm của tôi |
| --- | --- | --- |
| Scope | Đặt câu hỏi và chỉ ra kế hoạch quá rộng | Chọn và bảo vệ research question cuối cùng |
| Literature | Gợi ý search term hoặc paper để kiểm tra | Đọc source và xác minh mọi citation |
| Code | Review một implementation nhỏ hoặc error | Viết, chạy, test và hiểu pipeline |
| Experiment | Gợi ý control hoặc failure check | Định nghĩa protocol và tự thực hiện mọi run |
| Interpretation | Phản biện conclusion thiếu căn cứ | Quyết định evidence thực sự hỗ trợ điều gì |
| Writing | Chỉ ra chỗ mơ hồ hoặc thiếu context | Viết và bảo vệ final argument |

Vì vậy, output từ ChatGPT là proposal chứ không phải evidence. Một câu trả lời trôi chảy không trở thành một phần của luận văn cho đến khi vượt qua source checking hoặc experiment.

## Nhật ký bắt đầu trước model đầu tiên

Bài đầu tiên ghi lại những câu hỏi tôi phải trả lời trước khi code: bắt đầu với loại dữ liệu nào, triển khai bao nhiêu model, root-cause analysis cần có ý nghĩa gì và pipeline end-to-end đầu tiên nên nhỏ đến đâu.

1. [Trước khi code luận văn, tôi phải thu hẹp scope](/anomaly-detection/thesis/first-assignment/)

Mỗi entry sau đó cần ghi bốn nội dung: quyết định, evidence đứng sau, alternative bị loại và phép thử có thể chứng minh quyết định sai. Cách này tạo research trail thay vì một câu chuyện được làm đẹp sau khi đã biết kết quả.

Quy tắc 70/30 vẫn là lời nhắc cá nhân. Tiêu chuẩn công bố chặt hơn: không citation chưa kiểm chứng, không code không giải thích được và không conclusion không thể reproduce từ experiment đã ghi lại.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
