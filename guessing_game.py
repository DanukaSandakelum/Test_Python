import time

def get_ran_num(min_value, max_value, guess_number):
    current_time = time.time()
    microsecond_time = current_time * 1000000

    range_size = max_value - min_value + 1
    number = microsecond_time % range_size

    final = int(number) + min_value

    if guess_number == final:
        print("You win!")
        return True  
    else:
        print(f"Try again ****. Our number is: {final}, your number is: {guess_number}")
        return False 


print("Enter your range of numbers:")

min_value = int(input("Enter your min value^^^^: "))
max_value = int(input("Enter your max value ^^^^: "))
guess_number = int(input("Enter your guessing number ^^^^: "))


while True:
    if get_ran_num(min_value, max_value, guess_number):
        break  
    guess_number = int(input("Guess again: ")) 
