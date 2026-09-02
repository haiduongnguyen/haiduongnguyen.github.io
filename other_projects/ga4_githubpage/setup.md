---
title: Set Up GA4 on GitHub Pages
title_vi: Cài đặt GA4 trên GitHub Pages
title_en: Set up GA4 on GitHub Pages
description: A minimal, privacy-aware guide to installing and verifying GA4 on a Jekyll GitHub Pages site.
description_vi: Hướng dẫn tối thiểu và có lưu ý quyền riêng tư để cài, kiểm tra GA4 trên Jekyll GitHub Pages.
description_en: A minimal, privacy-aware guide to installing and verifying GA4 on a Jekyll GitHub Pages site.
date: 2026-02-09
writing_topic: notes
permalink: /other_projects/ga4_githubpage/setup.html
---

<section class="reading-page original-source" data-original-source="true" data-lang="en">

<div class="callout original-source__note">
<p><strong>Original article preserved in full.</strong> The editorial section that follows adds clarification without replacing the original text, code, or images.</p>
</div>

{% capture original_article_content %}

🔙 [Back to Home](/)


## Setting up GA4 for a Website

This post covers the minimal steps to set up Google Analytics 4 (GA4) for a website.
It focuses on what you actually need to get GA4 running — no advanced configuration yet.

### Prerequisites  
Before starting, make sure you have:  
A Google account   
Access to your website’s source code (or deployment pipeline)   



### Step 1: Create a GA4 property

Go to Google Analytics

Create a new account (or reuse an existing one)

Create a GA4 property

Add your website URL as a Web data stream

At the end of this step, you should receive a Measurement ID (format: G-XXXXXXXXXX).


### Step 2: Add the GA4 tag to your website

Add the following code inside the <head> section of your HTML:

```
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace G-XXXXXXXXXX with your own Measurement ID.

This setup uses gtag.js directly.
Google Tag Manager will be covered in a separate post.

### Step 3: Verify data collection

After deploying the code:
Open your website in a new browser tab
Go to GA4 → Realtime
Confirm that at least one active user appears
If nothing shows up:
Check that the Measurement ID is correct
Ensure the script is loaded only once
Disable ad blockers and retry

### Step 4: Deploy to production

Once data appears in Realtime:
Push the code to production
Leave GA4 running for at least 24 hours before evaluating data
Early data may look incomplete — this is normal.


### What’s next?

At this point, GA4 is successfully collecting data, but:
Events are still mostly automatic
Reports may feel limited
Metrics may look unfamiliar
The next posts will cover:
How GA4 events actually work
How to interpret default reports
When and why to create custom events


### Final note

GA4 setup is easy.
Understanding what GA4 measures and why is the real work — and that’s where most people get stuck.

## Default reports of GA4

- Number cus & Number events :  

![alt text](images/2.png)

- Users by country/ pages view/ channel   

![alt text](images/3.png)

- Reports built in

![alt text](images/4.png)

## Customer reports

<To be continue>   
Will be updated if this blog has more users access :>
{% endcapture %}

{{ original_article_content | markdownify }}
</section>
<article class="reading-page" data-lang="vi">
<header class="page-intro">
<p class="eyebrow">Tutorial · GA4</p>
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
<h2>Phần bổ sung: triển khai và kiểm chứng an toàn</h2>
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
<p class="eyebrow">Tutorial · GA4</p>
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
<h2>Addendum: deploy and verify safely</h2>
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
