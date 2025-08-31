# 🪙 Rare Metals ETL

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws&logoColor=white)  
![Databricks](https://img.shields.io/badge/Databricks-Analytics-red?logo=databricks&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

---

**Rare Metals ETL** is a data pipeline designed to extract, transform, and visualize data on rare metals prices. The project is divided into two main sections, combining ⚡ **AWS cloud infrastructure** (for extraction and transformation) with 📊 **Databricks** (for visualization).  

---

## 🔄 Project Workflow  

### 1️⃣ Data Extraction & Transformation (AWS)  
- **Fetch Data:** Retrieves real-time rare metals data from external APIs.  
- **Transform Data:** Cleans and structures the raw data into `.csv` format.  
- **Storage:** Uploads the processed files into an **AWS S3 bucket**.  

### 2️⃣ Data Ingestion & Visualization (Databricks)  
- **Ingest Data:** Loads the `.csv` files from S3 into **Databricks**.  
- **Processing & Analytics:** Performs transformations, aggregations, and metric calculations.  
- **Dashboard Visualization:** Presents insights through interactive dashboards.  

---
