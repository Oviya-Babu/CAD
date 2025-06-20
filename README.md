# 💌 Email Phishing Detector — AI-Powered Chrome Extension

> 🚨 Finalist Project | CAD 3.0 Hackathon – SRM  
> Built with ML, Flask & JavaScript | Solving real-world cyber threats

---

## 🚀 Project Overview

With the rapid rise of AI-generated content, phishing emails are now more sophisticated than ever.  
Our project, **Cyber Sentinel**, aims to tackle this pressing issue by leveraging Machine Learning to classify email content as **Phishing** or **Not Phishing**, all through a seamless Chrome Extension interface.

---

## 🛠️ Tech Stack

| Layer        | Technology Used                             |
|--------------|---------------------------------------------|
| Frontend     | HTML, CSS, JavaScript (Chrome Extension)    |
| Backend      | Python (Flask)                              |
| Machine Learning | Scikit-learn, TF-IDF, Random Forest     |
| Data Handling| Pandas, imbalanced-learn                    |
| Model File   | `phishing_email_model.pkl`                  |
| Dataset      | `Phishing_Email.csv` (Cleaned & Oversampled)|

---

## 🔍 Features

- 📩 Paste any email text in the extension
- 🧠 Real-time phishing prediction using ML
- 🔒 Backend API with JSON-based Flask route
- 📊 Confidence score for each prediction
- 🧪 Trained using TF-IDF + Random Forest classifier
- 💡 Built from scratch during a 24-hour Hackathon

---

## 📂 Repository Structure

phishing-email-detector/
├── backend/
│ ├── app.py
│ ├── phishing_email_model.pkl
│ └── Phishing_Email.csv
├── chrome-extension/
│ ├── popup.html
│ ├── popup.js
│ ├── styles.css
│ ├── manifest.json
│ └── icon-48.png
├── requirements.txt


** Hackathon Highlights**
 
🏁 Event: CAD 3.0 Hackathon, SRM
👨‍💻 Team: POS SQUAD
🎉 Achievement: Top 10 Finalist among 100+ teams
💡 Challenge: "AI is making phishing more realistic — how do we fight back?"
✅ Solution: Built an end-to-end ML-powered Chrome Extension to detect AI-generated phishing emails


✅ Future Enhancements
🔗 Deploy backend API to the cloud (Render/Heroku)
📥 Gmail auto-scan integration
🧠 Model improvement using LLMs & GPT integration
🌍 Multi-language dataset support


 License
This project is licensed under the MIT License – feel free to use, modify, and share with credit!


