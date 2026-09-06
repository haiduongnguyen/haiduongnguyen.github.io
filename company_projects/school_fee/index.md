---
title: "School-Fee Payments: Identify Before Forecasting Them"
title_vi: "Thanh toán học phí: nhận diện trước khi dự báo"
title_en: "School-Fee Payments: Identify Before Forecasting Them"
description: Identify school-fee transactions first, then estimate when a customer will pay and the expected ticket size.
description_vi: Nhận diện giao dịch học phí trước, sau đó ước tính thời điểm khách hàng thanh toán và ticket size dự kiến.
description_en: Identify school-fee transactions first, then estimate when a customer will pay and the expected ticket size.
date: 2026-02-05
writing_topic: projects
project_order: 1
permalink: /company_projects/school_fee/
---

{% capture article_en %}
🔙 [Back to Home](/)

# School-Fee Payments: Identify Before Forecasting Them

Forecasting is not the first problem. Before estimating when a customer will pay school fees and how much, we need to identify which bank transactions are actually school-fee payments and, when possible, which school received them. Otherwise, a forecasting model can produce precise-looking answers for the wrong transactions.

## The use cases need more than a school-fee label

School-fee payments often recur around school-specific collection periods, although their timing and amount can change between terms. Once identified, they can support three use cases:

| Use case | Information required | How it is used |
| --- | --- | --- |
| Unsecured lending | Expected payment time and amount (ticket size) | Estimate a recurring cash outflow |
| Financial capacity | Historical fee amount and payment frequency | Use as a supporting signal of financial capacity, not a conclusion on its own |
| Credit card | Months in which school-fee payments concentrate | Time seasonal campaigns |

A school-fee label alone is therefore not enough. The useful output needs four fields: the customer, the matched school, the likely payment period, and the expected amount.

## The ideal transaction identifies both parties

In the ideal case, both sides of the transaction are known:

- Sender: a parent or student
- Receiver: the school

With both entities identified, the payment purpose is much easier to infer. In practice, however, the bank usually has a much clearer view of the sender than of the receiver.

![Customer transactions](images/1.png)

## Receiver-side data is incomplete when the school uses another bank

In Viet Nam, schools use accounts from many different banks, while only a small number use TCB accounts. When a customer pays a school at another bank, the receiver-side information available internally is limited. Receiver account IDs alone therefore cannot provide a complete school list.

The main usable identity signal is the beneficiary name, which often contains the school name. This signal is noisy:

- Beneficiary names are not standardized.
- Spelling variations and abbreviations are common.
- Different schools may have similar or identical names.

For example, a full name such as `TRUONG TRUNG HOC PHO THONG <NAME>` may appear in abbreviated forms such as `THPT <NAME>` or `TRUONG <NAME>`. These variations may refer to the same school, while the same shortened name may also refer to different schools. Beneficiary-name matching can therefore assign a transaction to the wrong school or classify a non-school transaction as a school-fee payment.

## Keywords create candidates; repeated behavior validates them

The identification process separates broad candidate generation from stricter validation:

1. Create a high-recall candidate set from beneficiary names containing school-related keywords. The list can include `Truong`, `Tieu hoc`, `TH`, `Trung hoc`, `THCS`, `THPT`, `Dai hoc`, `DH`, `Mam non`, `Mau giao`, and `Hoc phi`.
2. Analyze the customers connected to each candidate using payment frequency, amount, and timing.
3. Look for customer-level consistency: the same customer transferring money to the same school across multiple months or years is stronger evidence than a single transaction.
4. Look for receiver-level consistency: transaction count, customer count, and concentration around recurring collection periods help distinguish a school from an accidental keyword match.
5. Resolve ambiguous school names and remove likely false positives.
6. Finalize the school-fee transaction set, aggregate features from both the customer and school perspectives, and integrate them into the feature mart.

The keyword list deliberately favors recall; the behavioral checks provide precision. Treating a keyword match as the final label would collapse these two jobs and allow false positives into every downstream analysis.

## The forecast has three separate targets

With 3–4 years of identified transactions, we restructure each customer's monthly payments into a time series. The final prediction is easier to reason about when split into three targets:

1. **Whether:** is the customer likely to make a school-fee payment in the next three months?
2. **When:** in which month is the payment most likely?
3. **Where and how much:** which previously observed school is the likely receiver, and what ticket size should be expected?

Time-series decomposition separates trend, seasonality, and residual behavior to support the timing and amount estimates. The customer's previous school relationships provide the candidate receiver; one time-series model is not expected to infer every target by itself.

## Two prediction tables provide independent evidence

The process produces two views of the next payment period:

- **Customer-level prediction:** for each customer, predict the school they will pay, the payment time, and the amount.
- **School-level prediction:** for each school, consider its historical payers and predict which of them are likely to pay during its next collection period.

The school-level view uses the school's collection pattern rather than treating every customer as a candidate. If School A usually collects fees in January and August, customers who previously paid School A are expected to be more likely to pay during those periods.

Customers appearing in both prediction tables are prioritized first. The other two groups—customer-level only and school-level only—are retained and labeled separately rather than discarded.

## Three cohorts reveal which prediction view adds value

After the payment period, the three cohorts are evaluated separately:

| Cohort | Why retain it |
| --- | --- |
| Customer ∩ School | Both views agree; this group receives the highest deployment priority |
| Customer only | Measures the incremental value of customer-level history |
| School only | Measures the incremental value of school collection patterns |

For each cohort, evaluation can check four outcomes independently: whether a payment occurred inside the prediction window, whether the school was correct, how far the predicted payment period was from the actual period, and the error in predicted ticket size. A single “correct prediction” label would hide which part of the forecast failed.

Comparing the three cohorts over the same observation window shows which view contributes useful predictions. The comparison then informs changes for the next month or the next school year instead of allowing only the overlap group to survive without evidence.

## What this approach still cannot observe

The method depends on transaction history. A new customer with no previous school-fee payment may appear in neither prediction table. A customer changing schools can also break the historical customer–school relationship. Receiver-side coverage remains incomplete when a school uses another bank, even after beneficiary-name analysis.

This article describes the identification and evaluation design, not model performance. Time-series decomposition and its implementation remain outside its scope and will be covered in a separate technical article.

The central lesson is simple: first establish that a transaction is a school-fee payment, then forecast its timing and amount. Better forecasting cannot repair a mislabeled transaction set.
{% endcapture %}
<article class="reading-page" data-lang="en">{{ article_en | markdownify }}</article>

{% capture article_vi %}
🔙 [Quay lại trang chủ](/)

# Thanh toán học phí: nhận diện trước khi dự báo

Dự báo chưa phải bài toán đầu tiên. Trước khi ước tính khi nào khách hàng sẽ thanh toán học phí và số tiền là bao nhiêu, cần xác định giao dịch ngân hàng nào thực sự là học phí và, khi có thể, trường nào đã nhận khoản tiền đó. Nếu không, mô hình có thể tạo ra những dự báo trông rất chính xác nhưng lại dành cho sai giao dịch.

## Các use case cần nhiều hơn một nhãn học phí

Thanh toán học phí thường lặp lại quanh kỳ thu tiền riêng của từng trường, dù thời điểm và số tiền có thể thay đổi giữa các học kỳ. Sau khi được nhận diện, các khoản thanh toán này có thể hỗ trợ ba use case:

| Use case | Thông tin cần có | Cách sử dụng |
| --- | --- | --- |
| Unsecured lending | Thời điểm và số tiền thanh toán dự kiến (ticket size) | Ước tính một dòng tiền ra có tính chu kỳ |
| Khả năng tài chính | Số tiền học phí và tần suất thanh toán trong quá khứ | Dùng như một tín hiệu hỗ trợ, không phải kết luận độc lập về khả năng tài chính |
| Credit card | Các tháng tập trung thanh toán học phí | Chọn thời điểm chạy campaign theo mùa |

Vì vậy, chỉ có nhãn học phí là chưa đủ. Output hữu ích cần bốn trường: khách hàng, trường được nhận diện, kỳ thanh toán có khả năng xảy ra và số tiền dự kiến.

## Giao dịch lý tưởng xác định được cả hai phía

Trong trường hợp lý tưởng, cả hai phía của giao dịch đều được xác định:

- Người gửi: phụ huynh hoặc học sinh, sinh viên.
- Người nhận: trường học.

Khi biết được cả hai phía, mục đích thanh toán dễ xác định hơn nhiều. Tuy nhiên, trên thực tế ngân hàng thường nhìn rõ người gửi hơn người nhận.

![Giao dịch giữa khách hàng và trường học](images/1.png)

## Dữ liệu phía người nhận không đầy đủ khi trường dùng ngân hàng khác

Tại Việt Nam, các trường sử dụng tài khoản ở nhiều ngân hàng khác nhau, trong khi chỉ một phần nhỏ sử dụng tài khoản TCB. Khi khách hàng thanh toán cho trường ở ngân hàng khác, thông tin phía người nhận có trong dữ liệu nội bộ bị giới hạn. Vì vậy, chỉ dựa vào ID tài khoản nhận sẽ không thể xây dựng danh sách trường đầy đủ.

Tín hiệu định danh chính có thể sử dụng là beneficiary name, thường chứa tên trường. Tuy nhiên, tín hiệu này khá nhiễu:

- Beneficiary name không được chuẩn hóa.
- Tên viết tắt và các biến thể chính tả xuất hiện thường xuyên.
- Nhiều trường có tên giống hoặc gần giống nhau.

Ví dụ, tên đầy đủ `TRUONG TRUNG HOC PHO THONG <TEN>` có thể xuất hiện dưới dạng `THPT <TEN>` hoặc `TRUONG <TEN>`. Các biến thể này có thể chỉ cùng một trường, nhưng cùng một tên rút gọn cũng có thể thuộc nhiều trường khác nhau. Vì thế, đối chiếu theo tên người thụ hưởng có thể gán giao dịch vào sai trường hoặc nhận nhầm một giao dịch không phải học phí.

## Keyword tạo candidate; hành vi lặp lại dùng để xác thực

Quy trình nhận diện tách bước tạo candidate rộng khỏi bước xác thực chặt hơn:

1. Tạo candidate set có recall cao từ tên người thụ hưởng chứa keyword liên quan đến trường học. Danh sách có thể gồm `Truong`, `Tieu hoc`, `TH`, `Trung hoc`, `THCS`, `THPT`, `Dai hoc`, `DH`, `Mam non`, `Mau giao` và `Hoc phi`.
2. Phân tích các khách hàng liên quan đến từng candidate theo tần suất, số tiền và thời điểm thanh toán.
3. Kiểm tra tính nhất quán ở cấp khách hàng: cùng một khách hàng chuyển tiền đến cùng một trường qua nhiều tháng hoặc nhiều năm là bằng chứng mạnh hơn một giao dịch đơn lẻ.
4. Kiểm tra tính nhất quán ở cấp người nhận: số giao dịch, số khách hàng và mức độ tập trung quanh các kỳ thu tiền lặp lại giúp phân biệt trường học với một keyword trùng ngẫu nhiên.
5. Xử lý tên trường không rõ ràng và loại các false positive có khả năng cao.
6. Chốt tập giao dịch học phí, tổng hợp feature theo cả góc nhìn khách hàng và trường học, sau đó đưa vào feature mart.

Danh sách keyword chủ động ưu tiên recall; các kiểm tra hành vi cung cấp precision. Nếu coi keyword match là nhãn cuối cùng, hai nhiệm vụ này bị gộp làm một và false positive sẽ đi vào mọi phân tích phía sau.

## Bài toán dự báo có ba target riêng

Với 3–4 năm giao dịch đã được nhận diện, chúng tôi chuyển các khoản thanh toán hằng tháng của từng khách hàng thành time series. Dự báo cuối cùng dễ kiểm soát hơn khi được tách thành ba target:

1. **Có hay không:** khách hàng có khả năng phát sinh thanh toán học phí trong ba tháng tới không?
2. **Khi nào:** giao dịch có khả năng xuất hiện nhất vào tháng nào?
3. **Ở đâu và bao nhiêu:** trường nào từng xuất hiện trong lịch sử là người nhận có khả năng cao nhất, và ticket size dự kiến là bao nhiêu?

Time-series decomposition tách trend, seasonality và residual để hỗ trợ ước tính thời điểm và số tiền. Quan hệ trường–khách hàng trong quá khứ cung cấp candidate cho phía người nhận; không kỳ vọng một time-series model tự suy ra toàn bộ các target.

## Hai bảng dự báo cung cấp hai nguồn evidence độc lập

Quy trình tạo ra hai góc nhìn cho kỳ thanh toán tiếp theo:

- **Dự báo theo khách hàng:** với từng khách hàng, dự báo trường họ sẽ thanh toán, thời điểm và số tiền.
- **Dự báo theo trường:** với từng trường, xét những khách hàng từng thanh toán tại đó và dự báo ai có khả năng thanh toán trong kỳ thu tiền tiếp theo.

Góc nhìn theo trường dùng pattern thu tiền của trường thay vì coi mọi khách hàng là candidate. Nếu Trường A thường thu học phí vào tháng 1 và tháng 8, những khách hàng từng thanh toán cho Trường A sẽ có khả năng cao hơn trong các kỳ đó.

Khách hàng xuất hiện trong cả hai bảng dự báo được ưu tiên triển khai trước. Hai nhóm còn lại—chỉ xuất hiện trong bảng theo khách hàng và chỉ xuất hiện trong bảng theo trường—vẫn được giữ lại và đánh dấu riêng.

## Ba cohort cho biết góc nhìn nào thực sự tạo thêm giá trị

Sau kỳ thanh toán, ba cohort được đánh giá riêng:

| Cohort | Lý do giữ lại |
| --- | --- |
| Customer ∩ School | Hai góc nhìn đồng thuận; nhóm này được ưu tiên triển khai cao nhất |
| Customer only | Đo giá trị tăng thêm từ lịch sử cấp khách hàng |
| School only | Đo giá trị tăng thêm từ pattern thu tiền của trường |

Với từng cohort, có thể kiểm tra độc lập bốn outcome: giao dịch có xảy ra trong prediction window không, trường có đúng không, kỳ thanh toán dự báo lệch kỳ thực tế bao xa và ticket size dự báo sai bao nhiêu. Một nhãn “dự báo đúng” duy nhất sẽ che mất phần nào của dự báo đã thất bại.

So sánh ba cohort trên cùng observation window cho biết góc nhìn nào tạo ra dự báo hữu ích. Kết quả đó trở thành căn cứ cải tiến cho tháng tiếp theo hoặc năm học tiếp theo, thay vì chỉ giữ nhóm giao nhau mà không có bằng chứng.

## Những gì phương pháp này vẫn không quan sát được

Phương pháp phụ thuộc vào lịch sử giao dịch. Khách hàng mới chưa từng thanh toán học phí có thể không xuất hiện trong cả hai bảng dự báo. Việc khách hàng chuyển trường cũng có thể làm quan hệ khách hàng–trường trong quá khứ mất hiệu lực. Coverage phía người nhận vẫn không đầy đủ khi trường dùng ngân hàng khác, kể cả sau khi phân tích tên người thụ hưởng.

Bài này mô tả thiết kế nhận diện và đánh giá, không công bố model performance. Time-series decomposition và phần triển khai cụ thể nằm ngoài phạm vi bài và sẽ được trình bày trong một bài kỹ thuật riêng.

Nguyên tắc cốt lõi rất đơn giản: trước hết phải xác lập giao dịch thực sự là học phí, sau đó mới dự báo thời điểm và số tiền. Forecast tốt hơn không thể sửa một tập giao dịch bị gán nhãn sai.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
