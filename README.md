# Random Password Generator

## Overview
This project is a **Random Password Generator** developed as the final project for a 4-week Python course. The program generates secure, random passwords based on user-defined specifications such as total password length, the number of letters, digits, and special characters. It also provides the option to save the password in a `.txt` file and measures the time taken to generate the password.

The code was written in 2 days as part of a programming exercise, and includes various future plans for improvements, such as a GUI, password strength checker, and multi-language support.

## Features
- **User-defined password length**: The user can choose the length of the password or allow the program to default to a 30-character password
- **Customizable character composition**: The user can specify how many letters, digits, and special characters the password should contain (can also be zero)
- **Random character assignment**: If the user leaves certain inputs blank, random values are assigned
- **ASCII Art**: Displays decorative ASCII art at different stages of the program using the [patorjk.com website](https://patorjk.com/software/taag)
- **Runtime Measurement**: Measures the time taken to generate the password
- **File Storage**: The generated password is saved as a `.txt` file in the same directory
- **Error Handling**: Ensures that user inputs are valid and prevents invalid passwords from being generated

## Dependencies
- **Python 3.x**
- **colorama** (for colored terminal output):
    - Install using `pip install colorama`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MaurizeDev/Python-RandomPasswordGenerator/
    ```

2. Install the required dependencies:
    ```bash
    pip install colorama
    ```

3. Run the Python script:
    ```bash
    python password_generator.py
    ```

## How to Use

1. **Run the Program**: The program will display a cover photo and prompt the user to enter specifications for the password
2. **Specify the Password Length**: The user can either enter the desired password length or press Enter to default to a 30-character password
3. **Customize the Password**: The user can choose how many letters, digits, and special characters the password should contain. If the user presses Enter, the program will choose random values within the allowed range
4. **View the Generated Password**: Once the password is generated, it is displayed in the console, and the runtime is measured
5. **Save the Password**: The password is automatically saved in a `.txt` file in the same directory. The file includes the password, the login (provided by the user), and the date and time of generation

## Example Output

```
╦ ╦┌─┐┬ ┬┬─┐  ┌┐┌┌─┐┬ ┬  ┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐
╚╦╝│ ││ │├┬┘  │││├┤ │││  ├─┘├─┤└─┐└─┐││││ │├┬┘ ││
 ╩ └─┘└─┘┴└─  ┘└┘└─┘└┴┘  ┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘

for "Amazon" is: bWfOsPbAbrii=hohl&WorL?TG[qjBs
```

## Future Plans
- **GUI**: Add a graphical user interface (GUI) to improve user experience
- **Password Strength Checker**: Implement a system to check the strength of the generated password (e.g., detecting repeated characters, ensuring sufficient complexity)
- **Human Readability**: Option to add dashes to improve readability without compromising security (e.g., `j3dh5-o$3jr-k3o0f`)
- **Decryption Feature**: Add functionality to decrypt stored passwords
- **Multi-language Support**: Expand to support multiple languages for broader usability
- **Generate Seed Phrases**: Add functionality to generate crypto seed phrases and other related tasks
- **Comment Option**: Allow users to add a comment about the password's purpose, which is also saved in the `.txt` file

## Acknowledgments
- ASCII Art generated using [patorjk.com](https://patorjk.com/software/taag) (Font: Calvin S)
