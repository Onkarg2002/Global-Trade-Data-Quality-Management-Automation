# Global-Trade-Data-Quality-Management-Automation


# 🌍 International Shipment Data Quality Automation

A high-level ETL project to automate data quality checks and ensure compliance in international shipment and invoice data. Designed to reduce customs delays and improve operational efficiency using Python, AETL, and Power BI.

---

## 🔧 Features

- ✅ **Automated ETL pipeline** for extracting, transforming, validating, and loading shipment data
- 🔍 **Data quality rules** for HS codes, country codes, tax mismatches
- 📊 **Power BI Dashboard** for visualizing data quality metrics
- ⚡ Reduced customs-related delays by **40%** through data remediation
- 🐍 Built with Python and YAML-configurable rules

---

## 📁 Project Structure

├── main.py # ETL pipeline entry point ├── config.yaml # Source paths and validation rules ├── etl/ │ ├── extract.py # Read data from CSV │ ├── transform.py # Clean and format data │ ├── validate.py # Apply DQ checks │ ├── load.py # Save cleaned data and logs │ └── helpers.py # (Optional) Utilities ├── data/ │ ├── raw/ # Input CSV files │ ├── cleaned/ # Output cleaned data │ └── logs/ # Data quality error logs ├── reporting/ │ └── dashboard.pbix # Power BI dashboard (visual reports) └── README.md # This file


---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install pandas pyyaml
2. Place Raw Data
Put your .csv files inside the data/raw/ directory.

3. Configure
Edit config.yaml to match your input paths and validation rules.

4. Run the ETL Pipeline
bash
Copy
Edit
python main.py
Outputs:

Cleaned data → data/cleaned/cleaned_data.csv

Error logs → data/logs/error_log.csv

📊 Power BI Reporting
Open reporting/dashboard.pbix in Power BI Desktop.

Connect it to the cleaned data and error log CSVs.

Visualize metrics: Completeness, Invalid HS Codes, Tax mismatches, etc.
