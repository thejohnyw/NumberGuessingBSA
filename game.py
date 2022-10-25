'''
Number Guessing Game via Binary Search
'''
#No imports/dependencies; just raw code and logic :))

breaklines = "---------" #breaklines for new sections of the game
print("Play the Binary Search Guessing Game!")
print("The binary search algorithm (BSA) will try to guess your number!")
print("Indicate the range of your number ")

min_range = int(input("Min: "))
max_range = int(input("Max: "))
while min_range > max_range: #keep asking for new ranges if they're invalid
    print("Min can't be greater than max. Please enter new ranges")
    min_range = int(input("Min: "))
    max_range = int(input("Max: "))
 
num = int(input("Enter your number: ")) #num to guess
attempts = 1 #Attempt count of BSA
guess = (min_range+max_range)//2 #starting guess is middle point

inGame = True #boolean to tell if in game or not
while inGame:
    if guess == num: # correct guess case
        print("Guess #" + str(attempts) + ": " + str(guess))

        if attempts == 1:
            print("BSA GOT YOUR NUM IN ONE TRY; You must've picked the middle number!")
        else:
            print("BSA got your num in " + str(attempts) + " times!")
        key_input = input("Continue playing? y to play again; enter anything else to exit: ")

        if key_input == "y": #start new game with new numbers
            print(breaklines * 8 + "\n", "New Game", " \n" + breaklines * 8)
            min_range = int(input("Min: "))
            max_range = int(input("Max: "))
            num = int(input("Enter your number: "))
            attempts = 1

            if min_range > max_range: #error message when invalid range
                print("Min can't be more than max. Please enter new ranges")
                min_range = int(input("Min: "))
                max_range = int(input("Max: "))
                num = int(input("Enter in your number: "))
            else:
                guess = (min_range+max_range)//2 #initial guess

        else: #user clicks out of game; breaks loop
            inGame = False
    

    elif num < min_range: #error message and new game when invalid number
        print("Number to guess can't be smaller than min.")
        key_input = input("Keep going? Enter y for yes; enter any other key for no: ")

        if key_input == "y": #start new game
            print(breaklines * 8 + "\n", "New Game", " \n" + breaklines * 8)
            min_range = int(input("Min: "))
            max_range = int(input("Max: "))
            num = int(input("Enter your number: "))
            attempts = 1

            if min_range > max_range: #error message when invalid range
                print("Min can't be larger than max. Please enter new ranges")
                min_range = int(input("Min: "))
                max_range = int(input("Max: "))
                num = int(input("Type in your number: "))
            else:
                guess = (min_range+max_range)//2
        else: #user clicks out of game; breaks loop
            inGame = False

    elif num > max_range: #error message and new game when invalid number

        print("Number to guess can't be larger than max.")
        key_input = input("Play again? Enter y for yes; enter any other key to end: ")
        if key_input == "y": #starting new game
            print(breaklines * 8 + "\n", "New Game", " \n" + breaklines * 8)
            min_range = int(input("Min: "))
            max_range = int(input("Max: "))
            num = int(input("Enter your num: "))
            attempts = 1

            if min_range > max_range: #error message and new numbers
                print("Min can't be larger than max. Please enter new ranges")
                min_range = int(input("Min: "))
                max_range = int(input("Max: "))
                num = int(input("Enter in your number: "))
            else:
                guess = (min_range+max_range)//2 #initial guess

        else: #user clicks out of game; breaks loop
            inGame = False

    elif guess <= num: 
        print("Guess #" + str(attempts) + ": " + str(guess))
        min_range = guess + 1 #moving left binary search pointer up
        guess = (min_range+max_range)//2
        attempts += 1

    elif guess > num: 
        print("Guess #" + str(attempts) + ": " + str(guess))  
        max_range = guess - 1 #moving right binary search pointer down
        guess = (min_range+max_range)//2
        attempts += 1