import random

print("-------------------------------------------------------------------------------------")
print("----------------------------WELCOME TO NUMBER GUESSING GAME--------------------------")
print("-------------------------------------------------------------------------------------")

lowest_number = 1
highest_number = 100

while True:
    number = random.randint(lowest_number, highest_number)
    guesses = 0
    print(f"I HAVE PICKED A NUMBER BETWEEN {lowest_number} AND {highest_number}. TRY TO GUESS IT...")

    while True:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess > number:
                print("YOUR GUESS IS HIGHER THAN REQUIRED. TRY A LOWER ONE!")
            elif guess < number:
                print("YOUR GUESS IS LOWER THAN REQUIRED. TRY A HIGHER ONE!")
            else:
                print("\YAYYYYY............!!!!!!!!!!!")
                print("YOU HAVE GUESSED THE CORRECT NUMBER")
                print(f"YOUR GUESS IS: {guess}")
                print(f"YOU HAVE GUESSED IT IN {guesses} ATTEMPTS")

                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes":
                    break  
                elif play_again == "no":
                    print("Thanks for playing!")
                    exit()  
                else:
                    print("Invalid choice. Exiting game.")
                    exit()
        else:
            print("Invalid input! Please enter a number.")

 

   

    
