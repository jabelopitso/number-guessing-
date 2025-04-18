import random

# def correct_guess(user_input):
#     user_input = input("guess your number? ")
    
#     random_number = 7
    
#     if user_input == 5:
#         return "too low"
#     elif user_input == 9:
#         return "Too high"
#     else:
#         return "correct"
    


def guess_number(user_guess):
    secret_number = random.randint(1,10)
    if user_guess == secret_number:
        return "Correct"
    elif user_guess<secret_number:
        return "Too low"
    else:
        return "Too high"