---
title: How Google Analytics 4 Works
title_vi: Google Analytics 4 hoạt động như thế nào
title_en: How Google Analytics 4 works
description: GA4 records interactions as events while retaining sessions; reports require defined users, parameters, dimensions, and metrics.
description_vi: GA4 ghi interaction dưới dạng event nhưng vẫn giữ session; report cần định nghĩa rõ user, parameter, dimension và metric.
description_en: GA4 records interactions as events while retaining sessions; reports require defined users, parameters, dimensions, and metrics.
date: 2026-02-09
writing_topic: notes
permalink: /other_projects/ga4_githubpage/
---

<article class="reading-page" data-lang="vi">
  <header class="page-intro"><h1>GA4 hoạt động như thế nào?</h1><p>GA4 là hệ thống đo lường dựa trên event. Giá trị của nó không nằm ở việc cài một đoạn script, mà ở việc định nghĩa đúng hành vi cần đo.</p></header>
  <h2>Data model</h2><ul><li><strong>User:</strong> một người dùng được nhận diện bằng các identifier khả dụng; không đồng nghĩa tuyệt đối với một con người.</li><li><strong>Session:</strong> nhóm interaction bắt đầu bởi <code>session_start</code>.</li><li><strong>Event:</strong> một hành vi như <code>page_view</code>, <code>scroll</code> hoặc event do mình định nghĩa.</li><li><strong>Parameter:</strong> ngữ cảnh đi kèm event, ví dụ page location hoặc article category.</li></ul>
  <figure><img src="images/1.png" alt="Sơ đồ funnel người dùng đi qua các bước tương tác trong GA4"><figcaption>Một funnel chỉ hữu ích khi mỗi bước tương ứng với một hành vi có ý nghĩa.</figcaption></figure>
  <h2>Dimension và metric</h2><p>Dimension mô tả dữ liệu, như country, page path hoặc channel. Metric là số đo, như users, sessions, event count hoặc conversion rate. Một report tốt bắt đầu từ câu hỏi, sau đó mới chọn dimension và metric.</p>
  <h2>Measurement plan tối thiểu</h2><ol class="process"><li>Viết câu hỏi kinh doanh.</li><li>Xác định hành vi chứng minh progress.</li><li>Đặt tên event và parameter nhất quán.</li><li>Kiểm thử bằng DebugView/Realtime.</li><li>Tạo report phục vụ quyết định cụ thể.</li><li>Review chất lượng dữ liệu định kỳ.</li></ol>
  <p><a href="/other_projects/ga4_githubpage/setup.html">Xem hướng dẫn cài GA4 cho GitHub Pages →</a></p>
  <h2>Session, event taxonomy và reporting schema</h2>
  <h3>Event-based không có nghĩa session biến mất</h3><p>GA4 lưu interaction theo event, nhưng vẫn có <code>session_start</code> và session-scoped metrics. Khác biệt quan trọng là event trở thành đơn vị dữ liệu linh hoạt hơn; không nên kỳ vọng metric GA4 khớp một-một với Universal Analytics vì identity, sessionization và attribution có thể khác.</p>
  <h3>Ưu tiên recommended event trước custom event</h3><p>Trước khi đặt tên mới, kiểm tra automatically collected, enhanced measurement và recommended events. Việc dùng taxonomy chuẩn giúp tận dụng report có sẵn và giảm nhiều tên khác nhau cho cùng một hành vi. Mỗi event cần owner, trigger, required parameters và ví dụ kiểm thử.</p>
  <h3>Gửi parameter chưa đủ để dùng nó trong report</h3><p>Parameter tùy chỉnh cần được đăng ký thành custom dimension hoặc custom metric nếu muốn phân tích trong standard report/Exploration. Chỉ nhìn thấy parameter ở DebugView không có nghĩa schema reporting đã hoàn tất.</p>
  <h3>User không đồng nghĩa với một con người duy nhất</h3><p>Browser identifier, User-ID và modeled identity có phạm vi khác nhau. Cross-device reporting phụ thuộc cách triển khai identity và consent; vì vậy hãy mô tả “user theo định nghĩa property” thay vì khẳng định số người tuyệt đối.</p>
  <h3>Measurement plan cho chính blog này</h3><ul><li><code>page_view</code>: bài nào thực sự được mở.</li><li><code>scroll</code>: chỉ là tín hiệu đọc thô, không chứng minh hiểu nội dung.</li><li><code>select_content</code> hoặc custom event có kiểm soát: click từ Writing sang một bài.</li><li>Không gửi email, tên, query chứa dữ liệu cá nhân hoặc internal identifier trong URL/parameter.</li></ul>
  <h2>Nguồn</h2><ul><li><a href="https://developers.google.com/analytics/devguides/collection/ga4">Google Analytics developer documentation</a></li><li><a href="https://support.google.com/analytics/answer/9322688">Google Analytics: Events</a></li></ul>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro"><h1>How GA4 works</h1><p>GA4 is an event-based measurement system. Its value does not come from installing a script; it comes from defining the right behavior to measure.</p></header>
  <h2>Data model</h2><ul><li><strong>User:</strong> a user identified through available identifiers; not a perfect one-to-one representation of a person.</li><li><strong>Session:</strong> a group of interactions initiated by <code>session_start</code>.</li><li><strong>Event:</strong> a behavior such as <code>page_view</code>, <code>scroll</code>, or a custom event.</li><li><strong>Parameter:</strong> context attached to an event, such as page location or article category.</li></ul>
  <figure><img src="images/1.png" alt="A funnel of user interactions measured in GA4"><figcaption>A funnel is useful only when every step maps to meaningful behavior.</figcaption></figure>
  <h2>Dimensions and metrics</h2><p>Dimensions describe data, such as country, page path, or channel. Metrics quantify it, such as users, sessions, event count, or conversion rate. A useful report starts with a question and only then selects dimensions and metrics.</p>
  <h2>Minimal measurement plan</h2><ol class="process"><li>Write the business question.</li><li>Identify behavior that demonstrates progress.</li><li>Name events and parameters consistently.</li><li>Test with DebugView or Realtime.</li><li>Build a report for a specific decision.</li><li>Review data quality regularly.</li></ol>
  <p><a href="/other_projects/ga4_githubpage/setup.html">Read the GA4 setup guide for GitHub Pages →</a></p>
  <h2>Sessions, event taxonomy, and reporting schema</h2>
  <h3>Event-based does not mean sessions disappeared</h3><p>GA4 stores interactions as events, but still collects <code>session_start</code> and exposes session-scoped metrics. The important change is that events are the more flexible data unit. Do not expect GA4 metrics to match Universal Analytics one-for-one because identity, sessionization, and attribution can differ.</p>
  <h3>Prefer recommended events before inventing custom ones</h3><p>Check automatically collected, enhanced-measurement, and recommended events before naming a new event. A standard taxonomy unlocks built-in reporting and prevents multiple names for the same behavior. Give each event an owner, trigger, required parameters, and a test example.</p>
  <h3>Sending a parameter does not make it report-ready</h3><p>Custom parameters must be registered as custom dimensions or metrics when you want to analyze them in standard reports or Explorations. Seeing a parameter in DebugView does not mean the reporting schema is complete.</p>
  <h3>A user is not automatically one unique human</h3><p>Browser identifiers, User-ID, and modeled identity have different scopes. Cross-device reporting depends on identity implementation and consent, so describe “users under the property’s identity definition” rather than claiming an absolute number of people.</p>
  <h3>A measurement plan for this blog</h3><ul><li><code>page_view</code>: which article was opened.</li><li><code>scroll</code>: a coarse reading signal, not proof of understanding.</li><li><code>select_content</code> or one controlled custom event: navigation from Writing to an article.</li><li>Never send email, names, personal query values, or internal identifiers in URLs or parameters.</li></ul>
  <h2>Sources</h2><ul><li><a href="https://developers.google.com/analytics/devguides/collection/ga4">Google Analytics developer documentation</a></li><li><a href="https://support.google.com/analytics/answer/9322688">Google Analytics: Events</a></li></ul>
</article>
