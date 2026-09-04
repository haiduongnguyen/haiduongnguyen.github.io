---
title: "GA4 Changed the Data Model, Not Just the Interface"
title_vi: "GA4 thay đổi data model, không chỉ giao diện"
title_en: "GA4 Changed the Data Model, Not Just the Interface"
description: GA4 records interactions through events and parameters while still deriving users, sessions, acquisition, engagement, and retention reports.
description_vi: GA4 ghi nhận tương tác qua event và parameter, đồng thời vẫn tạo report về user, session, acquisition, engagement và retention.
description_en: GA4 records interactions through events and parameters while still deriving users, sessions, acquisition, engagement, and retention reports.
date: 2026-02-09
writing_topic: notes
permalink: /other_projects/ga4_githubpage/
---

{% capture article_en %}
🔙 [Back to Home](/)

# GA4 Changed the Data Model, Not Just the Interface

Standard Universal Analytics stopped processing new data on July 1, 2023. Moving to Google Analytics 4 is not only a change of reports: GA4 records user interactions with an event-based data model.

This article is the starting point for my notes on learning GA4 and using it on this GitHub Pages site.

## The reporting funnel asks three different questions

![GA4 funnel from acquisition to retention](images/1.png)

- **Acquisition:** which channels bring users to the site?
- **Engagement:** which pages and interactions hold their attention?
- **Monetization and retention:** which users become customers, and how often do they return?

These stages should not be collapsed into one traffic number. Acquisition explains arrival, engagement explains behavior after arrival, and retention explains whether users come back.

## Events are the data model, but sessions still exist

Universal Analytics organized reporting mainly around sessions and pageviews. GA4 represents interactions such as page views, clicks, scrolls, and conversions as events. Event parameters carry additional context about each interaction.

It is more accurate to say that GA4 is **event-based** than to say that it has no sessions. GA4 still reports session-related metrics; they are derived within its event-based model.

This distinction matters when moving an old report. A UA metric should not be copied into GA4 merely because a field has a similar name—the event definition and session logic may have changed underneath it.

## GA4 connects web and app behavior through the same model

An event-based structure can represent interactions from websites and applications without requiring pageviews to be the central unit. Reports then aggregate those events into dimensions and metrics:

- A **dimension** describes an event or user, such as page title, country, or traffic channel.
- A **metric** counts or measures it, such as active users, views, event count, or sessions.

The useful question is therefore not “Which report should I open?” but “Which event, parameter, dimension, and metric represent the behavior I want to understand?”

## Continue with the implementation on this site

The next note shows how I added the Google tag once to the shared Jekyll layout and verified the data in GA4: [Set up GA4 on GitHub Pages](./setup.html).

References: [Google Analytics Help](https://support.google.com/analytics/answer/10089681?hl=en) and [Google Skillshop course](https://skillshop.docebosaas.com/learn/courses/8108/get-started-using-google-analytics/lessons/24354:8107/welcome-to-the-course-html-page).
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# GA4 thay đổi data model, không chỉ giao diện

Standard Universal Analytics ngừng xử lý dữ liệu mới từ ngày 1 tháng 7 năm 2023. Chuyển sang Google Analytics 4 không chỉ là đổi report: GA4 ghi lại tương tác của người dùng bằng event-based data model.

Bài viết này mở đầu chuỗi ghi chú của tôi khi học GA4 và áp dụng nó vào website GitHub Pages này.

## Reporting funnel trả lời ba câu hỏi khác nhau

![GA4 funnel từ acquisition đến retention](images/1.png)

- **Acquisition:** những channel nào đưa người dùng đến website?
- **Engagement:** những page và interaction nào giữ được sự chú ý của họ?
- **Monetization và retention:** người dùng nào trở thành khách hàng, và họ quay lại thường xuyên đến đâu?

Không nên gộp ba giai đoạn này thành một con số traffic. Acquisition giải thích người dùng đến từ đâu, engagement giải thích behavior sau khi họ đến, còn retention cho biết họ có quay lại hay không.

## Event là data model, nhưng session vẫn tồn tại

Universal Analytics tổ chức report chủ yếu quanh session và pageview. GA4 biểu diễn các interaction như page view, click, scroll và conversion dưới dạng event. Event parameter cung cấp thêm context cho từng interaction.

Nói GA4 **event-based** chính xác hơn nói rằng GA4 không có session. GA4 vẫn báo cáo session-related metric; các metric này được suy ra trong event-based model.

Khác biệt này quan trọng khi chuyển một report cũ. Không nên copy một UA metric sang GA4 chỉ vì field có tên tương tự—event definition và session logic bên dưới có thể đã thay đổi.

## GA4 kết nối behavior trên web và app bằng cùng một model

Event-based structure có thể biểu diễn interaction từ website và application mà không cần lấy pageview làm đơn vị trung tâm. Report sau đó tổng hợp các event thành dimension và metric:

- **Dimension** mô tả event hoặc user, chẳng hạn page title, country hoặc traffic channel.
- **Metric** đếm hoặc đo lường chúng, chẳng hạn active user, view, event count hoặc session.

Vì vậy, câu hỏi hữu ích không phải là “Tôi nên mở report nào?” mà là “Event, parameter, dimension và metric nào biểu diễn behavior tôi muốn hiểu?”

## Tiếp tục với phần triển khai trên website này

Ghi chú tiếp theo trình bày cách tôi thêm Google tag một lần vào shared Jekyll layout và kiểm tra dữ liệu trong GA4: [Thiết lập GA4 trên GitHub Pages](./setup.html).

Tham khảo: [Google Analytics Help](https://support.google.com/analytics/answer/10089681?hl=en) và [Google Skillshop course](https://skillshop.docebosaas.com/learn/courses/8108/get-started-using-google-analytics/lessons/24354:8107/welcome-to-the-course-html-page).
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
