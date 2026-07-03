# 📈 End-to-End Sales Forecasting & Demand Intelligence System

## 📌 Project Overview
This project is an end-to-end Sales Forecasting and Demand Intelligence System developed using the Superstore Sales Dataset. It analyzes historical sales trends, forecasts future demand using multiple time series models, detects anomalies in sales, segments products based on demand patterns, and provides an interactive Streamlit dashboard for business decision-making.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA)
- Analyze time series trends and seasonality
- Forecast sales using multiple models
- Compare forecasting models
- Detect sales anomalies
- Segment products using clustering
- Build an interactive Streamlit dashboard

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Statsmodels
- Prophet
- XGBoost
- Scikit-learn
- Streamlit

---

## 📂 Project Structure

```
sales-forecasting-dashboard/
│
├── analysis.ipynb
├── app.py
├── train.csv
├── requirements.txt
├── summary.pdf
├── README.md
├── charts/
│   ├── monthly_sales.png
│   ├── forecast.png
│   ├── anomalies.png
│   └── clusters.png
└── models/
    └── best_model.pkl
```

---

## 📊 Features

- Sales Trend Analysis
- Monthly & Yearly Sales Visualization
- Time Series Decomposition
- SARIMA Forecasting
- Facebook Prophet Forecasting
- XGBoost Forecasting
- Model Performance Comparison
- Isolation Forest Anomaly Detection
- Z-Score Anomaly Detection
- Product Demand Segmentation (K-Means)
- Interactive Streamlit Dashboard

---

## 📈 Dashboard Pages

### 📊 Sales Overview
- Total Sales
- Monthly Sales Trend
- Sales by Category
- Sales by Region

### 📈 Forecast Explorer
- Select Category or Region
- 1–3 Month Forecast
- Forecast Visualization
- MAE & RMSE Metrics

### ⚠️ Anomaly Report
- Sales Anomaly Detection
- Weekly Anomaly Table

### 📦 Demand Segmentation
- K-Means Cluster Visualization
- Product Cluster Details

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/sales-forecasting-dashboard.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📁 Dataset

- Superstore Sales Dataset (train.csv)
- Source: Kaggle

---

## 📊 Forecasting Models

- SARIMA
- Facebook Prophet
- XGBoost Regressor

---

## 📌 Evaluation Metrics

- MAE
- RMSE
- MAPE

---

## 👨‍💻 Author

**Manish Kumar**

MCA | Data Analyst | AI & Machine Learning Enthusiast

---

## 📄 License

This project is developed for educational and internship purposes.
