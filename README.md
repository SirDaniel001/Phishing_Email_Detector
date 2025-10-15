# Phishing Email Detection using AI & Expert Systems

## 📌 Project Overview
This project implements a hybrid **AI (Machine Learning) and Expert System** to detect phishing emails/SMS messages. It is developed as part of the Artificial Intelligence and Expert Systems course at Karatina University, with a direct application towards a career in cybersecurity, specifically targeting financial sector threats.

**Developer:** Daniel Muoka (@SirDaniel)  
**Registration Number:** P101/4338G/23  
**Institution:** Karatina University  
**Career Goal:** Cybersecurity Expert

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

# 🛡️ AI Phishing Email Detector + Telegram Bot

A hybrid AI system that detects phishing emails with 97% accuracy, featuring both web interface and Telegram chatbot.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-orange)
![Telegram Bot](https://img.shields.io/badge/Telegram-Bot%20API-blue)
![Accuracy](https://img.shields.io/badge/Accuracy-97%25-brightgreen)

## 🚀 Features

### 🤖 Dual Interface System
- **Web Application**: Flask-based interface for detailed analysis
- **Telegram Bot**: Instant mobile phishing detection via chat
- **Same AI Engine**: Consistent 97% accuracy across both interfaces

### 🔍 Advanced Detection
- **Hybrid AI System**: Machine Learning + Expert Rules
- **Real-time Analysis**: Instant phishing detection
- **Confidence Scoring**: Probability-based results
- **Rule Explanations**: Transparent decision-making

### 📊 Performance
- **Accuracy**: 97.76% on test data
- **Model**: Optimized Random Forest
- **Training**: 5,000+ labeled email samples
- **Features**: TF-IDF + Custom rule-based system

## 🎯 Quick Start

### Local Installation
git clone https://github.com/SirDaniel001/Phishing_Email_Detector.git
cd Phishing_Email_Detector

# Install dependencies
pip install -r requirements.txt

# Run web application
python code/app.py
# Visit: http://127.0.0.1:5000

# Run Telegram bot (in separate terminal)
python code/telegram_bot.py

🏃‍♂️ Running the Telegram Bot
Set up Telegram Bot (one-time):
export TELEGRAM_BOT_TOKEN="your_bot_token_here"

Start the bot:
python code/telegram_bot.py

Find your bot on Telegram and send:
/start

#💬 Using the Telegram Bot
Available Commands
/start - Welcome message and instructions
/help - Detailed usage guide
/analyze [text] - Analyze specific text
Any message - Automatic phishing analysis
Example Usage
User: URGENT: Your bank account suspended! Click: bit.ly/fake-link

#Bot: 🔍 Phishing Analysis Complete

Final Verdict: 🚨 PHISHING DETECTED
AI Prediction: SPAM (64.8% confidence)

🔍 Rules Triggered:
• Urgency language
• Suspicious request

💡 Recommendation:
🚨 HIGH RISK - Do not click links or provide information

#🌐 Web Interface
Access the web application at http://127.0.0.1:5000:
Paste suspicious emails for analysis
View detailed results with confidence scores
See rule triggers and explanations
Professional UI with real-time processing

#🏗️ System Architecture
User Input → Hybrid AI System → Analysis Results
    ↓              ↓               ↓
 Telegram     ML Model +      🛡️ Safe / 🚨 Phishing
   Bot       Expert Rules     + Confidence Score
    ↓              ↓               ↓
 Web App      Feature         Detailed Report
            Extraction

#Core Components
telegram_bot.py - Bot interface and message handling
simple_detector.py - Optimized model loading for real-time use
hybrid_system.py - ML + rule-based decision engine
app.py - Flask web application

#📈 Model Performance
Metric  	AI-Alone	Hybrid System
Accuracy	97.94%  	97.76%
Precision	98%     	98%
Recall   	85%     	85%

#🛠️ Technical Stack
Machine Learning: Scikit-learn, Random Forest, TF-IDF
Web Framework: Flask, HTML/CSS
Chat Platform: Python-Telegram-Bot API
Data Processing: Pandas, NumPy, Joblib
Model Persistence: Joblib serialization

#🔧 Project Structure
Phishing_Email_Detector/
├── code/                 # Source code
│   ├── telegram_bot.py   # Telegram bot interface
│   ├── simple_detector.py # Optimized model loader
│   ├── hybrid_system.py  # AI + rules engine
│   ├── app.py           # Flask web application
│   └── *.py            # Training & evaluation scripts
├── models/              # Trained AI models
│   ├── *.joblib        # Serialized models
├── data/               # Datasets
│   ├── spam.csv        # Training data
├── templates/          # Web UI templates
├── requirements.txt    # Dependencies
└── README.md          # This file

##🎓 Academic Value
This project demonstrates:
End-to-end ML pipeline from data to deployment
Hybrid AI systems combining ML with domain knowledge
Multiple interface design (web + mobile)
Production considerations and deployment challenges

🔮 Future Enhancements
Cloud deployment for 24/7 access
Multi-language support
Advanced phishing pattern detection
User analytics dashboard
Email integration

#👨‍💻 Author
Daniel - Cybersecurity & AI Enthusiast
GitHub: @SirDaniel001
Project: Phishing Email Detector
#📄 License
This project is open source and available under the MIT License.

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


