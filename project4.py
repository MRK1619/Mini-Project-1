#Simple Advanture Game

name=input("Type Your Name: ").upper()
print("Welcome ",name , "To This Advanture Game!")
answer=input("You Are On A Direct Road, It Has To Come An End And You Can Go Left Or Right... Which Way Would You Choose ..(Left/Right)? ").lower()

if answer=="left":
    answer=input("You Come To A River, You Can Walk Around It Or Swim Accross It... ? Type Walk To Walk And Swim To Swim Accross It..: ").lower() 
    if answer=="swim":
        print("You Swim Accross It And You Are Eaten By An Aalligator... You Lost The Game...")
    elif answer=="walk":
        print("You Walked For Many Miles....Ran Out Of Water And You Die...You Lost The Game")
    else:
        print("Not a Valid Option... You Lost The Game...")
             
elif answer == "right":
    answer=input("You Come To Bimasakti Strip...Do You Want To Go Inside Or Go Back (Inside/Back)? ").lower()
    if answer == "back":
        print("You Go Back And You Short  By Enimies...And You Lost The Game...")
    elif answer == "inside":
        answer = input("You Meet A Stranger Inside... Do You Like To Talk With Him(Yes/No)? ").lower()
        if answer == "yes":
            print("You Talk With The Stranger And They Give You Gold... You Win The Game...")
        elif answer == "no":
            print("You Ingnore The Stranger And You Did Not Get Anything And You Lost The Game...")    
        else:
            print("Not A Valid Option... You Lost The Game...")
    else:
        print("Not A Valid Option... You Lost The Game...")
else:
    print("Not A Valid Option... You Lost The Game...")

print("Thank You For Trying This Game", name)