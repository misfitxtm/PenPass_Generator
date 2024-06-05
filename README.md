# PenPass Generator

This is a simple password generator. Users can select the type of characters they want in their password and the desired length between 8 and 20 characters. The generated password can be copied to the clipboard for easy use. The purpose of this tool is to provide a secure, randomly generated password based on user preferences.

## Features

- Select character types for password:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Special characters (@-$)
  - Numbers (0-9)
- Choose password length between 8 and 20 characters
- Copy the generated password to the clipboard

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- `ttk` (Themed Tkinter widgets)

## Installation

### Linux

1. **Install Python 3 and Tkinter:**

    ```sh
    sudo apt update
    sudo apt install python3 python3-tk
    ```

2. **Clone the repository:**

    ```sh
    git clone https://github.com/misfitxtm/PenPass_Generator.git
    cd PenPass_Generator
    ```

3. **Run the program:**

    ```sh
    python3 penpass.py
    ```

### Windows

1. **Install Python 3:**

    Download and install Python 3 from the official [Python website](https://www.python.org/downloads/).

2. **Ensure Tkinter is installed:**

    Tkinter is included with Python by default. You can check if it is installed by running the following command in the Python shell:

    ```python
    import tkinter
    ```

    If you do not encounter any errors, Tkinter is installed.

3. **Clone the repository:**

    Open Command Prompt (cmd) and run:

    ```sh
    git clone https://github.com/misfitxtm/PenPass_Generator.git
    cd PenPass_Generator
    ```

4. **Run the program:**

    ```sh
    python penpass.py
    ```

## Usage

1. Run the program following the instructions above.
2. Select the desired character types by checking the boxes.
3. Adjust the slider to set the password length.
4. Click the "Generate" button to create a password.
5. The generated password will be displayed in the text box.
6. Click "Copy" to copy the password to your clipboard.

## Screenshots

![image](https://github.com/misfitxtm/PenPass_Generator/assets/38537232/746cf5e1-70d2-44c4-aa66-ae081443c106)


## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Created by Joshua Duane
- Inspired by the need for secure password generation
- Used for a Intro to Programming School project.

