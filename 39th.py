balance = 1000
print("1.Check Balance")
print("2.Deposit")
print("3.Withdraw")
choice = int(input("Enter your choice:"))
if choice ==1:
    print("Balance = ",balance)
elif choice ==2:
    amount = float(input("Enter amount to deposit:"))
    balance += amount
    print("New Balance = ",balance)
elif choice ==3:
    amount = float(input("Enter amount to withdraw:"))
    if amount <= balance:
        balance -= amount
        print("New Balance = ",balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid choice")
