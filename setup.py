import os
import platform
import sys
from datetime import datetime

from compiler import Compiler


class Color:
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WATER = (0, 191, 255)
    PURPLE = (128, 0, 128)
    YELLOW = (255, 255, 0)

    def __init__(self, color, r_step, g_step):
        self.color = color
        self.r_step = r_step
        self.g_step = g_step

    def __call__(self, text):
        os.system("")
        faded = ""
        for line in text.splitlines():
            r, g, b = self.color
            for character in line:
                faded += f"\033[38;2;{r};{g};{b}m{character}\033[0m"
                r += self.r_step
                g += self.g_step
                r = max(min(r, 255), 0)
                g = max(min(g, 255), 0)
        return faded


class Assets:
    @staticmethod
    def banner():
        return """
         _____             _                      
        | ____|_ __   __ _| |    __ _ _ __   __ _ 
        |  _| | '_ \ / _` | |   / _` | '_ \ / _` |
        | |___| | | | (_| | |__| (_| | | | | (_| |
        |_____|_| |_|\__, |_____\__,_|_| |_|\__, |
                     |___/                  |___/ 
        """

    @staticmethod
    def header():
        return f"""
        {name} {version} by {author}
        {description}
        {build}
            
        """


class Setup:
    def __init__(self):
        # Setup Variables
        self.banner = Assets.banner()
        self.header = Assets.header()

    # Setup Functions

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def pause(self):
        self.info("Press any key to continue...")

        if is_windows:
            os.system("pause >nul")
        else:
            input()

    def leave(self):
        try:
            self.pause()
            sys.exit()
        except Exception:
            exit()

    # Messages and Input Functions
    def input_text(self, message):
        input_msg = input(water(f"        [>] {message} : "))
        print(" ")
        return input_msg

    def input_yes_no(self, message):
        yes_or_no = input(yellow(f"        [?] {message} [y/n] : ")).lower()
        print(" ")

        if yes_or_no == "y":
            return True

        elif yes_or_no == "n":
            return False

        else:
            self.error("Invalid Input, must be a 'y' or 'n'")

    def info(self, message):
        print(blue(f"        [i] {message}"))
        print(" ")

    def error(self, error):
        print(red(f"        [⚠] Error : {error}"))
        print(" ")

    def splash(self):
        os.system("cls" if os.name == "nt" else "clear")

        # Print the Banner line by line
        for line in self.banner.splitlines():
            print(red(line))

        for line in self.header.splitlines():
            print(blue(line))


# Setup Information
name = "Compiler"
version = "v0.0.1-alpha"
author = "MostlyWhat Systems"
description = "Setup for the EngLang Compiler"
build = f"April 2023 Build - Running on Python {platform.python_version()}"

language = "EngLang"

full_name = f"{name} {version} by {author} - {description}"
compiler_name = f"{language} {name} {version} by {author}"

# Check if the OS is Windows
is_windows = platform.system() == "Windows"

if is_windows:
    os.system(f"title {full_name}")

# Setup Variables
setup = Setup()
compiler = Compiler

# Colors
red = Color(Color.RED, 0, -5)
blue = Color(Color.BLUE, 0, 3)
water = Color(Color.WATER, 0, 15)
purple = Color(Color.PURPLE, 3, -3)
yellow = Color(Color.YELLOW, 0, -3)


def interface():
    setup.splash()

    # Setup Information
    setup.info("Welcome to the EngLang Compiler Setup")

    # Setup Pre-Check
    ask_author = setup.input_yes_no("Do you want to enter the author of the program?")
    ask_license = setup.input_yes_no("Do you want to enter the license of the program?")

    setup.splash()

    while True:
        name = setup.input_text("Enter the EngLang file location (.enlg)")
        if name == "":
            setup.splash()
            setup.error("The name of the file cannot be empty")
        elif not os.path.exists(name):
            setup.splash()
            setup.error(
                "The file does not exist, please check the file location or typos in the name"
            )
        else:
            break

    setup.splash()

    if ask_author:
        while True:
            author = setup.input_text("Enter the author of the program")
            if author == "":
                setup.splash()
                setup.error("The author of the program cannot be empty")

                retry = setup.input_yes_no("Do you want to retry?")

                if retry:
                    continue

                else:
                    author = "None"
                    break

            else:
                break

    setup.splash()

    if ask_license:
        while True:
            license = setup.input_text("Enter the license of the program")
            if license == "":
                setup.splash()
                setup.error("The license of the program cannot be empty")

                retry = setup.input_yes_no("Do you want to retry?")

                if retry:
                    continue

                else:
                    license = "None"
                    break

            else:
                break

    setup.splash()

    # Setup Confirmation
    while True:
        setup.info("Compiler has received the following information:")

        setup.info(f"EngLang File : {name}")
        setup.info(f"Author : {author}")
        setup.info(f"License : {license}")

        if setup.input_yes_no("Do you want to continue?"):
            break

        setup.splash()

        setup.error("Setup was terminated by the user")

    setup.splash()

    setup.info("Compiler is now compiling the file")

    with open(name, "r") as f:
        englang_code = f.read()

    # Compile the file
    compiled_code = compiler(englang_code)[1]
    program_name = compiled_code[0]

    setup.pause()

    setup.splash()

    setup.info("Compiler has finished compiling the file, writing to a file.")

    output_folder = "./output/"
    output_filename = f"{program_name.lower()}.py"
    output_file = os.path.join(output_folder, output_filename)
    current_date = datetime.now().strftime("%Y-%m-%d")

    with open(output_file, "w") as f:
        f.write(
            f"# Name: {program_name.title()}\n# Author: {author}\n# Language: {language}\n# Compiled: {current_date}\n# Compiler: {compiler_name}\n# License: {license}\n\n"
        )
        f.write(compiled_code)

    setup.pause()

    setup.splash()

    setup.info(f"Compiler has written to the file {output_file}")

    if setup.input_yes_no("Would you like to run the program?"):
        try:
            os.system(f"python {output_file}")

        except Exception as e:
            setup.error(f"An error occurred while running the program: {e}")

    setup.info("Thank you for using the EngLang Compiler Setup")


def no_setup(filename):
    os.system("cls" if os.name == "nt" else "clear")


def main():
    try:
        if "--no-setup" in sys.argv:
            # Find Flag --file for the filename
            if "--file" in sys.argv:
                # Find the index of the flag
                index = sys.argv.index("--file")

                # Get the filename
                try:
                    filename = sys.argv[index + 1]
                except IndexError:
                    setup.error("Please specify a filename")

                # Compile the file
                no_setup(filename)

            else:
                setup.error("Please specify a file to read using --file <filename>")

        else:
            interface()

    except KeyboardInterrupt:
        setup.splash()

        setup.error("Setup was forced to terminate, you can always re-run the setup.")

    except Exception as e:
        setup.splash()

        setup.error(f"An error occurred while running the setup: {e}")

    finally:
        setup.leave()


if __name__ == "__main__":
    main()
