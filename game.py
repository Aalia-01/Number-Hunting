import random

def guess_game():
    lucky_num = random.randint(1,50)

    while True:
        user_num=int(input("Enter your number: "))

        if user_num == lucky_num:
            print("You Won")
            break


        elif user_num < lucky_num:
            print("Your number is TOO LOW")  

        else:
            print("Your number is TOO HIGH")


    print("Thank You For Playing.")


guess_game()                 

