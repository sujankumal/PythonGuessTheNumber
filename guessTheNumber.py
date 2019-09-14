attempts = 0
def matchValue(random_number_generated, user_input):
    try:
        user_value = int(user_input)
        # its integer
        if user_value < 1 or user_value > 100:
            print("Please input number between 1 to 100 or 'q' to quit")
            return 1
        if random_number_generated == user_value:
            print("Correct guess. Total Attempts:", str(attempts))
            return 0
        else:
            print("Sorry not matched. Please try again. Attempts: ", str(attempts), "\n")
            return 2
    except ValueError:
        # its string
        if str(user_input).lower() == 'q':
            print("User Quit. Attempts:", str(attempts))
            return -1
        else:
            print("Invalid Input. Please try again")
            return 3

if __name__ == "__main__":
    # library for random
    import random as r
    random_number_generated = r.randrange(1, 101)
    print(random_number_generated)
    while True:
        user_input = input("Please input a number between 1 to 100.\n")
        attempts += 1
        continue_loop = matchValue(random_number_generated, user_input)
        if continue_loop == 0 or continue_loop == -1:
            break