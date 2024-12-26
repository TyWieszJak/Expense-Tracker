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
            try:
                    choice = int(input("What do you want to do: "))
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
                                self.view_all()
                                expense_id = int(input("Enter the ID of the expense to delete: \n"))
                                view_deleted_amount = self.delete_expense(expense_id)
                                print(view_deleted_amount)

                            except ValueError:
                                print("Invalid input. Please enter a valid ID.")
                        case 3:
                            self.view_all()
                            expense_id = int(input("Enter the ID of the expense to update: \n"))
                            for expense in self.expenses.values():
                                if expense['id'] == expense_id:
                                    description = input("Enter the new description: \n")
                                    amount = float(input("Enter the new amount: \n"))
                                    update_expense = self.update_expense(expense,expense_id, description, amount)        
                                    print(update_expense)
                        case 4:
                            self.view_all()

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


    def view_all(self):
        view_all_expenses = self.view_all_expenses()
        if not view_all_expenses:
            print("Seznam výdajů je prázdný.")
        else:
            print("Seznam výdajů:")
            print("-" * 30)
            for id , description, expense, date in view_all_expenses:
                print(f"{id} {description:20} {expense:10.2f} dollars  {date}")
                print("-" * 30)
