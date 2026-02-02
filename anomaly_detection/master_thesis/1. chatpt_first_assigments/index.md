## Anomaly detection

**My master thesis is "Method of applied different algorithms on multidimension data"**

🔙 [Back to Home](/)

## Chat GPT ask me:

### Step 1 – Define the Project Scope (Mandatory)

Write down clear answers to the following three questions:

1. What is your primary data type?  

Choose one main type first:  

Multivariate tabular data  

Multivariate time-series data  

Recommendation: start with tabular data, then extend to time series later if time allows.  

2. How many anomaly detection models will you implement?  

Do not be over-ambitious.

Recommended for a Master’s thesis:

Isolation Forest

Autoencoder

(+ LOF or One-Class SVM only if time permits)

2 models = solid
3 models = very good
More than 3 = unnecessary risk

3. What is the basis of your Root Cause Analysis (RCA)?

You must be able to express this in one clear sentence.

Examples:

“RCA is based on feature contribution analysis.”

“RCA is based on reconstruction error from Autoencoders.”

❌ Avoid vague answers such as “general RCA” or “multiple methods”.

## My answer  

1. What is your primary data type?  
- For MVP1, I will choose multivariate tabular data  

2. How many anomaly detection models will you implement?
I think 3:
- Isolation forest  
- LOF  
- Autoencoder  

3. What is the basis of your Root Cause Analysis (RCA)?  
Cannot answer right now, I need to read more documents.  


### Task 2 – Pipeline Definition (Required)
The pipeline of this project (as now):
- Data input
- Data preprocessing
- Anomaly detection algorithms
- Root cause analysis
- Evaluation
- Visualization

### Task 3 – First Coding Milestone (Required)

Implement a minimal end-to-end pipeline with:

One dataset loader

One preprocessing step (scaling only)

One anomaly detector (only one model)

One script that runs everything once

No ensembles. No advanced RCA. No tuning.  