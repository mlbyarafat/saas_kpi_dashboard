
# 📊 SaaS KPI Dashboard

This project is a lightweight and smart **KPI Monitoring Dashboard** for SaaS applications that supports **anomaly detection**, **time series forecasting**, and **visual analytics** using the Netflix dataset.

---

## 🚀 Problem Statement

SaaS companies need constant insights into user activity, content trends, or system KPIs to prevent churn, discover opportunities, and alert on anomalies. Most available dashboards either lack intelligence or are cost-prohibitive.

This project demonstrates:
- ✅ Forecasting trends using ARIMA models
- 🚨 Detecting unusual behavior in time-series metrics
- 📈 Visual-ready dataset from Netflix titles for prototyping

---

## 🧩 Features

- 🔮 **Time Series Forecasting** with ARIMA
- 🚨 **Anomaly Detection** in usage/data trends
- 🔄 **Data Preprocessing** pipeline (CSV → Cleaned)
- ⚙️ Flask Backend for serving insights
- 🧪 Easily replaceable dataset for production SaaS

---

## 📁 Project Structure

```
saas_kpi_dashboard/
└── saas_kpi_dashboard/
    ├── app.py                         # Main Flask app
    ├── preprocess_netflix.py         # Cleans and processes Netflix dataset
    ├── requirements.txt              # Python dependencies
    ├── alerts/
    │   └── anomaly_detection.py      # Anomaly detection logic
    ├── data/
    │   ├── netflix_titles.csv        # Raw dataset
    │   └── processed_netflix.csv     # Cleaned dataset
    └── forecast/
        └── arima_model.py            # ARIMA model forecasting
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/mlbyarafat/saas_kpi_dashboard.git
cd saas_kpi_dashboard/saas_kpi_dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Flask App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` to access the dashboard/API.

---

## 🧪 Functional Modules

| File | Purpose |
|------|---------|
| `preprocess_netflix.py` | Prepares clean dataset for analysis |
| `arima_model.py` | Generates forecast for time-series KPIs |
| `anomaly_detection.py` | Detects anomalies in data trends |
| `app.py` | Runs the Flask backend server |

---

## 📦 Dataset

Used [`netflix_titles.csv`](https://www.kaggle.com/datasets/shivamb/netflix-shows) for demonstration. Replace it with your own SaaS KPIs to go live.

---

## 🔮 Future Scope

- 📈 Visual dashboard (HTML/JS frontend)
- 🧠 ML-based anomaly detection (e.g., Isolation Forest)
- 📦 API-based KPI data injection (POST/GET)
- 📧 Email/Slack alerts for detected anomalies

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Md. Arafat**  
GitHub: https://github.com/mlbyarafat
