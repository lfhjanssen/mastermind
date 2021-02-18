# Welcome to MasterMind! You will play against the computer :)
import random

code = [(random.randint(0, 9)), (random.randint(0, 9)), (random.randint(0, 9))]
error = "Something went terribly wrong. Only enter digits please."
print('Welcome to MasterMind!')


def game():
    try:
        input_string = input('Enter 3 digits between 0 and 9 separated by a space: ')
        user_code = input_string.split()
        user_code = list(map(int, user_code))
        user_guess = ['x', 'x', 'x']
        print('Your entry is: ', user_code)
        print("Let's check the code ...\n")
        if user_code[0] == code[0]:
            print('First digit is correct')
            user_guess[0] = user_code[0]
        elif user_code[0] == code[1]:
            print('First digit is in the code, but in the wrong place')
        elif user_code[0] == code[2]:
            print('First digit is in the code, but in the wrong place')
        if user_code[1] == code[1]:
            print('Second digit is correct')
            user_guess[1] = user_code[1]
        elif user_code[1] == code[2]:
            print('Second digit is in the code, but in the wrong place')
        elif user_code[1] == code[0]:
            print('Second digit is in the code, but in the wrong place')
        if user_code[2] == code[2]:
            print('Third digit is correct\n')
            user_guess[2] = user_code[2]
        elif user_code[2] == code[1]:
            print('Third digit is in the code, but in the wrong place\n')
        elif user_code[2] == code[0]:
            print('Third digit is in the code, but in the wrong place\n')
        print(f'Your code so far: {user_guess}\n')
        if user_code[0] == code[0] and user_code[1] == code[1] and user_code[2] == code[2]:
            print("You've cracked the code! We're all done for now.")
            return
        game()
    except:
        print(error)
        game()


game()
