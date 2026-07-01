# 🤖 AI Interview Assistant

An AI-powered interview preparation platform that generates role-specific interview questions and evaluates user responses using Google's Gemini API. The application provides an interactive interview experience through a React frontend and a FastAPI backend.

---

## 🚀 Features

* Generate interview questions based on job role
* Select interview difficulty (Easy, Medium, Hard)
* AI-generated evaluation of user answers
* Instant feedback with scores and suggestions
* Clean and responsive user interface
* REST API built with FastAPI
* Powered by Google Gemini AI

---

## 🛠️ Tech Stack

### Frontend

* React (Vite)
* JavaScript
* CSS

### Backend

* FastAPI
* Python
* Google Gemini API
* Uvicorn

---

## 📂 Project Structure

```text
AI-Interview-Assistant/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── service/
│       └── gemini.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Sankeerth1411/AI-Interview-Assistant.git
cd AI-Interview-Assistant
```

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file inside the `backend` folder:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the backend:

```bash
uvicorn main:app --reload
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## 📌 API Endpoints

### Generate Interview Question

```
POST /question
```

### Evaluate Answer

```
POST /evaluate
```

---

## 💡 Future Improvements

* User authentication
* Interview history
* Multiple interview rounds
* Voice-based interviews
* PDF interview reports
* Dashboard with analytics

---

## 📷 Screenshots

Add screenshots of:

* Home Page
* Question Generation
* Interview Page
* Result Page

---

## 👨‍💻 Author

**Sankeerth Rajoli**

GitHub: https://github.com/Sankeerth1411

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
