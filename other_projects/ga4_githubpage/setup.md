---
title: GA4 - Google Analytics 4
---

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