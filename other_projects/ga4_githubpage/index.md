---
title: GA4 - Google Analytics 4
---

🔙 [Back to Home](/)

## Introduction

Date: 2026-01-26
Link reference: https://support.google.com/analytics/answer/10089681?hl=vi&ref_topic=14089939&sjid=5418224013262677673-NC

Since July 1, 2023, Universal Analytics has stopped processing new data, making GA4 the default choice for Google Analytics users.

GA4 is not a simple upgrade. It changes how user behavior is measured, which can be confusing for those familiar with UA.

This post is a short introduction to GA4 and the starting point of a series documenting how I learn and use it in practice.

1. Course learn to use GA4 

https://skillshop.docebosaas.com/learn/courses/8108/get-started-using-google-analytics/lessons/24354:8107/welcome-to-the-course-html-page 

![funnel](images/1.png)

acquisition: what marketing channel bring customer

engagement: what content users engage with and share with others

monetization & retention: how many user become customers and how often they return website

2. What changed from Universal Analytics to GA4?

The key change is simple: GA4 measures events, not sessions.

Universal Analytics was built around sessions and pageviews.
GA4 treats every user interaction — page views, clicks, scrolls, conversions — as an event.

This shift allows GA4 to better track user behavior across devices and platforms, but it also means most UA metrics and reports no longer apply.

Understanding this mindset change is more important than learning any specific GA4 report.

3. What is GA4, at a high level?

GA4 is an event-based analytics system designed to track how users interact across websites and apps.

Instead of focusing on pageviews and sessions, GA4 focuses on user actions and their journey over time. This makes it more flexible for modern products, where users move across devices, platforms, and touchpoints.

Think of GA4 less as a reporting tool, and more as a behavior tracking framework.


4. Setup GA4
GA4 setup is relatively straightforward: create a property, add the tracking tag, and verify data collection.

I won’t cover the setup steps in detail here, since this post focuses on how GA4 works conceptually. A dedicated setup guide will follow in a separate post. [Setup guide](./setup.md)
