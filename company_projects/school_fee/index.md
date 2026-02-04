---
title: Modeling School Fee Payments as Time Series
---

🔙 [Back to Home](/)

## School fee

School fee payments are one of the most regular and predictable expenses for families with children.  
If we can correctly identify and model these payments from transaction data, it unlocks multiple financial use cases — from lending to customer profiling.

We can leverage this info to some use case:
- Unsecured lending: recurring annual payment → predictable cash outflow

- Financial ability: school fee amount + frequency → income proxy

- Credit card: seasonal spike → campaign timing


## Some barrier 

Identifying school fee transactions from banking data is not straightforward.
  
From transaction records, we can usually infer the transaction purpose only when both the sender and the receiver are known entities. In practice, this assumption does not hold well for school fee payments.  

![Customer transactions](1.png)


For school fees, the ideal case would be:

- Sender: parents or students

- Receiver: the school

However, in Viet Nam, most schools use bank accounts from various banks, while only a very small number of schools use TCB. As a result, receiver-side information about schools is largely missing from our internal data.  

This means we cannot reliably identify school fee transactions based on receiver accounts alone.

Instead, the only available signal is the beneficiary name, which often contains the school name. Unfortunately, this signal is noisy:

- Beneficiary names are not standardized

- Many schools share similar or identical names

- Spelling variations and abbreviations are common

Because of this, beneficiary name matching is not 100% accurate and can easily lead to mismatches.

As a consequence, a significant amount of preprocessing is required to:

- Filter out non-legitimate school transactions

- Resolve ambiguous school names

- Reduce false positives in school fee identification

## Clean data

To identify school fee transactions, we apply the following steps:

- Collect transactions whose beneficiary names contain the keyword “Truong” (school).

- Perform basic analysis on these customers across key dimensions (frequency, amount, timing).

- Filter legitimate schools using simple rules (number of transactions, number of customers, consistency).

- Finalize the list of school fee transactions.

- Aggregate features from both customer and school perspectives.

- Integrate the resulting features into the feature mart


## Time series

Despite these identification challenges, once a reliable set of school fee transactions is constructed, their time series characteristics reveal strong and useful patterns.     
After collecting 3–4 years of data, we restructure each customer’s monthly transactions into a time series.  
We then apply time series decomposition to separate trend, seasonality, and residual components, which are used to predict customer payments over the next three months. These predictions support the use cases described in the School Fee section.  

We also take an alternative, school-level approach.
For each school, we analyze seasonal payment patterns. For example, if School A typically collects fees in January and August, customers who have previously paid School A are expected to follow the same payment schedule.

(*) Time series decomposition and related methods will be covered in a separate technical blog.
