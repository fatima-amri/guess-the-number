import random
while True:
    a= random.randint(1,9);
    b= int(input("enter your guess: "))
    if a == b:
        print("exactly right :) ")
        print(a)
        if input("enter exit to quit the game = ") == "exit" :
            break
        else:
            continue
           
    elif a != b:
        if a<b:
            print("your guess is high")
            print(a)
        elif a>b:
            print("your guess is low ")
            print(a)
        if input("enter exit to quit the game = ") == "exit" :
            break
        else:
            continue

