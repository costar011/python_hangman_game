from random import *  
vocabulary = ["castle", "wrong", "sand", "chat",
              "brain", "target", "import"]  
words = choice(vocabulary)  
write = "" 


while True:
    succeed = True  
    print()
    for v in words: 
        if v in write:  
            print(v, end=" ")  
        else:  
            print("_", end=" ")  
            succeed = False  
    print()

    if succeed:  
        print("✅")
        break

    letter = input("Input Word >>>  ")  
    if letter not in write:  
        write += letter  

    if letter in words:  
        print("⭕️")
    else:   
        print("❌")
