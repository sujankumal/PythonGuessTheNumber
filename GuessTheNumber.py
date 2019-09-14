# library for random
import random as r
attempts = 0
random_number_generated = r.randrange(1, 101)
print(random_number_generated)
while True:
    user_input = input("Please input a number between 1 to 100.\n")
    attempts += 1
    try:
        val = int(user_input)
        # its integer
        if val < 1 and val >100:
            print("Please Input between 1 to 100")
            continue
        if random_number_generated == val:
            print("Correct guess. Total Attempts:", str(attempts))
            break
        else:
            print("Sorry not matched. Please try again. Attempts: ", str(attempts), "\n")
    except ValueError:
        # its string
        if str(user_input).lower() == 'q':
            print("User Quit. Attempts:",str(attempts))
            break
        else:
            print("Invalid Input. Please try again")
