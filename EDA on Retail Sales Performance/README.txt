# 🛍️ EDA on Retail Sales Performance

## 📌 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on a retail sales dataset (Superstore Dataset).  
The goal is to uncover patterns, relationships, and business insights that can help improve **sales strategy**, **profitability**, and **customer segmentation**.

---

## 🎯 Objectives
- Analyze sales and profit trends across regions, categories, and time periods.
- Identify high-performing and underperforming products or segments.
- Explore how discounts affect profit margins.
- Detect outliers, missing values, and data inconsistencies.
- Present actionable business insights through data visualization.

---

## 🧠 Key Insights (Highlights)
1️⃣ **Sales Trend:** Monthly sales show a consistent upward trend with peaks during November–December (holiday season).  
2️⃣ **Category Analysis:** Technology products generate the highest profit margins.  
3️⃣ **Regional Performance:** The West region contributes maximum revenue, while the East region needs improvement.  
4️⃣ **Discount Impact:** Higher discounts (>30%) tend to reduce overall profit.  
5️⃣ **Customer Segments:** Consumer segment dominates the order count and sales volume.

---

## 🧹 Data Cleaning Performed
- Removed duplicate records.  
- Handled missing values (if any).  
- Converted date columns to proper datetime format.  
- Created new features like `Order Month`.  
- Exported cleaned dataset to `outputs/cleaned_data.csv`.

---

## 📊 Exploratory Data Analysis
EDA was performed using:
- **Univariate Analysis** → Histograms, boxplots for Sales, Profit, Discount.  
- **Bivariate Analysis** → Correlation between Sales & Profit, Discount & Profit.  
- **Category-wise Analysis** → Bar plots for Category vs Sales/Profit.  
- **Regional Analysis** → Region vs Sales performance.  
- **Time Series Analysis** → Monthly Sales Trend line chart.

---

## 🧩 Tools & Libraries Used
| Category | Libraries |
|-----------|------------|
| Data Handling | pandas, numpy |
| Visualization | matplotlib, seaborn, plotly |
| Environment | Python 3.x, Jupyter Notebook |

---

## 📁 Project Structure
