# 💰 Personal Finance Analytics Dashboard

A full-stack personal finance management application built with Django that allows users to securely track income and expenses, manage transactions, and visualize financial metrics through an interactive dashboard.

## 🚀 Features

- 💰 Track and manage income and expenses
- 📊 Interactive financial dashboard
- 📈 Calculate total income, expenses, and balance
- 🗂️ Categorize transactions
- 🔍 Filter transactions by type
- ✏️ Edit financial records
- 🗑️ Delete transactions
- 🔐 User registration and authentication
- 👤 User-specific transaction management
- 📊 Visualize income and expense data

## 🛠️ Tech Stack

### Backend

- Python
- Django

### Database

- SQLite

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
  ├── Transaction Management
  │   ├── Add
  │   ├── Edit
  │   └── Delete
  │
  ├── Financial Analytics
  │   ├── Total Income
  │   ├── Total Expenses
  │   └── Balance
  │
  └── Interactive Dashboard
          │
          ▼
      SQLite Database
```

## 📁 Project Structure

```text
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
```

## ⚙️ Installation & Setup

Follow these steps to set up and run the project locally.

### Prerequisites

Make sure you have **Python** and **Git** installed on your system.

### 1. Clone the repository

```bash
git clone https://github.com/Svati-priya/ai-powered-personal-finance-dashboard.git
cd ai-powered-personal-finance-dashboard
```

### 2. Create a virtual environment

#### macOS & Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```text
SECRET_KEY=your-secret-key
```

Never commit the `.env` file to GitHub.

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🔐 Security

- Django `SECRET_KEY` is stored using environment variables.
- `.env` is excluded from Git using `.gitignore`.
- User transactions are associated with authenticated users.
- Users can only edit or delete their own transactions.
- Django authentication is used for user login and account management.

## 🔮 Future Improvements

- PostgreSQL database support
- Advanced spending analytics
- Monthly and category-based reports
- Budget tracking
- Expense trend visualization
- Automated financial insights
- AI/ML-based spending predictions
- AWS deployment
