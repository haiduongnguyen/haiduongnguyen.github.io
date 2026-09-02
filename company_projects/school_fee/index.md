---
title: Modeling School-Fee Payments as Time Series
title_vi: Mô hình hóa giao dịch học phí bằng time series
title_en: Modeling school-fee payments as time series
description: Beneficiary-name entity resolution produces customer–school time series evaluated at matching and forecasting layers.
description_vi: Entity resolution từ beneficiary name tạo chuỗi thời gian customer–school được đánh giá ở hai tầng matching và forecasting.
description_en: Beneficiary-name entity resolution produces customer–school time series evaluated at matching and forecasting layers.
date: 2026-02-05
writing_topic: projects
project_order: 1
permalink: /company_projects/school_fee/
---

<article class="reading-page" data-lang="vi">
  <header class="page-intro">

    <h1>Mô hình hóa giao dịch học phí</h1>
    <p>Từ beneficiary name thiếu chuẩn hóa đến tín hiệu thanh toán theo mùa có thể dùng cho phân tích khách hàng.</p>
    <div class="meta-row"><span>Cập nhật: 05/02/2026</span><span>Khoảng 7 phút đọc</span></div>
  </header>

  <div class="callout"><p><strong>Phạm vi bảo mật:</strong> không có dữ liệu khách hàng, rule nội bộ hoặc kết quả kinh doanh bí mật.</p></div>

  <h2>Bài toán</h2>
  <p>Học phí là một khoản chi tương đối đều đặn đối với gia đình có con đi học. Nếu nhận diện được các giao dịch này một cách đủ tin cậy, pattern về số tiền và thời điểm có thể hỗ trợ:</p>
  <ul>
    <li><strong>Lending:</strong> ước lượng một dòng tiền ra có tính chu kỳ.</li>
    <li><strong>Customer profiling:</strong> bổ sung tín hiệu về vòng đời và khả năng tài chính.</li>
    <li><strong>Campaign timing:</strong> xác định các giai đoạn chi tiêu theo mùa.</li>
  </ul>

  <figure>
    <img src="images/1.png" alt="Sơ đồ dòng thanh toán học phí giữa khách hàng và trường học" width="225" height="225">
    <figcaption>Tín hiệu cần tìm nằm trong dòng thanh toán giữa khách hàng và trường học.</figcaption>
  </figure>

  <h2>Vì sao nhận diện khó?</h2>
  <p>Trường hợp lý tưởng là biết rõ người gửi và trường nhận tiền. Nhưng phần lớn tài khoản trường học nằm ngoài ngân hàng, nên thông tin receiver đầy đủ thường không có trong dữ liệu nội bộ. Tín hiệu còn lại chủ yếu là beneficiary name.</p>
  <p>Trường tên là dữ liệu nhiễu: không có chuẩn viết chung, chứa viết tắt hoặc lỗi chính tả, và nhiều trường có tên gần giống nhau. Matching đơn giản theo từ khóa vì vậy dễ tạo false positive.</p>

  <h2>Quy trình đề xuất</h2>
  <ol class="process">
    <li><strong>Tạo candidate set.</strong> Chuẩn hóa Unicode, chữ hoa/thường và ký tự thừa; lọc các giao dịch có tín hiệu liên quan đến trường học.</li>
    <li><strong>Chuẩn hóa thực thể.</strong> Gom các biến thể beneficiary name về một school entity bằng rule, fuzzy matching và danh mục tham chiếu đã kiểm tra.</li>
    <li><strong>Chấm điểm độ tin cậy.</strong> Kết hợp tên, số khách hàng, tần suất, khoảng tiền và tính mùa vụ thay vì dựa vào một từ khóa.</li>
    <li><strong>Kiểm chứng.</strong> Lấy mẫu theo từng vùng điểm để review thủ công; theo dõi precision trước khi mở rộng coverage.</li>
    <li><strong>Tạo feature.</strong> Tổng hợp theo customer–school–month và chỉ đưa feature ổn định vào feature mart.</li>
    <li><strong>Theo dõi drift.</strong> Kiểm tra trường mới, tên mới và sự thay đổi pattern qua mỗi kỳ học.</li>
  </ol>

  <h2>Từ giao dịch đến time series</h2>
  <p>Sau khi có tập giao dịch đủ tin cậy, mỗi khách hàng được biểu diễn bằng tổng tiền và số lần thanh toán theo tháng. Có hai góc nhìn bổ trợ nhau:</p>
  <ul>
    <li><strong>Customer-level:</strong> decomposition trend, seasonality và residual; backtest theo rolling window để dự báo các tháng tiếp theo.</li>
    <li><strong>School-level:</strong> học pattern thu phí đặc trưng của từng trường, sau đó dùng pattern này làm prior cho khách hàng đã từng thanh toán tại trường đó.</li>
  </ul>

  <h2>Đánh giá đúng cách</h2>
  <p>Bài toán gồm hai tầng nên không thể chỉ nhìn một metric:</p>
  <ul>
    <li><strong>Entity matching:</strong> precision, recall và coverage trên tập được gán nhãn thủ công.</li>
    <li><strong>Forecast:</strong> MAE/WAPE so với baseline “cùng kỳ năm trước”, đánh giá bằng time-based split.</li>
    <li><strong>Business usefulness:</strong> độ ổn định của feature và lift khi đưa vào use case downstream.</li>
  </ul>

  <h2>Ngưỡng matching, backtest và rủi ro của proxy</h2>
  <h3>Tách precision, coverage và vùng abstain</h3>
  <p>Entity matcher không nhất thiết phải ép mọi transaction thành một school entity. Có thể dùng ba vùng: auto-accept ở confidence cao, manual review ở vùng giữa và abstain ở confidence thấp. Báo precision cùng coverage tại từng threshold giúp người đọc thấy trade-off thay vì chỉ một accuracy tổng hợp.</p>
  <h3>Backtest phải đi qua ranh giới năm học</h3>
  <p>Payment theo tháng có thể thưa, irregular và thay đổi quanh kỳ nhập học. Rolling-origin backtest nên bao phủ ít nhất một chu kỳ năm học hoàn chỉnh, so với seasonal-naive baseline và báo riêng error cho customer mới, school mới và customer có lịch sử đủ dài.</p>
  <h3>Ngăn leakage giữa matching và forecasting</h3>
  <p>Reference list, school popularity và feature aggregation tại thời điểm t chỉ được dùng dữ liệu có trước t. Nếu entity map được làm sạch bằng thông tin phát sinh sau test period, forecasting result sẽ lạc quan giả tạo dù split theo thời gian.</p>
  <h3>Không biến proxy thành sự thật về khách hàng</h3>
  <p>School-fee-like payment chỉ là một signal có uncertainty; nó không chứng minh quan hệ cha mẹ–con, thu nhập hay khả năng trả nợ. Downstream use case cần review về fairness, explainability, retention và quyền truy cập, đồng thời tránh dùng proxy nhạy cảm như một quyết định tự động duy nhất.</p>
  <div class="callout"><p><strong>Ranh giới công bố:</strong> không có label set hoặc outcome được phép công bố; các metric là kế hoạch đánh giá, không phải precision, forecast lift hoặc business uplift đã đạt được.</p></div>

  <h2>Entity resolution đặt trần hiệu quả cho toàn bộ pipeline</h2>
  <p>Phần khó nhất không phải chọn thuật toán dự báo. Chất lượng của entity resolution quyết định trần hiệu quả của toàn bộ pipeline. Một model phức tạp không thể bù cho tập giao dịch đầu vào có quá nhiều false positive.</p>
</article>

<article class="reading-page" data-lang="en">
  <header class="page-intro">

    <h1>Modeling school-fee payments</h1>
    <p>From unstandardized beneficiary names to seasonal payment signals that can support customer analytics.</p>
    <div class="meta-row"><span>Updated: February 5, 2026</span><span>About 7 min read</span></div>
  </header>

  <div class="callout"><p><strong>Confidentiality scope:</strong> no customer data, internal rules, or confidential business results are included.</p></div>

  <h2>The problem</h2>
  <p>School fees are a relatively regular expense for families with children. If these payments can be identified reliably, their amount and timing can support:</p>
  <ul>
    <li><strong>Lending:</strong> estimating a recurring cash outflow.</li>
    <li><strong>Customer profiling:</strong> adding lifecycle and financial-capacity signals.</li>
    <li><strong>Campaign timing:</strong> identifying seasonal spending periods.</li>
  </ul>

  <figure>
    <img src="images/1.png" alt="Diagram of a school-fee payment between a customer and a school" width="225" height="225">
    <figcaption>The signal of interest sits in the payment flow between a customer and a school.</figcaption>
  </figure>

  <h2>Why identification is difficult</h2>
  <p>In the ideal case, both the sender and the receiving school are known. In practice, most school accounts sit outside the bank, so complete receiver information is often unavailable. The main remaining signal is the beneficiary name.</p>
  <p>School names are noisy: there is no shared format, abbreviations and spelling variations are common, and many schools have similar names. Simple keyword matching therefore creates false positives.</p>

  <h2>Proposed workflow</h2>
  <ol class="process">
    <li><strong>Create a candidate set.</strong> Normalize Unicode, case, and punctuation; retain transactions with school-related signals.</li>
    <li><strong>Resolve entities.</strong> Map beneficiary-name variants to a school entity with rules, fuzzy matching, and a reviewed reference list.</li>
    <li><strong>Score confidence.</strong> Combine name, customer count, frequency, amount range, and seasonality instead of relying on one keyword.</li>
    <li><strong>Validate.</strong> Manually review stratified samples and monitor precision before expanding coverage.</li>
    <li><strong>Build features.</strong> Aggregate by customer–school–month and publish only stable features to the feature mart.</li>
    <li><strong>Monitor drift.</strong> Check new schools, name variants, and pattern changes each academic period.</li>
  </ol>

  <h2>From transactions to time series</h2>
  <p>Once the transaction set is reliable enough, each customer can be represented by monthly payment amount and frequency. Two complementary views are useful:</p>
  <ul>
    <li><strong>Customer level:</strong> decompose trend, seasonality, and residuals; use rolling backtests for forecasting.</li>
    <li><strong>School level:</strong> learn each school’s collection pattern and use it as a prior for customers who have paid that school before.</li>
  </ul>

  <h2>Evaluation</h2>
  <p>The problem has two layers, so one metric is not enough:</p>
  <ul>
    <li><strong>Entity matching:</strong> precision, recall, and coverage on a manually labeled set.</li>
    <li><strong>Forecasting:</strong> MAE/WAPE against a same-period-last-year baseline with time-based splits.</li>
    <li><strong>Business usefulness:</strong> feature stability and lift in the downstream use case.</li>
  </ul>

  <h2>Matching thresholds, backtesting, and proxy risk</h2>
  <h3>Separate precision, coverage, and an abstain region</h3>
  <p>An entity matcher does not need to force every transaction into a school entity. Use three regions: auto-accept at high confidence, manual review in the middle, and abstain at low confidence. Reporting precision and coverage at each threshold exposes the trade-off instead of hiding it behind one aggregate accuracy.</p>
  <h3>Backtest across academic-year boundaries</h3>
  <p>Monthly payments may be sparse, irregular, and concentrated around enrollment periods. A rolling-origin backtest should cover at least one complete academic cycle, compare against a seasonal-naive baseline, and report errors separately for new customers, new schools, and customers with enough history.</p>
  <h3>Prevent leakage between matching and forecasting</h3>
  <p>Reference lists, school popularity, and aggregates available at time t must use information available before t. If an entity map is cleaned with evidence observed after the test period, the forecast looks falsely strong even with a time-based split.</p>
  <h3>Do not turn a proxy into a fact about a customer</h3>
  <p>A school-fee-like payment is an uncertain signal; it does not prove parent–child relationships, income, or repayment capacity. Downstream uses need fairness, explainability, retention, and access review, and the proxy should not become the sole input to an automated decision.</p>
  <div class="callout"><p><strong>Publication boundary:</strong> no publishable label set or outcome is available; the metrics are an evaluation plan, not achieved matching precision, forecast lift, or business uplift.</p></div>

  <h2>Entity resolution sets the performance ceiling for the pipeline</h2>
  <p>The hardest part is not choosing a forecasting algorithm. Entity-resolution quality sets the ceiling for the entire pipeline. A complex model cannot compensate for an input set dominated by false positives.</p>
</article>
