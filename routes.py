from flask import Flask, request, jsonify, make_response
from models import db, User, Expense
import csv

app = Flask(__name__)

# Add user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], phone_number=data['phone_number'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'}), 201

# Retrieve user details
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'phone_number': user.phone_number}), 200
    return jsonify({'message': 'User not found'}), 404

# Add expense
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    new_expense = Expense(user_id=data['user_id'], amount=data['amount'], split_type=data['split_type'], participants=data['participants'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully!'}), 201

# Retrieve expenses for a specific user
@app.route('/expenses/<int:user_id>', methods=['GET'])
def get_user_expenses(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    if expenses:
        expense_list = [{'amount': exp.amount, 'split_type': exp.split_type, 'participants': exp.participants} for exp in expenses]
        return jsonify({'expenses': expense_list}), 200
    return jsonify({'message': 'No expenses found for this user'}), 404

# Generate and download balance sheet
@app.route('/balance_sheet/<int:user_id>', methods=['GET'])
def download_balance_sheet(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    if not expenses:
        return jsonify({'message': 'No expenses found for this user'}), 404

    # Prepare CSV data
    output = []
    output.append(['Amount', 'Split Type', 'Participants'])
    for exp in expenses:
        output.append([exp.amount, exp.split_type, exp.participants])

    # Create CSV response
    response = make_response("\n".join([",".join(map(str, row)) for row in output]))
    response.headers["Content-Disposition"] = "attachment; filename=balance_sheet.csv"
    response.headers["Content-type"] = "text/csv"
    return response

# Home route
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Daily Expenses Sharing App!'})

if __name__ == '__main__':
    app.run(debug=True)  # This will run the Flask application
