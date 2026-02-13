def foo(word):
    # Reverses the string for comparison
    new_string = word.lower().strip()[::-1]
    if new_string == word:
        # Returns true
        return True
    # Checks if the reversed string is not the same as the original word
    if new_string != word:
        # Returns false
        return False
    # Returns none
    return None


def helloworld(balls):
    # initialize an empty string
    new_string = ''
    for x in balls.strip()[::-1]:
        new_string = new_string + x
    # returns the new string
    return new_string


def lolz(phrase):
    # imports the random module
    import random
    # Initialize empty string for return
    new_string = list(phrase)
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[0] = phrase[0].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[0] = phrase[0].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[1] = phrase[1].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[1] = phrase[1].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[2] = phrase[2].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[2] = phrase[2].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[3] = phrase[3].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[3] = phrase[3].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[4] = phrase[4].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[4] = phrase[4].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[5] = phrase[5].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[5] = phrase[5].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[6] = phrase[6].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[6] = phrase[6].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[7] = phrase[7].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[7] = phrase[7].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[8] = phrase[8].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[8] = phrase[8].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[9] = phrase[9].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[9] = phrase[9].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[10] = phrase[10].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[10] = phrase[10].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[11] = phrase[11].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[11] = phrase[11].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[12] = phrase[12].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[12] = phrase[12].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[13] = phrase[13].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[13] = phrase[13].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[14] = phrase[14].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[14] = phrase[14].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[15] = phrase[15].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[15] = phrase[15].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[16] = phrase[16].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[16] = phrase[16].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[17] = phrase[17].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[17] = phrase[17].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[18] = phrase[18].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[18] = phrase[18].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[19] = phrase[19].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[19] = phrase[19].lower()
    # Pick randomly between 0 and 1
    if random.randrange(2) == 1:
        # Capitalizes the letter
        new_string[20] = phrase[20].upper()
    # if it's 0:
    else:
        # lowercases the letter
        new_string[20] = phrase[20].lower()
    newer_string = "".join(new_string)
    # returns the newER string
    return newer_string


while True:
    string = input("Input a string: ")
    print("1. Check for palindrome\n"
          "2. Reverse word\n"
          "3. Randomcase")
    choice = input("Input a command: ")
    if choice == "1":
        result = foo(string)
        if result is not False:
            print(f'"{string}" is a palindrome.')
        if result is not True:
            print(f'"{string}" is not a palindrome.')
    if choice == "2":
        print(f'"{string}" reversed is {helloworld(string)}')
    if choice == "3":
        print(f'The result is: {lolz(string)}')




















        #                                           hi