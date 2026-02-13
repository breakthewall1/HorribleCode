import random


def check_palindrome(string):
    # Reverses the string for comparison
    reverse = string.lower().strip()[::-1]
    if reverse == string:
        return True
    else:
        return False


def reverse(string):
    # Reverses the string and instantly returns it
    return string.strip()[::-1]


def randomcase(string):
    # Initialize empty string for return
    new_string = ''
    for x in string:
        # Pick randomly between 0 and 1
        if random.randrange(2) == 1:
            new_string += x.upper()
        else:
            new_string += x.lower()
    return new_string


# Initialize a loop for inputs
while True:
    string = input("Input a string: ")
    print("1. Check for palindrome\n"
          "2. Reverse word\n"
          "3. Randomcase")
    choice = input("Input a command: ")
    # Match-Case to check for inputs
    match choice.strip():
        case "1":
            result = check_palindrome(string)
            if result:
                print(f'"{string}" is a palindrome.')
            else:
                print(f'"{string}" is not a palindrome.')
        case "2":
            print(f'"{string}" reversed is {reverse(string)}')
        case "3":
            print(f'The result is: {randomcase(string)}')
        # Handles choices outside the given commands
        case _:
            print("Invalid input.")
