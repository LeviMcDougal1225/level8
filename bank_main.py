
from BankAccount import BankAccount

customer_name = input("Enter your name: ")

customer_account = BankAccount(customer_name)

# Keeps showing the banking menu until the customer quits

while True: 

    print("Please choose from the folowing options: \n1. Make a deposit \n2. Make a withdrawal \n3. View account information \n4. Quit")

    try:
        choice = int(input("Please enter your choice here: "))

    except ValueError:
        print("Invalid choice. Please try again.")
        continue

    if choice == 1:

        deposit_amount = float(input("How much would you like to deposit? "))

        customer_account.deposit(deposit_amount)

    elif choice == 2:

        withdrawal_amount = float(input("How much would you like to withdraw? "))

        customer_account.withdraw(withdrawal_amount)

    elif choice == 3:

        customer_account.view_account()

    # Ends program when they are done

    elif choice == 4:
            print("Thank you for your business!")
            break

    else:

        print("Invalid choice. Please try again.")
                        















    


    































