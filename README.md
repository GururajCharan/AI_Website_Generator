# 🚀 AI Website Generator

An AI-powered web application that generates complete frontend websites (HTML, CSS, JavaScript) from simple user prompts using Google Gemini and Streamlit.

---

## 📌 Overview

This project allows users to describe a website idea (e.g., *"Create a YouTube clone"*), and instantly generates a fully functional website with modern UI.

The generated website is:

* ✅ Responsive
* ✅ Styled with CSS
* ✅ Interactive with JavaScript
* ✅ Ready to download as a ZIP file

---

## ⚙️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Google Gemini API**
* HTML, CSS, JavaScript

---

## ✨ Features

* 🔹 AI-based website generation
* 🔹 Converts text prompts into working websites
* 🔹 Live preview inside the app
* 🔹 Download generated website as ZIP
* 🔹 Clean and modern UI output

---

## 📂 Project Structure

```
project/
│── website_file.py     # Main Streamlit app
│── index.html          # Generated HTML file
│── style.css           # Generated CSS
│── script.js           # Generated JS
│── requirements.txt    # Dependencies
│── .env                # API Key (not pushed)
│── .gitignore
│── output/             # Screenshots
```

---

## 🔑 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-website-generator.git
cd ai-website-generator
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file and add:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### ▶️ Run the App

```bash
streamlit run website_file.py
```

---

## 🧠 How It Works

1. User enters a website idea
2. Prompt is sent to Gemini via LangChain
3. AI generates complete website code
4. Code is saved and previewed
5. User downloads the website

---

## 📸 Screenshots

*Add your screenshots here (output folder)*

---

## ⚠️ Notes

* `.env` file is excluded for security
* Virtual environments (`venv/`) are ignored
* Generated files may vary based on prompt

---

## 🚀 Future Improvements

* Multi-page website generation
* Backend integration
* Hosting directly from app
* Template customization



