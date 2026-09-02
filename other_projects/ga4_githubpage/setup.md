---
title: Set Up GA4 on GitHub Pages
title_vi: Cài đặt GA4 trên GitHub Pages
title_en: Set up GA4 on GitHub Pages
description: Install GA4 once in a Jekyll layout, verify collection at three layers, detect duplicate tags, and account for consent.
description_vi: Cài GA4 một lần trong layout Jekyll, kiểm tra ba lớp thu thập, phát hiện tag trùng lặp và xử lý consent.
description_en: Install GA4 once in a Jekyll layout, verify collection at three layers, detect duplicate tags, and account for consent.
date: 2026-02-09
writing_topic: notes
permalink: /other_projects/ga4_githubpage/setup.html
---

<article class="reading-page" data-lang="vi">
<header class="page-intro">

<h1>Cài GA4 trên GitHub Pages</h1>
<p>Cấu hình tối thiểu cho một site Jekyll, kèm cách xác nhận dữ liệu thực sự được gửi.</p>
</header>
<h2>1. Tạo web data stream</h2>
<p>Trong Google Analytics, tạo property và web data stream cho domain. Sau đó lấy Measurement ID dạng <code>G-XXXXXXXXXX</code>.</p>
<h2>2. Thêm tag một lần</h2>
<p>Với Jekyll, đặt đoạn sau trong file include được dùng ở phần <code>&lt;head&gt;</code> của layout. Không thêm lại vào từng bài viết.</p>
<pre>
<code>&lt;script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"&gt;&lt;/script&gt;
&lt;script&gt;
  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  gtag("js", new Date());
  gtag("config", "G-XXXXXXXXXX");
&lt;/script&gt;</code>
</pre>
<h2>3. Deploy và kiểm thử</h2>
<ol>
<li>Mở source của production page và kiểm tra Measurement ID chỉ xuất hiện một lần.</li>
<li>Dùng DevTools Network để tìm request đến Google Analytics.</li>
<li>Mở Realtime hoặc DebugView và thực hiện một page view.</li>
<li>Nếu không thấy, kiểm tra ad blocker, consent state và cache deploy.</li>
</ol>
<h2>4. Quyền riêng tư</h2>
<p>Không gửi email, số điện thoại, customer ID nội bộ hoặc dữ liệu định danh cá nhân trong URL/event parameter. Tùy đối tượng và khu vực phục vụ, hãy đánh giá nhu cầu consent banner và privacy notice.</p>
<h2>5. Sau khi cài</h2>
<p>Viết measurement plan trước khi tạo custom event. Tracking nhiều không đồng nghĩa với hiểu người dùng tốt hơn.</p>
<h2>Consent mode và kiểm tra tag trùng lặp</h2>
<p>Ở phiên bản hiện tại của blog này, Google tag được nạp ngay trong <code>_includes/head-custom.html</code>. Đây là cấu hình đơn giản và đang hoạt động, nhưng nó chưa tự giải quyết yêu cầu đồng thuận. Nếu blog phục vụ người đọc tại khu vực cần consent, hãy chọn basic hoặc advanced consent mode dựa trên chính sách riêng tư và tư vấn pháp lý phù hợp. Consent mode chỉ truyền trạng thái đồng thuận tới tag; nó không thay thế giao diện xin đồng thuận.</p>
<ul>
<li><strong>Basic consent mode:</strong> chặn Google tag cho tới khi người dùng tương tác với banner.</li>
<li><strong>Advanced consent mode:</strong> nạp tag với trạng thái mặc định bị từ chối; tag có thể gửi tín hiệu không dùng cookie. Trạng thái mặc định phải được đặt trước mọi lệnh <code>config</code> hoặc <code>event</code>.</li>
</ul>
<p>Sau mỗi lần thay layout hoặc plugin analytics, có thể chạy đoạn sau trong DevTools Console để phát hiện tag bị chèn hai lần:</p>
<pre>
<code>const gaScripts = [...document.scripts]
  .map(script =&gt; script.src)
  .filter(src =&gt; src.includes("googletagmanager.com/gtag/js"));

console.table(gaScripts);
if (gaScripts.length !== 1) {
  throw new Error(`Expected one Google tag, found ${gaScripts.length}`);
}</code>
</pre>
<p>Kiểm tra đủ ba lớp: request trong Network, event trong Realtime/DebugView, và báo cáo sau thời gian xử lý. Custom parameter chỉ xuất hiện trong báo cáo chuẩn sau khi được đăng ký thành custom dimension hoặc metric. Measurement ID là cấu hình công khai, nhưng URL, tiêu đề trang và event parameter vẫn phải được kiểm soát để không làm lộ dữ liệu cá nhân.</p>
<h2>Nguồn</h2>
<ul>
<li>
<a href="https://developers.google.com/analytics/devguides/collection/ga4">Google Analytics: Set up data collection</a>
</li>
<li>
<a href="https://support.google.com/analytics/answer/7201382">Google Analytics: Verify data collection</a>
</li>
<li><a href="https://developers.google.com/tag-platform/security/concepts/consent-mode">Google: Consent mode concepts</a></li>
<li><a href="https://support.google.com/analytics/answer/6366371">Google Analytics: Avoid sending personally identifiable information</a></li>
</ul>
</article>

<article class="reading-page" data-lang="en">
<header class="page-intro">

<h1>Set up GA4 on GitHub Pages</h1>
<p>A minimal configuration for a Jekyll site, including how to confirm that data is actually being sent.</p>
</header>
<h2>1. Create a web data stream</h2>
<p>In Google Analytics, create a property and web data stream for the domain. Copy its Measurement ID in the form <code>G-XXXXXXXXXX</code>.</p>
<h2>2. Add the tag once</h2>
<p>For Jekyll, put the following snippet in an include used by the layout’s <code>&lt;head&gt;</code>. Do not repeat it in every article.</p>
<pre>
<code>&lt;script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"&gt;&lt;/script&gt;
&lt;script&gt;
  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  gtag("js", new Date());
  gtag("config", "G-XXXXXXXXXX");
&lt;/script&gt;</code>
</pre>
<h2>3. Deploy and verify</h2>
<ol>
<li>Open the production source and check that the Measurement ID appears only once.</li>
<li>Use the Network panel to find requests to Google Analytics.</li>
<li>Open Realtime or DebugView and trigger a page view.</li>
<li>If nothing appears, check ad blockers, consent state, and deployment cache.</li>
</ol>
<h2>4. Privacy</h2>
<p>Do not send email addresses, phone numbers, internal customer IDs, or personal data in URLs or event parameters. Depending on your users and jurisdictions, assess the need for consent and a privacy notice.</p>
<h2>5. After installation</h2>
<p>Write a measurement plan before creating custom events. More tracking does not automatically create more understanding.</p>
<h2>Consent mode and duplicate-tag detection</h2>
<p>In the current version of this blog, the Google tag loads immediately from <code>_includes/head-custom.html</code>. That simple setup works, but it does not resolve consent requirements by itself. If the blog serves readers in a jurisdiction where consent is required, choose basic or advanced consent mode according to your privacy policy and appropriate legal advice. Consent mode communicates a user&rsquo;s choice to tags; it does not provide the consent interface.</p>
<ul>
<li><strong>Basic consent mode:</strong> blocks Google tags until the visitor interacts with the consent banner.</li>
<li><strong>Advanced consent mode:</strong> loads tags with denied defaults; tags may send cookieless signals. Set the default state before any <code>config</code> or <code>event</code> command.</li>
</ul>
<p>After changing a layout or analytics plugin, run this in DevTools Console to detect an accidentally duplicated tag:</p>
<pre>
<code>const gaScripts = [...document.scripts]
  .map(script =&gt; script.src)
  .filter(src =&gt; src.includes("googletagmanager.com/gtag/js"));

console.table(gaScripts);
if (gaScripts.length !== 1) {
  throw new Error(`Expected one Google tag, found ${gaScripts.length}`);
}</code>
</pre>
<p>Verify all three layers: the Network request, the event in Realtime or DebugView, and the processed report. A custom parameter becomes available in standard reporting only after it is registered as a custom dimension or metric. The Measurement ID is public configuration, but URLs, page titles, and event parameters still need governance so they do not expose personal data.</p>
<h2>Sources</h2>
<ul>
<li>
<a href="https://developers.google.com/analytics/devguides/collection/ga4">Google Analytics: Set up data collection</a>
</li>
<li>
<a href="https://support.google.com/analytics/answer/7201382">Google Analytics: Verify data collection</a>
</li>
<li><a href="https://developers.google.com/tag-platform/security/concepts/consent-mode">Google: Consent mode concepts</a></li>
<li><a href="https://support.google.com/analytics/answer/6366371">Google Analytics: Avoid sending personally identifiable information</a></li>
</ul>
</article>
