import random
print("WELCOME TO MADLIBS")
print("Enter the following words to get your madlibs story")
Animals=['elephant','dog','cat','fox']
place=['forest','zoo','shopping mall']
expression=['shocked','suprised']
while True:
    Adjective1 = input("Enter an Adjective: ")
    Adjective2 = input("Enter another Adjective: ")
    Adjective3 = input("Enter another Adjective: ")
    Adjective4 = input("Enter another Adjective: ")
    Noun = input("Enter a Noun: ")
    Noun1 = input("Enter another Noun (place or thing): ")
    random_place=random.choice(place)
    random_animal=random.choice(Animals)
    random_expression=random.choice(expression)

    print("Your Mad Libs Story ")
    print(f"Today I went to a {Adjective1} {random_place}.")
    print(f"There, I saw a {Noun} and {random_animal} which are very {Adjective2}.")
    print(f"After seeing them, I felt {Adjective3} and {random_expression}.")
    print(f"Finally, after roaming around the {random_place}, I was {Adjective4} and went to the {Noun1}.")

    choice=input("DO YOU WANT TO PLAY AGAIN(YES/NO)").lower()
    if choice!="no":
        continue
    else:
        print("THANK YOU FOR PLAYING")
        break

