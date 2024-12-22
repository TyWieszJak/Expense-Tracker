from user_choices import UserChoices



class UserInterface(UserChoices):
    def __init__(self):
        super().__init__()

    def menu(self):

        while True:
            print ("1. Add an expense")
            print("2. Delete an expense")
            print("3. Update an expense")
            print("4. View all expense")
            print("5. Summary of all expense")
            print("6. Summary for specific month")
            print("7. Exit")

            choice = int(input("What do you want to do: "))
            try:

                match choice:
                    case 1:
                        try:
                            add_amount = float(input("Enter the amount of the expense: \n"))
                            description = input("Enter the description: \n").strip()
                            if not description:
                                raise ValueError("Description cannot be empty.")
                            view_adding_amount = self.add_expense(description, add_amount)
                            #self.add_expense(description, add_amount)
                        except ValueError as e:
                            print(f"Invalid input: {e}")
                        
                        print(view_adding_amount)
                    case 2:
                        try:
                            for expense_id, expense_details in self.expenses.items():
                                print(f"ID: {expense_details['id']} - Amount: {expense_details['amount']} - Description: {expense_details['description']} - Date: {expense_details['date']}")
                            expense_id = int(input("Enter the ID of the expense to delete: \n"))
                            view_deleted_amount = self.delete_expense(expense_id)
                            print(view_deleted_amount)

                        except ValueError:
                            print("Invalid input. Please enter a valid ID.")
                    case 3:
                        pass
                    case 4:
                        view_all_expenses = self.view_all_expenses()

                        if not view_all_expenses:
                            print("Seznam výdajů je prázdný.")
                        else:
                            print("Seznam výdajů:")
                            print("-" * 30)
                            for description, expense in view_all_expenses:
                                print(f"{description:20} {expense:10.2f}")
                            print("-" * 30)

                    case 5:
                        expense = self.summary_all_expenses()
                        print(f"Amount of the expense is : {expense} dollars.\n")
                    case 6:
                        pass
                    case 7:
                        exit()
                    case _:
                        print("Invalid choice. Please try again.")
            except ValueError:
                print ("Invalid choice. Please enter a number.")
            except  KeyboardInterrupt:
                print("Program successfully end by user")
