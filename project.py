#Simple Quiz Game
print("Welcome To My Quiz")

playing = input("Do You Want To Play? ")

if playing.lower() != "yes":
    quit()

print("Okey! Let's Play :)")
score = 0

answer = input("What Does CPU Stand For? ")
if answer.lower() =="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("What Is GPU Stands For? ")
if answer.lower() =="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What Is RAM Stands For? ")
if answer.lower() =="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("What Is ROM Stands For? ")
if answer.lower() =="read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("Who Is The Prime Minister Of India? ")
if answer.lower() =="narendra modi":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
print("You Give  " + str(score) +  "  Answer Correct!")
print("You Got  " + str(score*100/5) +  "%.")