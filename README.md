# 💳 Credit Card Fraud Detection System

A Machine Learning-based web application that detects fraudulent credit card transactions using the **Extra Trees Classifier**. The application provides both **single transaction prediction** and **batch prediction through CSV upload** through an interactive **Streamlit dashboard**.

---

## 🚀 Live Demo

**🌐 Streamlit App:** *(Add your deployed Streamlit link here)*

**💻 GitHub Repository:** *(Add your GitHub repository link here)*

---

# 📌 Project Overview

Credit card fraud has become one of the biggest challenges in the financial industry. Detecting fraudulent transactions accurately while minimizing false alarms is crucial for protecting customers and financial institutions.

This project uses **Machine Learning** to classify transactions as **Legitimate** or **Fraudulent**. Multiple classification algorithms were evaluated, and the **Extra Trees Classifier** achieved the best overall performance.

The web application provides an intuitive interface for:

- 📊 Interactive Dashboard
- 📂 Dataset Exploration
- 🔍 Single Transaction Prediction
- 📄 Batch Prediction using CSV Upload
- 📥 Download Prediction Results
- 📈 Model Performance Analysis
- 🌳 Feature Importance Visualization

---

# 📂 Dataset

**Dataset:** Credit Card Fraud Detection Dataset

### Dataset Statistics

| Property | Value |
|----------|--------|
| Total Transactions | 284,807 |
| Legitimate Transactions | 284,315 |
| Fraudulent Transactions | 492 |
| Features | 31 |
| Target Variable | Class |

### Target Variable

| Value | Meaning |
|-------|----------|
| 0 | Legitimate Transaction |
| 1 | Fraudulent Transaction |

The dataset is highly **imbalanced**, therefore **SMOTE (Synthetic Minority Oversampling Technique)** was used to balance the training data before model training.

---

# 🛠 Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Extra Trees Classifier
- SMOTE (Imbalanced-Learn)

## Data Processing

- Pandas
- NumPy

## Visualization

- Matplotlib

## Web Framework

- Streamlit

---

# 🤖 Machine Learning Workflow

The project follows the complete Machine Learning lifecycle:

1. Load Dataset
2. Data Cleaning
3. Handle Missing Values
4. Feature Scaling
5. Apply SMOTE
6. Train Multiple Models
7. Compare Model Performance
8. Select Best Model
9. Save Trained Model
10. Deploy using Streamlit

---

# 📊 Models Evaluated

The following algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- ⭐ Extra Trees Classifier (Best)
- Gradient Boosting
- AdaBoost
- XGBoost
- LightGBM
- CatBoost

### 🏆 Best Model

**Extra Trees Classifier**

---

# 📈 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | **99.95%** |
| Precision | **94.74%** |
| Recall | **75.79%** |
| F1 Score | **84.21%** |

---

# ✨ Application Features

## 🏠 Dashboard

- Dataset Overview
- Fraud Statistics
- Transaction Summary
- Interactive Charts

---

## 🔍 Prediction

### Single Transaction Prediction

- Enter transaction details manually
- Predict Fraud / Legitimate
- Fraud Probability Score

### Batch Prediction

- Upload CSV File
- Predict all transactions
- Download prediction results as CSV

---

## 📊 Visualizations

- Class Distribution
- Feature Importance
- Confusion Matrix
- ROC Curve

---

# 📁 Project Structure

```text
Fraud-Detection-System/
│
├── app.py
│
├── assets/
│   ├── logo.png
│   └── style.css
│
├── data/
│   └── raw/
│       └── creditcard.csv
│
├── pages/
│   ├── home.py
│   ├── dataset.py
│   ├── prediction.py
│   ├── model.py
│   └── about.py
│
├── saved_models/
│   ├── best_model.pkl
│   ├── amount_scaler.pkl
│   ├── time_scaler.pkl
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
│
├── src/
│
├── utils/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Fraud-Detection-System.git
```

---

## 2️⃣ Move into the Project Directory

```bash
cd Fraud-Detection-System
```

---

## 3️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

---

## 4️⃣ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

# 📸 Application Screenshots

> Add screenshots of your application after deployment.

Suggested screenshots:

- 🏠 Home Page
- 📊 Dashboard
- 📂 Dataset Page
- 🔍 Prediction Page
- 📈 Model Performance
- 📄 Batch Prediction

---

# 🎯 Future Improvements

- 🔗 Real-time API Integration
- 🧠 Deep Learning Models
- 📜 Transaction History
- 🔐 User Authentication
- 🤖 Explainable AI (SHAP/LIME)
- ☁ Cloud Database Integration
- 📱 Mobile Responsive UI
- 📊 Real-time Fraud Monitoring Dashboard

---

# 📦 Requirements

Major libraries used:

- streamlit
- pandas
- numpy
- matplotlib
- scikit-learn
- imbalanced-learn
- joblib
- xgboost
- lightgbm
- catboost

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 👩‍💻 Developer

## Disha Dutta

**GitHub:** *(Add your GitHub Profile Link)*

**LinkedIn:** *(Add your LinkedIn Profile Link)*

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is created for **educational and learning purposes**. Feel free to fork and enhance it for your own learning.