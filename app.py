from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import TransactionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Add a secret key for form validation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Transaction {self.id} - {self.category} - {self.amount}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-transaction', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        new_transaction = Transaction(
            amount=form.amount.data,
            category=form.category.data,
            date=form.date.data
        )
        try:
            db.session.add(new_transaction)
            db.session.commit()
            return redirect(url_for('report'))
        except Exception as e:
            return f"An error occurred while adding the transaction: {e}"
    
    return render_template('add_transaction.html', form=form)

@app.route('/report')
def report():
    transactions = Transaction.query.order_by(Transaction.date).all()
    return render_template('report.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)

