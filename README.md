# Daily Expenses Sharing App

This project is a backend for a Daily Expenses Sharing Application that allows users to add expenses, split them using various methods, and generate balance sheets.

## Features
- User management (create users, retrieve user details)
- Expense management (add expenses, retrieve individual and overall expenses)
- Split expenses equally, by exact amount, or by percentage
- Generate and download balance sheets

## Installation and Setup

### Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy

### Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/daily_expenses_app.git
   cd daily_expenses_app
### Set up a virtual environment
- python3 -m venv venv
- source venv/bin/activate

### Run the Flask application
- python app.py

### API Endpoints
- POST /users: Create a new user
- GET /users/<user_id>: Retrieve user details
- POST /expenses: Add a new expense
- GET /expenses/<user_id>: Retrieve a user's expenses
- GET /balance_sheet/<user_id>: Download the balance sheet
