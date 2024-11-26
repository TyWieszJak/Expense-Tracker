from datetime import datetime

class UserChoices:
    def __init__(self):
        self.expenses = {}  # Slovník pro výdaje
        self.counter = 1

    def add_expense(self, description, add_amount, date=None):
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        expense = {
            'id' : self.counter,
            'amount' : float(add_amount),
            'description' : description,
            'date' : date
        }
        self.expenses[self.counter] = expense
        self.counter += 1  # Při každém přidání výdaje se inkrementuje counter
        return (f"Added: #{expense['id']} - {add_amount} dollars for {description} on {date}.\n")

    def delete_expense(self, expense_id):
        for description, expense in list(self.expenses.items()):
            if expense['id'] == expense_id:
                del self.expenses[description]
                return f"Deleted expense: {expense['description']} (ID: {expense_id}).\n"
        return f"No expense found with ID '{expense_id}'.\n"

    def summary_all_expenses(self):
        return sum(expense["amount"] for expense in self.expenses.values())

