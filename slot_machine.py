import random
import time  # For adding delay

symbols = ["🍒", "⭐", "🔔", "🍉", "🍋"]

def spin_row():
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_pay(result, bet):
    if result[0] == result[1] == result[2]:
        print("🎉 YOU WON!")
        if result[0] == "🍒":
            return bet * 3
        elif result[0] in ["⭐", "🔔", "🍉"]:
            return bet * 2
        else:
            return bet * 1
    else:
        return 0

def main():
    print("🎰 WELCOME TO PYTHON SLOT GAME 🎰")
    print("SYMBOLS: 🍒 ⭐ 🔔 🍉 🍋")
    balance = 100

    while balance > 0:
        print(f"\nYour Balance: ${balance}")
        bet = input("Enter your bet amount (or type 'q' to quit): ")

        if bet.lower() == 'q':
            print("Thanks for playing! 👋")
            break

        if not bet.isdigit():
            print("❌ INVALID INPUT. Please enter a positive number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("❌ Insufficient balance.")
            continue
        if bet <= 0:
            print("❌ Invalid bet. It should be greater than 0.")
            continue

        balance -= bet
        print("........Spinning 🎲")
        time.sleep(1)  # Adds a pause for effect
        result = spin_row()
        print_row(result)

        payout = get_pay(result, bet)
        if payout > 0:
            print(f"💰 You won: ${payout}")
            balance += payout
        else:
            print("😢 Better luck next time.")

    if balance <= 0:
        print("💸 Game Over! You are out of balance.")

if __name__ == '__main__':
    main()
