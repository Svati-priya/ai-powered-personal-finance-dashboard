# 💰 AI-Powered Personal Finance Dashboard

A full-stack personal finance management application built with Django and PostgreSQL to help users track income and expenses, analyze spending behavior, and visualize important financial metrics through an interactive dashboard.

## 🚀 Features

- 💰 Track and manage income and expenses
- 📊 Interactive financial dashboard
- 📈 Analyze spending patterns
- 🗂️ Categorize transactions
- 🔍 Filter and manage financial records
- 📊 Visualize financial KPIs and trends
- 🤖 Data-driven financial insights
- 🗄️ PostgreSQL database integration
- 🔐 User authentication and account management

## 🛠️ Tech Stack

### Backend

- Python
- Django

### Database

- PostgreSQL
- SQLite (local development)

### Frontend

- HTML
- CSS
- JavaScript

### Tools

- Git
- GitHub
- Postman

## 🏗️ Project Architecture

```text
User
  │
  ▼
Django Web Application
  │
  ├── Authentication
  │
  ├── Expense Management
  │
  ├── Financial Analytics
  │
  └── Interactive Dashboard
  │
  ▼
PostgreSQL Database

ai-powered-personal-finance-dashboard/
│
├── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tracker/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
├── Procfile
├── build.sh
├── README.md
└── .gitignore