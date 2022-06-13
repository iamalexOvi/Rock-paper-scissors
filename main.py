import random #imports the random module and function

while True:
    poss_action = ['rock', 'paper', 'scissors']
    print("Please select operation -\n" \
        "R. Rock\n" \
        "S. Scissors\n" \
        "P. Paper\n" \
        )
    #take input from the user 
    user_input = input("Enter a choice (R, S, P): ")
    if user_input.lower() == 'r':
        user_choice = poss_action[0]
    elif user_input.lower() == 's':
        user_choice = poss_action[1]
    elif user_input.lower() == 'p':
        user_choice = poss_action[2]
    else:
        print('Sorry, you entered a wrong choice')
        #list of choice for the computer
    
    computer_choice = random.choice(poss_action)

    #prints both computer and user choice 
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    #this block of code determines outcome
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
  
    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        break
