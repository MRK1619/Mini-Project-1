#Number Guassing Game
import random

top_of_range = input("Type a Number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range<=0:
        print("Please Type A Number Larger Than 0 Next Time:")
        quit()
else:
    print("Please Type A Number Next Time.")
    quit()

random_number =random.randint(0,top_of_range)
guesses =0

while True:
    guesses += 1
    User_guess = input("MAke a Guess: ")
    if User_guess.isdigit():
        User_guess=int(User_guess)
    else:
        print("please type a number next time.")   
        continue
    
    if User_guess==random_number:
        print("you got it!")
        break
    else:
        if User_guess>random_number:
            print("you were baove the number!")
        else:
            print("you were below the number!")

print("you got it in", guesses, "guesses")
 