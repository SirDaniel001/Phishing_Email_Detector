# Phishing Email Detection using AI & Expert Systems

## 📌 Project Overview
This project implements a hybrid **AI (Machine Learning) and Expert System** to detect phishing emails/SMS messages. It is developed as part of the Artificial Intelligence and Expert Systems course at Karatina University, with a direct application towards a career in cybersecurity, specifically targeting financial sector threats.

**Developer:** Daniel Muoka (@SirDaniel)  
**Registration Number:** P101/4338G/23  
**Institution:** Karatina University  
**Career Goal:** Cybersecurity Expert at the Central Bank of Kenya

## 🎯 Project Objectives
1. To build a machine learning model that accurately classifies messages as "ham" (legitimate) or "spam" (phishing).
2. To integrate a rule-based expert system for explainable AI and improved detection of known phishing patterns.
3. To create a functional web application demo for real-time classification.
4. To demonstrate practical AI skills for cybersecurity applications.

## 📂 Project Structure
Phishing_Email_Detector/
├── code/ # Python scripts for data processing, modeling, and application
├── data/ # Dataset storage (raw and cleaned)
├── docs/ # Documentation, reports, and presentations
├── models/ # Saved trained models
└── venv/ # Python virtual environment


## 📊 Dataset
**Source:** SMS Spam Collection Dataset from Kaggle  
**Contents:** 5,572 SMS messages tagged as either ham (legitimate) or spam (phishing)  
**Original Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)

**Label Distribution:**
- Ham: 4,825 messages
- Spam: 747 messages

## 🛠️ Technology Stack
- **Programming Language:** Python 3.13
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Natural Language Processing:** NLTK
- **Web Application:** Flask
- **Development Environment:** Kali Linux

## 📅 Project Roadmap (7-Day Plan)

### Day 1: Foundation & Setup (Completed ✅)
- Created project structure and virtual environment
- Installed required Python packages
- Acquired and cleaned dataset
- Validated environment and data integrity

**Tools Installed:** pandas, numpy, scikit-learn, nltk, flask, matplotlib, seaborn

### Day 2: Data Preprocessing & NLP
- Text cleaning and normalization
- Tokenization and stopword removal
- Feature extraction using TF-IDF

### Day 3: Model Training & Evaluation
- Implement Naive Bayes and Random Forest classifiers
- Initial model evaluation and selection

### Day 4: Model Optimization
- Hyperparameter tuning
- Advanced performance metrics analysis
- Final model selection

### Day 5: Expert System Integration
- Develop rule-based phishing detection logic
- Create hybrid AI-Expert system

### Day 6: Application Development
- Build Flask web application
- Create user interface for real-time classification

### Day 7: Documentation & Deployment
- Finalize project documentation
- Prepare presentation materials
- Deploy application for demonstration

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- Kali Linux (or similar Linux distribution)
- pip package manager

### Installation
1. Clone or download this project structure
2. Create virtual environment: `python3 -m venv venv`
3. Activate environment: `source venv/bin/activate`
4. Install requirements: `pip install pandas numpy scikit-learn nltk flask matplotlib seaborn`

### Usage
1. Ensure virtual environment is activated: `source venv/bin/activate`
2. Run data cleaning: `python code/clean_data.py`
3. Execute main training script: `python code/train_model.py`
4. Launch web application: `python code/app.py`

## 📝 License
© 2025 Daniel Muoka (@SirDaniel). This project is licensed for academic use at Karatina University. All rights reserved.

## 🤝 Acknowledgments
- Karatina University Computer Science Department
- Apache SpamAssassin for public dataset
- Kaggle community for data resources
- The cybersecurity community for ongoing research in phishing detection


