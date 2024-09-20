# Final project Python (July 2024)
# Random Password Generator: Generates random password, safes password as .txt-file, measures runtime
# 4-week Python course, 2 days time for writing this code

import random
import time
from datetime import datetime
from colorama import Fore, Style

cover_photo = r"""
╦═╗┌─┐┌┐┌┌┬┐┌─┐┌┬┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
╠╦╝├─┤│││ │││ ││││  ╠═╝├─┤└─┐└─┐││││ │├┬┘ ││  ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
╩╚═┴ ┴┘└┘─┴┘└─┘┴ ┴  ╩  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘  ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─

This AI powered algorithm generates strong random passwords with predefined length, number of letters, digits and special chars
"""  # Cover Photo, https://patorjk.com/software/taag (Font Name: Calvin S)

print(cover_photo)

# Character collections from which random characters are later selected
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
           "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H",
           "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

special_chars = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":",
                 ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]


def get_valid_number_or_default(prompt, default=None):
    """
    Prompts the user for a number. If the user presses Enter without input, returns the default value.
    If the user enters a valid number, returns the number.
    Args:
        prompt (str): The message displayed to the user when asking for input.
        default (int or None): The default value to return if the user presses Enter without input.
    Returns:
        int: A valid integer input by the user, or the default value.
    Raises:
        ValueError: If the user does not input a valid integer and does not press Enter for default.
    """
    while True:
        user_input = input(prompt)
        if user_input == "" and default is not None:
            return default
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def user_password_specifications():
    """Ask user for specifications of the password - total length, number of letters, digits & special chars.
    If the user leaves input blank, default/random values are selected.
    Returns specifications for next function."""

    # Set default password length to 30 if the user presses Enter without input
    password_length = get_valid_number_or_default(
        f"Enter desired password total {Fore.BLUE}LENGTH{Style.RESET_ALL} (Enter for default 30): -> ", 30)

    # Generate random values for letters, digits, and special characters if user presses Enter
    remaining_length = password_length

    number_letters = get_valid_number_or_default(
        f"How many {Fore.BLUE}LETTERS{Style.RESET_ALL} should the password contain? (Enter for random): -> ",
        random.randint(1, remaining_length))
    remaining_length -= number_letters

    number_digits = get_valid_number_or_default(
        f"How many {Fore.BLUE}DIGITS{Style.RESET_ALL} should the password contain? (Enter for random): -> ",
        random.randint(0, remaining_length))
    remaining_length -= number_digits

    number_special_chars = get_valid_number_or_default(
        f"How many {Fore.BLUE}SPECIAL CHARACTERS{Style.RESET_ALL} should the password contain? (Enter for random): -> ",
        remaining_length)

    # Check if the sum of letters, digits, and special characters exceeds the password length
    if number_letters + number_digits + number_special_chars > password_length:
        raise ValueError("Sum of letters, digits, and special characters exceeds password length")

    return password_length, number_letters, number_digits, number_special_chars


def generate_password(letters, digits, special_chars):
    """
    Generates a random password based on user specifications.
    Args:
        letters (list): A list of possible letters for the password.
        digits (list): A list of possible digits for the password.
        special_chars (list): A list of possible special characters for the password.
    Returns:
        tuple: The generated password and the start time of the password generation.
    """
    # Get user-defined password specifications (length, number of letters, digits, and special characters)
    password_length, number_letters, number_digits, number_special_chars = user_password_specifications()

    # Check: At least one of the groups (letters, digits, or special characters) must be greater than 0
    if number_letters == 0 and number_digits == 0 and number_special_chars == 0:
        raise ValueError("Cannot generate a password with 0 letters, 0 digits, and 0 special characters.")

    start_time = time.time()  # Record the start time of password generation
    picked_letters = []  # Initialize the list to store the selected characters

    # Add the desired number of letters
    for _ in range(number_letters):
        picked_letters.append(random.choice(letters))

    # Add the desired number of digits
    for _ in range(number_digits):
        picked_letters.append(random.choice(digits))

    # Add the desired number of special characters
    for _ in range(number_special_chars):
        picked_letters.append(random.choice(special_chars))

    # Fill the remaining characters until the desired password length is reached
    while len(picked_letters) < password_length:
        if number_letters > 0:  # only if user wants letters
            picked_letters.append(random.choice(letters))
        if len(picked_letters) < password_length and number_digits > 0:  # only if user wants digits
            picked_letters.append(random.choice(digits))
        if len(picked_letters) < password_length and number_special_chars > 0:  # only if user wants special characters
            picked_letters.append(random.choice(special_chars))

    # Shuffle the characters and trim if the list exceeds the password length
    random.shuffle(picked_letters)
    picked_letters = picked_letters[:password_length]

    password = ''.join(picked_letters)  # Join the characters to form the final password
    return password, start_time  # Return the generated password and the start time


def print_results():
    """Calls "generate_password()" function and print results with beautiful ASCII image.
    Returns the password and login variable for the next function to safe it as txt"""
    login = input(
        f"For which {Fore.BLUE}LOGIN{Style.RESET_ALL} do you need this password? -> ")
    password, start_time = generate_password(letters, digits, special_chars)
    print("\n" + 80 * '─')
    print(r"""╦ ╦┌─┐┬ ┬┬─┐  ┌┐┌┌─┐┬ ┬  ┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐
╚╦╝│ ││ │├┬┘  │││├┤ │││  ├─┘├─┤└─┐└─┐││││ │├┬┘ ││
 ╩ └─┘└─┘┴└─  ┘└┘└─┘└┴┘  ┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘""")  # https://patorjk.com/software/taag (Font Name: Calvin S)
    print(f"for \"{login}\" is: {Fore.BLUE}{password}{Style.RESET_ALL}")  # todo: login name in ASCII image :D
    return password, login, start_time


def save_password_to_txt(password, login, start_time):
    """Safe generated password in a .txt file in the same directory as the running script"""
    filename = f"Password_{login}.txt"
    now = datetime.now().strftime("%B %d, %Y at %H:%M:%S")
    with open(filename, 'w') as file:
        file.write(f"Login: {login}\n")
        file.write(f"Password: {password}\n\n")
        file.write(f"Generated: {now}\n\n")
    end_time = time.time()
    runtime = end_time - start_time  # runtime above 1 second with password length of >3_000_000 chars
    print(f"\n>> Password saved to \"{filename}\" | Runtime:", round(runtime, 5), "seconds")
    # todo: Maybe not create new file, but write every new password in same file.
    # todo: Append new passwords for same login or simply overwrite old passwords? -> TBD


def start_program():
    """Start the program by calling the "print_results()" function, which in turn calls all other functions above.
    Also calls "save_password_to_txt()" function to safe the generated password to .txt"""
    final_password, login, start_time = print_results()
    save_password_to_txt(final_password, login, start_time)


start_program()  # no explanation needed

# todo: GUI

# todo V2: Check how strong is the generated password and give recommendations
#  e. g. 3x the same character in a row -> not secure. Or same char too often in entire password -> generate new
#  or number of chars too low -> not secure

# todo V2: Add dashes for better human readability, security should remain the same -> j3dh5-o$3jr-k3o0f
# todo V2: Decryption
# todo V2: multi language
# todo V3: multi purpose: generate crypto seed phrases and more
# todo V3: allow user to add a comment (optional) which is also safed in .txt
