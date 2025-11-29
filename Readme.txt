📊 E-Commerce Customer Insights & Retention Dashboard

End-to-End Analytics Project — SQL (BigQuery) • Power BI • RFM Segmentation • Marketing ROI

This project simulates the analytics workflows used in modern e-commerce companies, turning raw transactional data into a complete retention, customer behavior, and marketing efficiency dashboard.

The goal is to help stakeholders understand:

Revenue trends over time

Customer retention & repeat behavior

Geographic and hourly purchasing patterns

Marketing ROI & ROAS performance by channel

Customer segmentation using RFM and strategic recommendations

🧠 Key Business Questions

How are revenue and orders trending over time?

What does customer retention and AOV look like between new vs repeat customers?

How do time, weekday, and geography influence purchasing?

Which marketing channels provide the strongest ROAS and ROI?

What are our main customer segments and how should we act on them?

🛠️ Tech Stack
Data Engineering & SQL

Google BigQuery

SQL for cleaning, transforming, and building analytical tables

Star-schema modelling (Fact Orders + Dimensions)

Analytics & Visualization

Power BI

DAX (segmentation metrics, interactive recommendations)

Customer Segmentation

RFM scoring

Dynamic segment KPIs

Segment-level recommendations based on actual metrics

🗂️ Project Structure
.
├── data/
│   ├── raw_orders.csv
│   ├── customers.csv
│   └── marketing_spend.csv
├── sql/
│   ├── rfm_scores.sql
│   ├── rfm_segments_clean.sql
│   ├── v_orders_enhanced_final.sql
│   ├── channel_map.sql
│   └── location_map.sql
├── dashboard/
│   ├── page1_revenue_orders_quarter.png
│   ├── page2_aov_retention_repeat_vs_onetime.png
│   ├── page3_time_and_location.png
│   ├── page4_marketing_roi_roas.png
│   ├── page5_rfm_overview_all_segments.png
│   └── page5_rfm_segment_drilldown_at_risk.png
└── README.md

📈 Dashboard Overview

Below is a walkthrough of each dashboard page with screenshot previews.

📌 Page 1 — Revenue & Orders Over Time

Insights delivered:

Total revenue by quarter

YOY seasonality patterns

High-level performance indicators (Revenue, AOV, Orders)

📷 Screenshot:


📌 Page 2 — AOV, Retention & Repeat Behavior

Insights delivered:

AOV trend between new vs repeat customers

Monthly repeat-rate trend

Clear visibility into customer lifetime patterns

📷 Screenshot:


📌 Page 3 — Time & Location Insights

Insights delivered:

Purchases per hour and weekday

Geographic breakdown by location

Peak demand windows for campaign timing

📷 Screenshot:


📌 Page 4 — Marketing Efficiency: ROI & ROAS

A bubble chart comparing:

ROI

ROAS

Marketing spend (bubble size)

Channel annotations

📷 Screenshot:


📌 Page 5 — RFM Segmentation & Strategic Actions
1️⃣ Overview of all segments (bar chart + KPIs)

Potential Loyal Customers

High Value Customers

Lost Customers

At-Risk Customers

New Customers

📷 Screenshot:


2️⃣ Drilldown by Segment (Dynamic Recommendations)

Each segment includes:

Average Recency

Average Frequency

Average Monetary

Revenue

AOV

Automatically generated strategic action (driven by DAX)

📷 Screenshot:


🧮 Data Modelling

The model follows a simple but robust star schema:

Fact Table

Fact Orders → built directly from raw.orders

Dimensions

Dim Customers (standardized from raw custom data)

Dim Customer RFM (from customer_rfm_segments_clean)

Dim Channels (from mapping table)

Dim Locations

RFM Pipeline

Compute recency, frequency, monetary → customer_rfm_scores

Assign R/F/M scores (1–5)

Map into segments via customer_rfm_segments_clean

Feed into Power BI for DAX-based insights

🎯 Key Quantitative Recommendations (Dynamic)

The dashboard generates segment-specific, data-driven actions such as:

At-Risk Customers:
Re-engage ~900 customers with avg. recency ~370 days.

High Value Customers:
Protect revenue by retaining ~1,000 high-spend customers.

Lost Customers:
Win-back offers to ~975 customers with nearly zero recent activity.

Potential Loyal:
Nurture ~1,768 customers close to becoming full loyalists.

These recommendations change dynamically based on the slicer.

🚀 Final Notes

This project demonstrates:

Full analytics lifecycle

Hands-on SQL & data modelling

Business-oriented dashboarding

Marketing & retention analytics

Clear quantitative recommendations

It is structured to match the expectations of Data Analyst hiring managers.

🙌 Contact

For questions or collaboration:
Francesco Marchì
(You can add email or LinkedIn here)