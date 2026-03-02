📘 README — Sales Analyzing Agent (AI + ML Dashboard)

📌 Project Overview
The **Sales Analyzing Agent** is an AI/ML-powered dashboard application developed using **Streamlit**.  
It provides:

- Interactive sales analytics  
- Region-wise and category-wise breakdown  
- Time-series forecasting using **Prophet ML model**  
- Visual reports (line chart, bar chart, pie chart, forecast curves)  
- Company-branded dashboard (logo included)  
- Built-in synthetic dataset (365 days of sales data)

This project is production-ready, modular, and easy to modify or deploy.
---

🏗 Features

 📊 1. Sales Analytics Dashboard
- Sales over time  
- Sales by region  
- Category distribution  
- Total, average, and peak sales metrics  

 🤖 2. Machine Learning – Forecasting
The system uses the **Prophet** forecasting model to predict future sales for:
- 7 to 180 days  
- With auto-generated confidence intervals

 🎨 3. Company Branding
- Custom logo (placeholder provided in `assets/`)  
- Clean UI with sidebar navigation  

 📁 4. Modular Codebase
Separated into logical modules:
- `data_loader.py`
- `visualizer.py`
- `forecasting.py`
- `utils.py`
---

📂 Project Folder Structure
```
sales_analyzing_agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sales_data.csv
│
├── assets/
│   └── company_logo.png
│
└── modules/
    ├── data_loader.py
    ├── visualizer.py
    ├── forecasting.py
    └── utils.py
```

⚙️ Installation & Setup

 1. Install Python
Make sure Python **3.8+** is installed.

 2. Install Dependencies
Run inside the project folder:

```
pip install -r requirements.txt
```
This installs:
- Streamlit  
- Prophet  
- Pandas  
- Plotly  
- NumPy  
- Scikit-learn  
- Matplotlib  
---

 3. Run the Application
Navigate to your folder:
Run Streamlit:
```
streamlit run app.py
```
Your dashboard will open.

📘 Usage Instructions

 ▶ Dashboard Sections
 **1. Overview Metrics**
Displays:
- Total Sales  
- Average Daily Sales  
- Maximum Daily Sale  

 **2. Visual Charts**
- Line chart: Sales trend  
- Bar chart: Sales by region  
- Pie chart: Category distribution  

 **3. Forecasting**
Use slider to select number of days (7–180).  

Outputs:
- Forecast line graph  
- Forecast data table (Predicted, Lower, Upper bounds)

---

🧪 Dataset
The project includes a synthetic dataset containing:

- 365 days  
- Randomized sales values between **500–2500**  
- Regions: *North, South, East, West*  
- Categories: *Electronics, Furniture, Groceries, Clothing*  

File location:
```
data/sales_data.csv
```
You may replace this with your real dataset (same column names required).
---

🛠 Customization

 ✔ Change Company Logo
Replace the image at:
```
assets/company_logo.png
```

 ✔ Replace Dataset
Upload your CSV matching:
```
date,sales,region,category
```

 ✔ Add More Analytics
Modify `modules/visualizer.py` to add:
- Heatmaps  
- Multi-year trends  
- Regional time-series  
---

 🚀 Deployment Options
You can deploy this app to:

- Streamlit Cloud  
- Heroku  
- AWS EC2  
- Azure Web App  
- DigitalOcean  
---

---
