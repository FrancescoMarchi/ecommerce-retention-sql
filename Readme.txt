# E-commerce Retention & Marketing Efficiency  
_SQL + BigQuery + Power BI portfolio case study_

---

## 1. Project Overview

This project simulates the analytics stack of a mid-size e-commerce company that wants to **grow revenue by improving customer retention and marketing efficiency**.

> 🔒 **Data note**  
> All data is **synthetic** and generated for learning/portfolio purposes.  
> No real customers, orders, or marketing platforms are involved.  
> The goal is to mirror realistic patterns and decisions, not to expose real business data.

### Core Business Questions

1. **Revenue & Growth**
   - How are **revenue, orders, and profit** evolving over time?
   - Which quarters are best and worst, and by how much?

2. **Customer Behaviour**
   - How does **Average Order Value (AOV)** move over time?
   - What’s the **split between repeat and one-time customers**?
   - How is our **customer retention rate** trending?

3. **When & Where Customers Buy**
   - At what **time of day** do customers buy the most?
   - Which **days of the week** are strongest?
   - Which **locations** generate the most orders?

4. **Marketing Efficiency**
   - Which **channel** gives the best balance of **ROI**, **ROAS** and **spend scale**?

5. **Customer Segmentation (RFM)**
   - How many **New**, **High-Value**, **At-Risk**, and **Lost** customers do we have?
   - What are their **typical behaviours** (recency, frequency, monetary)?
   - How should we **prioritise actions** by segment?

---

## 2. Tech Stack

- **Data Warehouse:** Google BigQuery  
- **Query Language:** SQL (CTEs, views, window functions)  
- **Analytics / BI:** Power BI  
- **Other:** RFM segmentation logic, synthetic data generation

---

## 3. Data Model

The final model in Power BI follows a **star-schema** pattern:

**Fact tables**

- `Fact Orders`  
  - one row per order  
  - key fields: `order_id`, `customer_id`, `order_date`, `channel`, `location`  
  - metrics: `net_revenue`, `margin_pct`, `profit`, `order_hour`, `order_day_name`, …

- `Fact Marketing Spend`  
  - one row per **channel x month**  
  - fields: `month`, `channel`, `spend_usd`

- `Fact Customer RFM`  
  - one row per customer with behaviour features  
  - fields: `customer_id`, `recency_days`, `frequency`, `monetary`, `r_score`, `f_score`, `m_score`, `segment_group`

**Dimension tables**

- `Dim Customers` – customer master data  
- `Dim Date` – calendar, year/quarter/month/day, used for all time-based analysis  
- `Dim Channel` – marketing / acquisition channel  
- `Dim Customer Types` / `Dim Customer RFM` – category labels for segments

Relationships are **one-to-many** from dimensions into the fact tables to keep filters controlled and calculations stable.

---

## 4. Key Metrics

**Sales & Profitability**

- **Total Revenue** – sum of net order revenue  
- **Total Orders** – count of orders  
- **Total Profit (channel-level)** – revenue minus marketing spend (when relevant)  
- **AOV (Average Order Value)** – revenue ÷ orders

**Customer Metrics**

- **Repeat vs One-Time Customers** – based on purchase count  
- **Customer Retention Rate (quarterly)** – returning customers ÷ customers from previous quarter  
- **RFM Scores** – recency, frequency, monetary scores from 1–5  
- **RFM Segment Group** – New, Potential Loyal, High Value, At-Risk, Lost

**Marketing Efficiency**

- **ROI** – (incremental profit – spend) ÷ spend  
- **ROAS** – revenue ÷ spend  
- **Bubble size** – spend volume per channel

---

## 5. Dashboard Tour

The solution is delivered as a **5-page Power BI report**.  
Below, each page has a short description and a screenshot placeholder.

---

### Page 1 – Revenue & Orders Overview

**Purpose:** Give leadership a quick sense of overall business performance and seasonality.

**Key visuals**

- **Combo chart**:  
  - Bars = **Total Revenue** by `Year-Quarter`  
  - Line = **Total Orders**  
- **KPI cards**:  
  - Total Revenue  
  - Total Orders  
  - Total Profit  
- **Best / Worst Quarter cards**:  
  - Show the **top** and **bottom** quarters by revenue, with the quarter label and value.

**Screenshot**

![Page 1 – Revenue and Orders by Quarter](screenshots/page1_revenue_orders_quarter.png)

---

### Page 2 – Customer Value & Retention

**Purpose:** Understand if we’re monetising the customer base well and keeping them.

**Key visuals**

- **AOV over time** (line chart) – Are customers spending more or less per order?  
- **Repeat vs One-Time customers** (horizontal bar) – Size of loyal base vs new/single buyers.  
- **Quarterly retention rate** (line chart) – % of customers returning from previous quarter.

**Screenshot**

![Page 2 – AOV, Repeat vs One-Time, Retention](screenshots/page2_aov_retention_repeat_vs_onetime.png)

**Example insight**

> AOV is relatively stable with seasonal spikes, repeat customers form a slightly larger group than one-time buyers, and retention hovers around ~21–23%, leaving room for improvement via lifecycle campaigns.

---

### Page 3 – When & Where Customers Buy

**Purpose:** Help operations and marketing understand **timing** and **geography** of demand.

**Key visuals**

- **Orders by hour of day** (line chart) – reveals clear **evening peaks**, helpful for staffing, delivery windows, and campaign timing.  
- **Orders by day of week** (column chart) – small but meaningful differences between weekdays and weekend.  
- **Total orders by location** (horizontal bar) – compares **HCMC, Hanoi, Taipei, Danang**.

**Screenshot**

![Page 3 – Orders by Time and Location](screenshots/page3_time_and_location.png)

---

### Page 4 – Marketing Efficiency (ROI vs ROAS)

**Purpose:** Explain which channels are pulling their weight once spend is considered.

**Key visual**

- **Scatter / bubble chart: “Marketing Efficiency: ROI vs ROAS by Channel”**  
  - X-axis: **ROAS**  
  - Y-axis: **ROI**  
  - Bubble size: **Marketing spend**  
  - Colour / label: **Channel** (email, organic, paid_search, referral, social)

Interpretation example:

- **Referral** – high ROI and ROAS, smaller bubble ⇒ highly efficient but limited scale.  
- **Email & Social** – decent ROI/ROAS at medium scale ⇒ good evergreen channels.  
- **Paid Search** – large bubble but lower ROI ⇒ growth lever that needs optimisation.

**Screenshot**

![Page 4 – ROI vs ROAS by Channel](screenshots/page4_marketing_roi_roas.png)

---

### Page 5 – RFM Segmentation & Drilldown

**Purpose:** Turn the customer base into **actionable segments** and quantify the opportunity in each.

This page is **interactive** and supports two modes:

#### 5.1 Segment Overview (All Segments Selected)

When the slicer is set to **“All”**, the page answers:

- How many customers are in each **RFM segment**?  
- How are **r_score vs f_score** distributed across the base?  
- What are the overall averages for **recency, frequency, monetary value, and revenue?**

**Key visuals**

- **RFM Segment Distribution** (horizontal bar) – counts by segment:  
  - New Customers  
  - Potential Loyal Customers  
  - High Value Customers  
  - At-Risk Customers  
  - Lost Customers  
- **R/F heatmap matrix** – `r_score` on rows, `F1/F3/F4/F5` on columns (frequency scores), highlighting concentration of behaviour.  
- **KPI cards** – For the currently selected segment(s):  
  - Segment Customers  
  - Segment Avg Recency  
  - Segment Avg Frequency  
  - Segment Avg Monetary  
  - Segment Revenue  
  - Segment AOV

**Screenshot (All segments)**

![Page 5 – RFM Overview (All Segments)](screenshots/page5_rfm_overview_all_segments.png)

---

#### 5.2 Segment Drilldown (Single Segment Selected)

When the user chooses a specific segment (e.g. **At-Risk Customers**) from the slicer:

- All cards update to show **segment-level metrics** only.  
- The R/F heatmap shrinks to show only the **relevant score combinations**.  
- The **segment description** changes dynamically to provide **plain-language guidance**.

**Example: At-Risk Customers**

- **Headline:** `AT-RISK CUSTOMERS — SAVE PRIORITY`  
- **Description:**  
  Customers whose activity is dropping. Use reminders, targeted offers and re-engagement campaigns.

This pattern is repeated for each segment, e.g.:

- **High Value Customers** – protect & reward  
- **Potential Loyal Customers** – nurture into VIPs  
- **Lost Customers** – win-back campaigns  
- **New Customers** – strong onboarding & first-90-days experience

**Screenshot (Segment selected)**

![Page 5 – At-Risk Segment Drilldown](screenshots/page5_rfm_segment_drilldown_at_risk.png)

---

## 6. Business Insights (Examples)

Because this is synthetic data, the numbers are illustrative, but the **type of insight** is realistic.

1. **Revenue & Volume**
   - Total revenue ≈ **$3M**, ~**13K orders** over the 3-year period.
   - Clear **quarter-to-quarter variation** with identifiable best and worst quarters.

2. **Customer Value & Loyalty**
   - A meaningful share of the base is **repeat customers**, supporting retention-driven growth.  
   - **Retention rate around low-20%** suggests room for improvement via lifecycle programs.

3. **Timing & Geography**
   - **Evening hours** are the key purchase window ⇒ ideal time for campaigns and onsite promotions.  
   - **HCMC** leads in order volume, followed by **Hanoi**, with **Taipei** and **Danang** smaller but meaningful markets.

4. **Marketing Efficiency**
   - **Referral** shows strong ROI/ROAS but limited spend ⇒ opportunity to scale if quality remains high.  
   - **Paid Search** is expensive and less efficient ⇒ candidate for optimisation and tighter keyword strategy.

5. **RFM Segmentation**
   - Large **Potential Loyal** and **High Value** groups ⇒ strong base for VIP programs and personalised experiences.  
   - Almost **1K Lost Customers** and **~950 At-Risk** ⇒ concrete pools for win-back and save campaigns.  
   - The heatmap shows **where recency/frequency are weakest**, guiding which score combinations to prioritise.

---

## 7. Repository Structure (Suggested)

```text
.
├── sql/
│   ├── 01_create_base_tables.sql
│   ├── 02_create_clean_views.sql
│   ├── 03_marketing_spend_views.sql
│   ├── 04_rfm_scoring.sql
│   └── 05_rfm_segments_final.sql
├── powerbi/
│   └── ecommerce_retention_marketing.pbix
├── screenshots/
│   ├── page1_revenue_orders_quarter.png
│   ├── page2_aov_retention_repeat_vs_onetime.png
│   ├── page3_time_and_location.png
│   ├── page4_marketing_roi_roas.png
│   ├── page5_rfm_overview_all_segments.png
│   └── page5_rfm_segment_drilldown_at_risk.png
└── README.md

## 8. How to Reproduce

Load data into BigQuery

Create a dataset (e.g. ecommerce_retention_sql).

Run the scripts in sql/ in order:

base tables

cleaned / enhanced views

marketing spend

RFM scoring and segment assignment

Connect Power BI to BigQuery

Use the BigQuery connector in Power BI.

Import the views created in step 1
(e.g. v_orders_final, v_marketing_spend, customer_rfm_segments_final, dim_date, dim_channel, etc.).

Open the Power BI report

Open powerbi/ecommerce_retention_marketing.pbix.

Refresh all; check that totals and counts match the SQL queries.

Explore the dashboards

Page 1–4: high-level performance and marketing efficiency.

Page 5: play with the RFM segment slicer and read the dynamic segment descriptions.

## 9. Possible Extensions

If this were a real production project, next steps could include:

Adding cohort analysis (1st purchase cohort vs retention and revenue).

Building lifetime value (LTV) models per channel or segment.

Integrating real marketing platform exports (Meta, Google Ads, email tools).

Deploying the SQL logic as scheduled BigQuery jobs with dbt or similar.

Publishing the Power BI report to the Power BI Service with row-level security for different teams.

## 10. Contact

If you’d like to discuss the project, the data model, or how this could be adapted to a real business, feel free to connect.