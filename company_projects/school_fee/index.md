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

Forecasting is not the first problem. Before estimating when a customer will pay school fees and how much, we first need to identify which bank transactions are actually school-fee payments and, when possible, which school received them.

## What the use cases need

School fees are among the more regular and predictable expenses for families with children. Once identified, these payments can support three use cases:

| Use case | Information required | How it is used |
| --- | --- | --- |
| Unsecured lending | Expected payment time and amount (ticket size) | Estimate a recurring cash outflow |
| Financial capacity | Historical fee amount and payment frequency | Use as an indirect signal of financial capacity |
| Credit card | Months in which school-fee payments concentrate | Time seasonal campaigns |

A school-fee label alone is therefore not enough. The useful output needs the customer, the matched school, the likely payment period, and the expected amount.

## What a school-fee transaction should look like

In the ideal case, both sides of the transaction are known:

- Sender: a parent or student
- Receiver: the school

With both entities identified, the transaction purpose is much easier to infer.

![Customer transactions](images/1.png)

## Why receiver-side identification breaks down

In Viet Nam, schools use accounts from many different banks, while only a small number use TCB accounts. Receiver-side school information is therefore largely missing from our internal data, so receiver accounts alone cannot reliably identify school-fee payments.

The main usable identity signal is the beneficiary name, which often contains the school name. This signal is noisy:

- Beneficiary names are not standardized.
- Spelling variations and abbreviations are common.
- Different schools may have similar or identical names.

Beneficiary-name matching can therefore assign a transaction to the wrong school or classify a non-school transaction as a school-fee payment.

## How we construct the school-fee transaction set

The identification process is:

1. Create a candidate set from beneficiary names containing school-related keywords such as `Truong`, `Tieu hoc`, `Trung hoc`, and `Dai hoc`.
2. Analyze the related customers across payment frequency, amount, and timing.
3. Filter legitimate schools using the number of transactions, number of customers, and payment consistency. One useful consistency signal is the same customer transferring money to the same school across multiple months or years.
4. Resolve ambiguous school names and remove likely false positives.
5. Finalize the school-fee transaction set.
6. Aggregate features from both the customer and school perspectives, then integrate them into the feature mart.

This preprocessing step determines which transactions enter the later analysis. Forecasting a poorly identified transaction set would only produce precise-looking results for the wrong payments.

## Apply time-series analysis after identification

With 3–4 years of identified transactions, we restructure each customer's monthly payments into a time series. Time-series decomposition separates the trend, seasonality, and residual components, which are then used to predict payments over the next three months.

We produce a second prediction table at the school level. For each school, it predicts which parents are likely to pay based on the school's collection pattern. If School A usually collects fees in January and August, customers who previously paid School A are expected to follow a similar schedule.

This produces two views of the next payment period:

- **Customer-level prediction:** for each customer, predict the school they will pay, the payment time, and the amount.
- **School-level prediction:** for each school, predict the parents who are likely to pay during its collection period.

Customers appearing in both prediction tables are prioritized first. The other two groups—customer-level only and school-level only—are retained and labeled separately rather than discarded.

After the payment period, we measure the outcome of each group separately. Comparing the overlap, customer-only, and school-only groups shows which method contributes useful predictions and provides evidence for improving the method in the next month or the next school year.

(*) Time-series decomposition and related methods will be covered in a separate technical article.
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
