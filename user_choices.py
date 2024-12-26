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
        self.counter += 1  #
        return (f"Added: #{expense['id']} - {add_amount} dollars for {description} on {date}.\n")

    def delete_expense(self, expense_id):
        for description, expense in list(self.expenses.items()):
            if expense['id'] == expense_id:
                del self.expenses[description]
                return f"Deleted expense: {expense['description']} (ID: {expense_id}).\n"
        return f"No expense found with ID '{expense_id}'.\n"

    def summary_all_expenses(self):
        return sum(expense["amount"] for expense in self.expenses.values())
    
    def view_all_expenses(self):
        return [(expense['id'], expense['description'], expense['amount'], expense['date']) for expense in self.expenses.values()]
    
    def update_expense(self, expense,expense_id, description, amount):
        expense['description'] = description
        expense['amount'] = amount
        expense['date'] = expense['date']
        return f"Updated expense: {expense['description']} (ID: {expense_id}).\n"    



         #list(self.expenses.items())
         #[(description, expense) for description, expense in self.expenses.items()]

