#password manager
name = input("What Is Your Name ..")

def add():
    name = input('Account Name :')
    pwd = input("Password: ")
    
    with open('passwords.txt','a') as f: #for creating a new text file
        f.write(name + "|" + pwd + "\n") # for storing name and password
        
def view():
    with open('passwords.txt','r') as f: 
        for line in f.readlines():
            data =line.rstrip()
            print(line)
while True:
    mode = input("would you like to add a new password or view existing ones (view,add), press q to quit? ").lower()
    if mode =="q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
         print("Invalid Mode.")
         continue