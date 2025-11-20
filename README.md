# Final Project: Flask Healthcare Application

**Author:** Saheed Adebowale Badru
**Course:** BAN6420 – Programming in R & Python
**University:** Nexford University
**Program:** Master of Science in Data Analytics

# Introduction 

A complete guide to understanding, setting up, running, analyzing, and deploying the Flask Healthcare Income & Spending Survey Application.

This application allows users to submit demographic and household spending information through a Flask web form, stores responses in MongoDB Atlas, exports the dataset into CSV format, generates visual insights in Jupyter Notebook, and deploys the live application on AWS EC2.

---

# 📌 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Local Installation & Setup](#local-installation--setup)
6. [Running the Flask Application Locally](#running-the-flask-application-locally)
7. [Exporting MongoDB Data to CSV](#exporting-mongodb-data-to-csv)
8. [Data Analysis in Jupyter Notebook](#data-analysis-in-jupyter-notebook)
9. [GitHub Repository Setup](#github-repository-setup)
10. [AWS EC2 Deployment Guide](#aws-ec2-deployment-guide)
11. [Security Notes](#security-notes)
12. [Rubric Checklist](#rubric-checklist)

---

# 🧭 Project Overview

This project is a **Flask web application** that collects data on:

* Age
* Gender
* Total Monthly Income
* Monthly Expenses (Utilities, Entertainment, School Fees, Shopping, Healthcare)

Data submitted through the application is stored in **MongoDB Atlas**, exported to a CSV file using a custom Python script, and analyzed in **Jupyter Notebook** with meaningful visualizations.

The final application is deployed to **AWS EC2** and accessible through a public DNS.

---

# ⭐ Features

* User-friendly HTML form for data entry
* MongoDB Atlas integration for cloud data storage
* Python `User` class for structured data transformation
* CSV export functionality
* Data analysis using Pandas and Matplotlib
* Visual chart generation for reporting or presentations
* GitHub repository linkage for version control
* AWS deployment for live hosting

---

# 🛠 Technologies Used

* **Python 3**
* **Flask** (Web Framework)
* **MongoDB Atlas** (Cloud Database)
* **Pymongo** (MongoDB Client)
* **Pandas** (Data Analysis)
* **Matplotlib** (Data Visualization)
* **Jupyter Notebook** (Analysis Environment)
* **AWS EC2** (Deployment)
* **Git & GitHub** (Version Control)

---

# 📁 Project Structure

```
Final-Flask-Healthcare-App/
│
├── app.py                # Main Flask application
├── config.py             # MongoDB connection config (DO NOT commit secrets)
├── models.py             # User class for CSV transformation
├── export_to_csv.py      # Script to export MongoDB data to CSV
├── requirements.txt      # Project dependencies
│
├── data/
│   └── user_spending.csv # Generated CSV file
│
├── notebooks/
│   └── analysis.ipynb    # Jupyter data analysis notebook
│
├── templates/
│   ├── index.html        # Main form page
│   └── success.html      # Post-submission confirmation
│
├── static/
│   └── style.css         # Optional CSS
│
└── README.md             # Project documentation
```

---

# 🖥 Local Installation & Setup

Follow these steps to run the project locally.

## 1. Clone the repository

```
git clone https://github.com/<your-username>/final-flask-healthcare-app.git
cd final-flask-healthcare-app
```

## 2. Create and activate a virtual environment

### Windows:

```
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```
pip install -r requirements.txt
```

## 4. Create your `config.py`

```
MONGO_URI = "your-mongodb-atlas-uri-here"
```

⚠️ **Do not commit your real MongoDB URI.**

---

# ▶ Running the Flask Application Locally

```
python app.py
```

Visit in your browser:

```
http://127.0.0.1:5000/
```

Fill the form → Submit → Check MongoDB Atlas for new documents.

---

# 📤 Exporting MongoDB Data to CSV

To export all collected survey data to CSV:

```
python export_to_csv.py
```

Your CSV file will be generated at:

```
data/user_spending.csv
```

---

# 📊 Data Analysis in Jupyter Notebook

Launch Jupyter Notebook:

```
jupyter notebook
```

Open:

```
notebooks/analysis.ipynb
```

This notebook generates:

* `age_income_chart.png`
* `gender_spending_chart.png`

Charts are saved in the `data/` folder and can be used for reports or presentations.

---

# 🌐 GitHub Repository Setup

If you haven't pushed the project to GitHub yet, follow these steps.

## 1. Initialize Git

```
git init
git add .
git commit -m "Initial commit"
```

## 2. Create a `.gitignore`

Recommended entries:

```
venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
config.py
```

```
git add .gitignore
git commit -m "Add gitignore"
```

## 3. Connect to GitHub

```
git remote add origin https://github.com/<your-username>/final-flask-healthcare-app.git
git branch -M main
git push -u origin main
```

---

# ☁ AWS EC2 Deployment Guide

Deploy your Flask app live using AWS EC2.

## Step 1 — Launch EC2 Instance

* AMI: Ubuntu 22.04
* Type: t2.micro
* Open inbound ports:

  * **22** (SSH)
  * **80** (HTTP)
  * Or **5000** if using Flask default port

Download your `.pem` key.

## Step 2 — SSH into EC2 (Windows example)

```
ssh -i "C:\Users\HP\Downloads\my-key.pem" ubuntu@<ec2-public-dns>
```

## Step 3 — Install dependencies

```
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
```

## Step 4 — Clone your repository

```
git clone https://github.com/<your-username>/final-flask-healthcare-app.git
cd final-flask-healthcare-app
```

## Step 5 — Create venv and install requirements

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 6 — Configure MongoDB access

Create a `config.py` on the server with a valid Atlas URI.

## Step 7 — Run Flask (recommended: port 5000)

```
python3 app.py
```

Visit:

```
http://<ec2-public-dns>:5000/
```

If using port 80, run with sudo:

```
sudo python3 app.py
```

And access:

```
http://<ec2-public-dns>/
```

---

# 🔐 Security Notes

* Never push real credentials to GitHub.
* Restrict MongoDB Atlas network access.
* Clean your `.pem` permissions locally.
* Use environment variables if extending the project.

---

# ✅ Checklist

This section ensures all project requirements have been met.

### ✔ Flask Application

* Form fields implemented
* `/submit` route working
* Data saved to MongoDB Atlas

### ✔ MongoDB Integration

* Valid URI
* Proper document structure

### ✔ User Class

* Implemented in `models.py`
* Used in CSV export script

### ✔ CSV Export

* `export_to_csv.py` generates CSV correctly

### ✔ Jupyter Notebook Visualizations

* Income by age chart
* Spending by gender chart
* PNG files saved

### ✔ AWS Deployment

* EC2 instance running Flask app
* Accessible via public DNS

### ✔ Documentation

* README is complete, clear, and well-structured

---

📌 **END OF README**\
