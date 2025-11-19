                                    # Banking System
balance = 0
running = True


# Main loop
while running:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    Choice = input("Enter Your Choice(1-4): ")

    if choice == "1":
        print(f"Your Balance is: ${balance:. 2f}")
    elif Choice == "2":
        amount = float(input("Enter amount to Deposit"))
        if amount > 0:
            balance += amount
            print(f"${amount}Deposit Successful!")
        else:
            print("Invalid amount. Please enter a positive number.")
    
    elif Choice == "3":
        amount = float(input("Enter amount to withdraw: $"))
        if amount > balance:
            print("Insufficient Funds!")
        elif amount <= 0:
            print("Invalid amount.Please enter a positive number")
        else:
            balance -= amount 
            print(f"${amount} Withdrawal Successful!")
    
    elif choice == "4":
        print("Thannk you for using our banking system.")
        running = False


    

