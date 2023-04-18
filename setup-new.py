import argparse
import json
import os
import platform
import sys
import traceback
from datetime import datetime

import pytomlpp
from colorama import Back, Fore, Style

from compiler import Compiler


class Setup:
    # -----
    # Initialization and Configuration Functions
    # -----
    def __init__(self):
        # Configuration Variables
        self.config_file = "config.toml"

        # Read Config
        with open(self.config_file, "r") as f:
            toml_config = f.read()
            self.config = pytomlpp.loads(toml_config)

        # Setup Information Configuration
        self.setup_information = self.config["setup"]["information"]
        self.setup_name = self.setup_information["name"]
        self.setup_language = self.setup_information["language"]
        self.setup_version = self.setup_information["version"]
        self.setup_author = self.setup_information["author"]
        self.setup_description = self.setup_information["description"]
        self.setup_build = self.setup_information["build"]

        # Setup Style Configuration
        self.setup_style = self.config["setup"]["style"]

        # Setup Popup Configuration
        self.setup_style_info = self.setup_style["info"].upper()
        self.setup_style_error = self.setup_style["error"].upper()
        self.setup_style_warning = self.setup_style["warning"].upper()
        self.setup_style_success = self.setup_style["success"].upper()

        # Setup Input Configuration
        self.setup_style_input = self.setup_style["input"].upper()
        self.setup_style_yes_no = self.setup_style["yes_no"].upper()

        # Setup Asset Configuration
        self.setup_assets = self.config["setup"]["assets"]
        self.setup_assets_banner = ["banner"]

    # -----
    # Setup Functions
    # -----

    # Is running on Windows or Not
    def is_windows(self):
        """Check if the OS is Windows."""
        return platform.system() == "Windows"

    # Parse Arguments
    def parse_arguments(self):
        """Parse command-line arguments and return a dictionary of flags."""
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("-h", "--help", action="store_true")
        parser.add_argument("-nc", "--no-color", action="store_true")
        parser.add_argument("-ns", "--no-splash", action="store_true")
        parser.add_argument("-nb", "--no-banner", action="store_true")
        parser.add_argument("-nh", "--no-header", action="store_true")
        parser.add_argument("-np", "--no-pause", action="store_true")
        parser.add_argument("-ni", "--no-interface", action="store_true")
        parser.add_argument("-f", "--filename", nargs="?")
        args = parser.parse_args()
        return vars(args)

    # Error Handling
    def error_handling(self):
        """Handle errors."""
        error = traceback.format_exc()

        for line in error.split("\n"):
            if "File" in line or "line" in line or "in" in line:
                self.error(line.strip())

    # -----
    # Input and Output Functions
    # -----

    # Input Text
    def input_text(self, message):
        return input(f"        [>] {message} : ")

    # Input Yes or No
    def input_yes_no(self, message):
        pass

    # -----
    # Popup Functions
    # -----

    # Info
    def info(self, message):
        print(f"        [i] {message}")

    # Error
    def error(self, message):
        print(f"        [⚠] Error : {message}")

    # Warnings
    def warning(self, message):
        print(f"        [⚠] Warning : {message}")

    # Success
    def success(self, message):
        print(f"        [✓] Success : {message}")

    # -----
    # Splash Functions
    # -----

    # Splash
    def splash(self):
        pass

    # Banner
    def banner(self):
        pass

    # Header
    def header(self):
        pass

    # Clear
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    # Pause
    def pause(self):
        self.info("Press any key to continue...")

        if self.is_windows():
            os.system("pause >nul")
        else:
            input()

    # Leave
    def leave(self):
        try:
            self.pause()
            sys.exit()
        except Exception:
            exit()


class Color:
    @staticmethod
    def info():
        return f"{Fore}.{Setup.setup_style_info}"

    @staticmethod
    def error():
        return f"{Fore}.{Setup.setup_style_error}"

    @staticmethod
    def warning():
        return f"{Fore}.{Setup.setup_style_warning}"

    @staticmethod
    def success():
        return f"{Fore}.{Setup.setup_style_success}"

    @staticmethod
    def input():
        return f"{Fore}.{Setup.setup_style_input}"

    @staticmethod
    def yes_no():
        return f"{Fore}.{Setup.setup_style_yes_no}"


class EngLangSetup:
    def __init__(self, mode):
        # Setup Settings
        self.setup_mode = mode

        # User Settings
        self.ask_author = False
        self.ask_license = False

        # File Information
        self.name = None
        self.author = None
        self.license = None

        # File Variables
        self.englang_code = None
        self.python_code = None

    def __call__(self):
        if self.setup_mode == "cli":
            self.cli()

        elif self.setup_mode == "no-setup":
            self.no_setup()

    def cli(self):
        self.show_splash()
        self.show_info("Welcome to the EngLang Compiler Setup")
        self.pre_check()
        self.get_file_location()
        self.get_author()
        self.get_license()
        self.confirm_setup()
        self.compile_file()
        self.write_output()
        self.run_program()

    def no_setup(self):
        pass

    def show_splash(self):
        Setup.splash()

    def show_info(self, message):
        Setup.info(message)

    def pre_check(self):
        self.ask_author = Setup.input_yes_no(
            "Do you want to enter the author of the program?"
        )
        self.ask_license = Setup.input_yes_no(
            "Do you want to enter the license of the program?"
        )

    def get_file_location(self):
        while True:
            self.name = Setup.input_text("Enter the EngLang file location (.enlg)")
            if self.name == "":
                self.show_splash()
                self.show_error("The name of the file cannot be empty")
            elif not os.path.exists(self.name):
                self.show_splash()
                self.show_error(
                    "The file does not exist, please check the file location or typos in the name"
                )
            else:
                break
        self.show_splash()

    def get_author(self):
        if not self.ask_author:
            return
        while True:
            self.author = Setup.input_text("Enter the author of the program")
            if self.author != "":
                break
            self.show_splash()
            self.show_error("The author of the program cannot be empty")
            retry = Setup.input_yes_no("Do you want to retry?")
            if not retry:
                self.author = "None"
                break
        self.show_splash()

    def get_license(self):
        if not self.ask_license:
            return
        while True:
            self.license = Setup.input_text("Enter the license of the program")
            if self.license != "":
                break
            self.show_splash()
            self.show_error("The license of the program cannot be empty")
            retry = Setup.input_yes_no("Do you want to retry?")
            if not retry:
                self.license = "None"
                break
        self.show_splash()

    def confirm_setup(self):
        while True:
            self.show_info("Compiler has received the following information:")
            self.show_info(f"EngLang File : {self.name}")
            self.show_info(f"Author : {self.author}")
            self.show_info(f"License : {self.license}")
            if Setup.input_yes_no("Do you want to continue?"):
                break
            self.show_splash()
            self.show_error("Setup was terminated by the user")
        self.show_splash()
        self.show_info("Compiler is now compiling the file")

    def compile_file(self):
        with open(self.name, "r") as f:
            englang_code = f.read()
        compiled_code = Compiler(englang_code)[1]
        self.program_name = compiled_code[0]
        Setup.pause()
        self.show_splash()
        self.show_info("Compiler has finished compiling the file, writing to a file.")

    def write_output(self):
        output_folder = "./output/"
        output_filename = f"{self.program_name.lower()}.py"
        output_file = os.path.join(output_folder, output_filename)
        current_date = datetime.now().strftime("%Y-%m-%d")
        with open(output_file, "w") as f:
            f.write(
                f"# Name: {program_name.title()}\n# Author: {author}\n# Language: {language}\n# Compiled: {current_date}\n# Compiler: {compiler_name}\n# License: {license}\n\n"
            )
            f.write(compiled_code)

    def run_program(self):
        self.show_splash()
        self.show_info("Compiler has finished writing the file, running the program.")
        Setup.pause()
        self.show_splash()
        os.system(f"python {output_file}")


# Defining Variables
setup = Setup()

# Global Flags


def main():
    try:
        arguments = setup.parse_arguments()

        if arguments["help"]:
            # Display help message and exit.
            print("Help message goes here.")

        elif arguments["no-interface"]:
            # Handle --no-interface flag.
            print("Interface disabled.")

        filename = arguments["filename"]
        if filename is not None:
            # Use the provided filename.
            EngLangSetup(mode="cli", filename=filename, **arguments)

        else:
            # No filename provided.
            EngLangSetup(mode="cli", **arguments)

    except KeyboardInterrupt:
        setup.splash()

        setup.error("Setup was forced to terminate, you can always re-run the setup.")

    except Exception:
        setup.splash()

        setup.error_handling()

    finally:
        setup.leave()


if __name__ == "__main__":
    main()
