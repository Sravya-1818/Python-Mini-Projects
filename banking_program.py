import pwinput
def show_balance(balance):
    print("***********************")
    print(f"Your balance is ${balance:.2f}")
    print("***********************")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("***********************")
        print("That's not a valid amount")
        print("***********************")
        return 0
    else:
        return amount

def withdrawal(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("***********************")
        print("Insufficient funds")  
        print("***********************")
        return 0
    else:
        return amount

def set_pin():
    PIN = pwinput.pwinput(prompt="Enter your new PIN number: ",mask="*")
    return PIN

def main():    
    correct_pin ="1234"
    balance = 0
    is_running = True

    while is_running:
        print("\n***********************")
        print("********BANKING********")
        print("***********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Set PIN")
        print("5. Exit")
        print("***********************")

        choice = input("Enter your choice (1-5): ")

        if choice in ['1', '2', '3']:
            pin = pwinput.pwinput(prompt="Enter your PIN number: ",mask="*")
            if pin == correct_pin:
                if choice == '1':
                    show_balance(balance)
                elif choice == '2':
                    balance += deposit()
                elif choice == '3':
                    balance -= withdrawal(balance)
            else:
                print("***********************")
                print("INVALID PIN NUMBER")
                print("1. TRY AGAIN")
                print("2. RESET PIN")
                print("***********************")
                sub_choice = input("Enter your choice (1 or 2): ")
                if sub_choice == '1':
                    continue
                elif sub_choice == '2':
                    correct_pin = set_pin()
                else:
                    is_running = False

        elif choice == '4':
            correct_pin = set_pin()
        elif choice == '5':
            is_running = False
        else:
            print("***********************")
            print("Invalid choice (Error)")
            print("***********************")

    print("***********************")
    print("Thank you. Have a nice day!")
    print("***********************")

if __name__ == '__main__':
    main()
