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

Dự báo chưa phải bài toán đầu tiên. Trước khi ước tính khi nào khách hàng sẽ thanh toán học phí và số tiền là bao nhiêu, trước hết cần xác định giao dịch ngân hàng nào thực sự là học phí và, khi có thể, trường nào đã nhận khoản tiền đó.

## Các use case cần những thông tin gì?

Học phí là một trong những khoản chi tương đối đều đặn và có thể dự đoán của gia đình có con đi học. Sau khi được nhận diện, các khoản thanh toán này có thể hỗ trợ ba use case:

| Use case | Thông tin cần có | Cách sử dụng |
| --- | --- | --- |
| Unsecured lending | Thời điểm và số tiền thanh toán dự kiến (ticket size) | Ước tính một dòng tiền ra có tính chu kỳ |
| Khả năng tài chính | Số tiền học phí và tần suất thanh toán trong quá khứ | Dùng như một tín hiệu gián tiếp về khả năng tài chính |
| Credit card | Các tháng tập trung thanh toán học phí | Chọn thời điểm chạy campaign theo mùa |

Vì vậy, chỉ có nhãn school fee là chưa đủ. Output hữu ích cần cho biết khách hàng, trường được match, thời gian có khả năng thanh toán và số tiền dự kiến.

## Một giao dịch học phí lý tưởng có hình dạng như thế nào?

Trong trường hợp lý tưởng, cả hai phía của giao dịch đều được xác định:

- Người gửi: phụ huynh hoặc học sinh, sinh viên.
- Người nhận: trường học.

Khi biết được cả hai entity, mục đích giao dịch dễ xác định hơn nhiều.

![Giao dịch giữa khách hàng và trường học](images/1.png)

## Vì sao không thể chỉ nhận diện từ phía người nhận?

Tại Việt Nam, các trường sử dụng tài khoản ở nhiều ngân hàng khác nhau, trong khi chỉ một phần nhỏ sử dụng tài khoản TCB. Vì vậy, dữ liệu nội bộ phần lớn không có thông tin đầy đủ về trường ở phía người nhận; chỉ dựa vào receiver account sẽ không thể nhận diện học phí một cách đáng tin cậy.

Tín hiệu định danh chính có thể sử dụng là beneficiary name, thường chứa tên trường. Tuy nhiên, tín hiệu này khá nhiễu:

- Beneficiary name không được chuẩn hóa.
- Tên viết tắt và các biến thể chính tả xuất hiện thường xuyên.
- Nhiều trường có tên giống hoặc gần giống nhau.

Vì thế, matching theo beneficiary name có thể gán giao dịch vào sai trường hoặc nhận nhầm một giao dịch không phải học phí.

## Cách xây dựng tập giao dịch học phí

Quy trình nhận diện gồm:

1. Tạo candidate set từ beneficiary name chứa các keyword liên quan đến trường học như `Truong`, `Tieu hoc`, `Trung hoc` và `Dai hoc`.
2. Phân tích các khách hàng liên quan theo tần suất, số tiền và thời điểm thanh toán.
3. Lọc các trường hợp lệ dựa trên số giao dịch, số khách hàng và tính nhất quán của hoạt động thanh toán. Một tín hiệu consistency hữu ích là cùng một khách hàng chuyển tiền đến cùng một trường qua nhiều tháng hoặc nhiều năm.
4. Xử lý các tên trường không rõ ràng và loại những false positive có khả năng cao.
5. Chốt tập giao dịch học phí.
6. Tổng hợp feature theo cả góc nhìn khách hàng và trường học, sau đó đưa vào feature mart.

Bước preprocessing này quyết định giao dịch nào được đưa vào phân tích phía sau. Nếu tập giao dịch được nhận diện sai, mô hình forecast chỉ tạo ra những kết quả trông chính xác cho các khoản thanh toán không đúng.

## Chỉ phân tích time series sau khi đã nhận diện

Với 3–4 năm giao dịch đã được nhận diện, chúng tôi chuyển các khoản thanh toán hằng tháng của từng khách hàng thành một time series. Time-series decomposition tách chuỗi thành trend, seasonality và residual; các thành phần này được dùng để dự báo thanh toán trong ba tháng tiếp theo.

Chúng tôi đồng thời tạo bảng dự báo thứ hai ở cấp độ trường. Với mỗi trường, bảng này dự báo những phụ huynh có khả năng thanh toán dựa trên pattern thu tiền của trường. Nếu Trường A thường thu học phí vào tháng 1 và tháng 8, những khách hàng từng thanh toán cho Trường A được kỳ vọng sẽ đi theo lịch tương tự.

Như vậy có hai góc nhìn cho kỳ thanh toán tiếp theo:

- **Dự báo theo khách hàng:** với từng khách hàng, dự báo trường họ sẽ thanh toán, thời điểm và số tiền.
- **Dự báo theo trường:** với từng trường, dự báo những phụ huynh có khả năng thanh toán trong kỳ thu tiền.

Khách hàng xuất hiện trong cả hai bảng dự báo được ưu tiên triển khai trước. Hai nhóm còn lại—chỉ xuất hiện trong bảng theo khách hàng và chỉ xuất hiện trong bảng theo trường—vẫn được giữ lại và đánh dấu riêng.

Sau kỳ thanh toán, kết quả của ba nhóm được đo độc lập. So sánh nhóm giao nhau, nhóm customer-only và nhóm school-only cho biết method nào tạo ra dự báo hữu ích, từ đó cung cấp bằng chứng để cải tiến phương pháp cho tháng tiếp theo hoặc năm học tiếp theo.

(*) Time-series decomposition và các phương pháp liên quan sẽ được trình bày trong một bài kỹ thuật riêng.
{% endcapture %}
<article class="reading-page" data-lang="vi">{{ article_vi | markdownify }}</article>
