expenses = []   
def add_expense():
    month = input("Enter month (Jan, Feb, etc): ")
    name = input("Enter expense name: ")
    amount = int(input("Enter amount: "))

    expenses.append([month, name, amount])
    print(" Expense added!\n")
def monthly_total():
    search_month = input("Enter month to check: ")
    total = 0
    for e in expenses:
        if e[0].lower() == search_month.lower():
            total += e[2]
    print(f"Total expense for {search_month} =", total, "\n")
def yearly_total():
    total = 0

    for e in expenses:
        total += e[2]

    print(" Grand Total (Year) =", total, "\n")
while True:
    print("====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. Monthly Total")
    print("3. Yearly Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        monthly_total()

    elif choice == "3":
        yearly_total()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice\n")
