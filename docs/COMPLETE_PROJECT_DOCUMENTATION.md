# Hybrid AI-Expert Phishing Detection System

## 📋 Project Overview
A machine learning system that combines artificial intelligence with rule-based expert systems to detect phishing emails and messages with high accuracy and explainable reasoning.

**Developer:** Daniel Muoka (@SirDaniel)  
**Registration Number:** P101/4338G/23  
**Institution:** Karatina University  
**Academic Program:** BSc Computer Science (Third Year)  
**Career Focus:** Cybersecurity Engineering  
**Target Role:** Security Engineer

## 🎯 Project Objectives
- Build an accurate phishing detection AI model (>97% accuracy)
- Integrate explainable rule-based expert system
- Create user-friendly web application interface
- Demonstrate practical cybersecurity application of AI

## 🛠️ Technology Stack
- **Programming Language:** Python 3.13
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Natural Language Processing:** NLTK, TF-IDF Vectorization
- **Web Framework:** Flask
- **Environment:** Kali Linux, Virtual Environments
- **Data Serialization:** Joblib

## 📂 Project Structure

```text
Phishing_Email_Detector/
├── 📁 code/                 → Python scripts
│   ├── 🧠 app.py                 → Flask web application
│   ├── ⚙️ preprocess_data.py     → Data preprocessing
│   ├── 🤖 train_model.py         → Model training
│   ├── 🎯 optimize_model.py      → Hyperparameter tuning
│   └── 🧩 hybrid_system.py       → Hybrid AI-Expert system
│
├── 📁 data/                 → Datasets
│   ├── 📄 spam_cleaned.csv      → Cleaned dataset
│   └── 📦 *.joblib             → Processed data files
│
├── 📁 models/               → Machine learning models
│   ├── 🪄 optimized_random_forest_model.joblib
│   ├── 🧠 best_random_forest_model.joblib
│   └── 🔤 tfidf_vectorizer.joblib
│
├── 📁 templates/            → Web templates
│   ├── 🏠 index.html            → Main page
│   └── 📊 result.html           → Results page
│
├── 📁 docs/                 → Documentation
│
└── 🐍 venv/                 → Python virtual environment
```


## 📊 Performance Results
- **Overall Accuracy:** 97.94%
- **Spam Precision:** 0.99 (99% of detected spam was actually spam)
- **Spam Recall:** 0.85 (85% of all spam messages detected)
- **False Positive Rate:** <1%

## 🚀 Key Features
1. **Hybrid Intelligence:** Combines AI pattern recognition with human-defined rules
2. **Explainable AI:** Provides clear reasons for each decision
3. **Real-time Processing:** Web interface for instant analysis
4. **High Accuracy:** Professional-grade performance metrics
5. **Robust Architecture:** Proper error handling and validation

## 📅 Project Timeline (7-Day Implementation)
- **Day 1:** Environment Setup & Data Acquisition
- **Day 2:** Data Preprocessing & NLP
- **Day 3:** Model Training & Evaluation  
- **Day 4:** Model Optimization
- **Day 5:** Expert System Integration
- **Day 6:** Web Application Development
- **Day 7:** Documentation & Deployment (Current)

## 🎓 Academic Relevance
This project demonstrates competencies in:
- Machine Learning and AI implementation
- Natural Language Processing (NLP)
- Software Engineering best practices
- Cybersecurity threat detection
- Web application development
- Professional documentation

## 🔧 Installation & Usage
# 1. Clone repository
git clone <repository-url>
cd Phishing_Email_Detector

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run web application
export FLASK_APP=code/app.py
flask run --debug

📈 Future Enhancements
Real email integration (IMAP/POP3)
Browser extension development
Real-time threat intelligence feeds
Multi-language support
Mobile application version

👨‍💻 Developer Statement
This project represents my commitment to developing practical cybersecurity solutions using artificial intelligence. The hybrid approach demonstrates my understanding that effective security systems combine automated pattern recognition with human expertise and explainable decision-making.

© 2025 Daniel Muoka (@SirDaniel) | Karatina University | P101/4338G/23
