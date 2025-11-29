# 📊 E-Commerce Customer Insights & Retention Dashboard

**End-to-End Analytics Project — SQL (BigQuery) • Power BI • RFM Segmentation • Marketing ROI**

This project simulates the analytics workflows used in a modern e-commerce company, turning raw transactional data into a complete **retention, customer behavior, and marketing efficiency** dashboard.

The goal is to help stakeholders understand:

- Revenue trends over time  
- Customer retention & repeat behavior  
- Geographic and hourly purchasing patterns  
- Marketing ROI & ROAS performance by channel  
- Customer segmentation (RFM) and data-driven actions

---

## 🧠 Key Business Questions

1. **How are revenue and orders trending over time?**  
2. **What does customer retention and AOV look like between new vs repeat customers?**  
3. **How do time of day, weekday, and geography influence purchasing?**  
4. **Which marketing channels provide the strongest ROAS and ROI?**  
5. **What are our main customer segments and how should we act on them?**

---

## 🛠️ Tech Stack

### Data Engineering & SQL

- **Google BigQuery**  
- **SQL** for cleaning, transforming, and building analytical tables  
- **Star-schema modelling** (Fact Orders + Dimensions)

### Analytics & Visualization

- **Power BI**  
- **DAX** for segmentation metrics and interactive recommendations

### Customer Segmentation

- **RFM scoring** (Recency, Frequency, Monetary)  
- **Dynamic segment KPIs**  
- Segment-level recommendations based on actual metrics

---

## 🗂️ Project Structure

```text
.
├── assets/
│   └── screenshots/
│       ├── page1_revenue_orders_quarter.png
│       ├── page2_aov_retention_repeat_vs_onetime.png
│       ├── page3_time_and_location.png
│       ├── page4_marketing_roi_roas.png
│       ├── page5_rfm_overview_all_segments.png
│       └── page5_rfm_segment_drilldown_at_risk.png
├── data/
│   └── ...  # cleaned / helper datasets
├── powerbi/
│   └── Ecommerce_RFM_Customer_Analytics.pbix
├── orders_realistic_FINAL.csv
└── README.md

```


(BigQuery SQL is managed directly in the warehouse; key transformation logic is described in the Data Modelling section.)

📈 Dashboard Overview
Below is a walkthrough of each dashboard page with screenshot previews.

📌 Page 1 — Revenue & Orders Over Time


Insights delivered

Total revenue by quarter

YOY seasonality patterns

High-level performance indicators (Revenue, AOV, Orders)

📌 Page 2 — AOV, Retention & Repeat Behavior


Insights delivered

AOV trend split by new vs repeat customers

Monthly repeat-rate trend

Clear visibility into customer lifetime behavior

📌 Page 3 — Time & Location Insights


Insights delivered

Purchases per hour of day and weekday

Geographic breakdown by location

Identification of peak demand windows for campaign timing

📌 Page 4 — Marketing Efficiency: ROI & ROAS


Visual

Bubble chart by marketing channel:

X-axis: ROAS

Y-axis: ROI

Bubble size: Marketing spend

Clear annotations for:

Referral (best)

Paid Search (underperforming)

Email / Social (solid mid-performers)

This view makes it easy to see where to scale, optimize, or cut spend.

📌 Page 5 — RFM Segmentation & Strategic Actions
1️⃣ Overview of all segments (bar chart + KPIs)


Segments:

Potential Loyal Customers

High Value Customers

Lost Customers

At-Risk Customers

New Customers

The bar chart shows customer count per segment, supported by cards with segment-level metrics.

2️⃣ Drilldown by Segment (Dynamic Recommendations)


For the selected segment, the dashboard displays:

Average Recency

Average Frequency

Average Monetary value

Segment Revenue

Segment AOV

An automatically generated strategic action (driven by DAX), e.g.:

“Re-engage about 900 inactive customers (avg recency ~370 days).”

🧮 Data Modelling
The model follows a simple but robust star schema.

Fact Table
Fact Orders

Built directly from raw.orders (backed by orders_realistic_FINAL.csv)

One row per order with customer, channel, date, and financials

Dimensions
Dim Customers

Standardized from customer raw data (cleaned IDs, channels, locations)

Dim Customer RFM

Based on customer_rfm_segments_clean / customer_rfm_segments_v2

Includes:

customer_id

recency_days, frequency, monetary

r_score, f_score, m_score

segment_group (High Value, At-Risk, etc.)

Dim Channels

From a mapping table to ensure consistent channel names across marketing + orders

Dim Locations

Region / city standardization for geographic analysis

RFM Pipeline (BigQuery)
Compute RFM base metrics

Recency (days since last order)

Frequency (number of orders)

Monetary (total spend)

Assign R/F/M scores (1–5)

Using quantiles / business rules

Map into RFM segments

customer_rfm_segments_clean table encodes segment logic

Example segments: High Value, Potential Loyal, At-Risk, Lost, New

Load into Power BI

Used to drive all segment cards, tables, and recommendations

🎯 Key Quantitative Recommendations (Dynamic)
The dashboard generates segment-specific, data-driven actions such as:

At-Risk Customers
→ Re-engage ~900 customers with average recency ~370 days.

High Value Customers
→ Protect revenue by retaining ~1,000 high-spend customers.

Lost Customers
→ Launch win-back offers to ~975 customers with almost zero recent activity.

Potential Loyal Customers
→ Nurture ~1,768 customers who are close to becoming fully loyal.

These numbers are not hard-coded: they update dynamically based on the selected segment and current data.

🚀 Final Notes
This project demonstrates:

The full analytics lifecycle: from raw CSVs → SQL transformations → semantic model → dashboards

Hands-on SQL and data modelling in BigQuery

Business-oriented Power BI dashboards with clear storytelling

Marketing & retention analytics grounded in RFM and ROI/ROAS

Concrete, quantitative recommendations instead of just charts

It is structured to match the expectations of Data Analyst and Business Analyst hiring managers.

🙎‍♂️ Contact
For questions or collaboration:

Name: Francesco Marchì

Email: marchi.frncsc@gmail.com

LinkedIn: https://www.linkedin.com/in/francesco-march%C3%AC-115657205/