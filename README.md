# 📱 PhonePe Transaction Analytics Dashboard - 2024

![Dashboard Preview]<img width="1707" height="863" alt="Phonepe Dashboard" src="https://github.com/user-attachments/assets/0ecada95-83c1-4535-a5b9-184fba840227" />


> A complete end-to-end data analytics project analyzing **300,000 PhonePe transactions** across 6 cities, 4 product lines, and 3 payment methods for the year 2024.

---

## 📊 Project Overview

This project simulates and analyzes a real-world fintech transaction dataset inspired by PhonePe - one of India's leading digital payment platforms. The goal is to uncover patterns in transaction success, failure reasons, city-level performance, and product reliability using Python for data generation and Tableau for visualization.

---

## 🔢 Key Metrics at a Glance

| Metric | Value |
|---|---|
| Total Transactions | 3,00,000 |
| Total Volume | ₹245 Crore |
| Success Rate | 81.1% |
| Failure Rate | 14.1% |
| Pending Rate | 4.8% |
| Avg. Transaction Value | ₹8,161 |

---

## 📁 Project Files

| File | Description |
|---|---|
| `01_Phonepe.py` | Python script to generate the synthetic dataset (300,000 rows) |
| `phonepe_dataset.csv` | Generated dataset *(create by running the Python script)* |
| `PhonePe_Dashboard.twbx` | Tableau workbook with the interactive dashboard |
| `Phonepe_Dashboard.jpg` | Dashboard screenshot/preview |
| `PhonePe_Analytics_Presentation.pdf` | Full analytical presentation with findings & recommendations |

---

## 🛠️ Tools & Technologies

- **Python** - Data generation (`pandas`, `numpy`, `random`, `datetime`)
- **Tableau** - Interactive dashboard & visualizations
- **Excel / CSV** - Data storage format

---

## 🚀 How to Run

### Step 1 — Generate the Dataset
```bash
pip install pandas numpy
python 01_Phonepe.py
```
This will create `phonepe_dataset.csv` with 300,000 rows of transaction data.

### Step 2 — Open the Tableau Dashboard
- Open `PhonePe_Dashboard.twbx` in **Tableau Desktop** or **Tableau Public**
- Connect it to the generated `phonepe_dataset.csv` if prompted
- Use the Month, Product Type, and Location filters to explore the data

---

## 📌 Dataset Columns

| Column | Description |
|---|---|
| `Transaction_ID` | Unique transaction identifier |
| `User_ID` | Anonymized user ID |
| `Date` | Transaction date (Jan-Dec 2024) |
| `Time` | Transaction time (HH:MM:SS) |
| `Product_Type` | Money Transfer / Loan / Insurance / Bill Payment |
| `Amount` | Transaction amount in ₹ |
| `Payment_Method` | UPI / Bank Transfer / Wallet |
| `Status` | Success / Failed / Pending |
| `Failure_Reason` | Bank Denied / Wrong PIN / Network Down / Insufficient Balance / Time Out |
| `Location` | Delhi / Mumbai / Pune / Bangalore / Chennai / Hyderabad |

---

## 🔍 Key Findings

1. **Bill Payment leads** with an 88.4% success rate - nearly 10% better than all other products.
2. **Money Transfer lags** at 78.5% success despite driving the highest transaction volume (avg ₹25,108 per txn).
3. **All 5 failure reasons are equally distributed** (~20% each) - no single bottleneck dominates.
4. **No growth trend in 2024** - monthly volume flat between 23,830-25,480 transactions, a red flag for a fintech platform.
5. **Hyderabad has the highest failure rate** (14.3%) vs Pune (13.8%), suggesting regional infrastructure or banking partnership issues.
6. **Payment method does NOT affect success rate** - all methods (UPI, Bank Transfer, Wallet) perform at ~81.1%.

---

## 💡 Recommendations

1. **Fix Money Transfer reliability** - Apply Bill Payment's pre-auth balance checks and smarter retry logic.
2. **Address all 5 failure reasons systematically** - Add in-app balance nudges, network fallback routing, and better PIN error recovery flows.
3. **Audit Hyderabad & Bangalore** - Investigate local bank partnership SLAs and network infrastructure.
4. **Launch user acquisition strategy** - Explore new city expansion, referral programs, and cashback campaigns to restore organic growth.

---

## 📷 Dashboard Preview

The Tableau dashboard includes:
- KPI cards (Total Transactions, Volume, Success Rate, Failure Rate, Avg Value)
- Product Type Performance table & bar chart
- Monthly Transaction Trend line chart
- Transaction Status split (pie chart)
- City-wise Performance table & bar chart
- Interactive filters by Month, Product Type, and Location

---

## 👩‍💻 Author

**Vaishali Parmar**  
Data Analyst | Python • SQL • Tableau  

---

## 📄 License

This project is for educational and portfolio purposes only. The dataset is synthetically generated and does not represent real PhonePe transaction data.
