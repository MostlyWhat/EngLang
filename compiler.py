import os
import re
from datetime import datetime


# The EngLangConverter class contains static methods for converting code written in a custom
# English-like language to Python syntax.
class EngLangConverter:
    @staticmethod
    def convert(code):
        """
        The function converts a given code from a custom English-like language to Python.

        :param code: a string containing the code to be converted from English-like syntax to Python
        syntax
        :return: The `convert` method is returning a string that represents the converted code.
        """
        code = code.replace("PROGRAM", "").replace("END PROGRAM", "").strip()
        code = EngLangConverter.replace_import(code)
        code = EngLangConverter.replace_init(code)
        code = EngLangConverter.replace_class_with_indent(code)
        code = EngLangConverter.replace_function_with_indent(code)
        # code = EngLangConverter.convert_keywords(code)
        code = EngLangConverter.convert_set_statements(code)
        code = EngLangConverter.convert_if_statements(code)
        code = EngLangConverter.convert_while_statements(code)
        code = EngLangConverter.convert_for_statements(code)
        code = EngLangConverter.convert_comparison_statements(code)
        code = EngLangConverter.convert_arithmetic_ops(code)
        code = EngLangConverter.replace_display(code)
        code = EngLangConverter.replace_new_and_return_and_end(code)
        code = EngLangConverter.convert_variables_to_type(code)

        lines = code.split("\n")
        output_lines = []

        for line in lines:
            if line.startswith("    "):
                line = line[4:]
            if line.strip() == "" and output_lines and output_lines[-1].strip() == "":
                continue
            output_lines.append(line)

        return "\n".join(output_lines)

    @staticmethod
    def get_program_name(code):
        """
        The function extracts the name of a program from a given code.

        :param code: a string that represents the source code of a program written
        in a programming language.
        :return: the program name as a string, or None if not found.
        """
        print("[ EngLang Compiler] Getting program name...")
        program_line = code.split("\n")[0]
        program_name = program_line.replace("PROGRAM", "").strip()
        return program_name if program_name else None

    @staticmethod
    def replace_import(code):
        """
        This function replaces "IMPORT" statements in Python code with "from [module] import *".

        :param code: a string containing the code to be compiled
        :return: the modified code with import statements replaced using regular expression.
        """
        print("[ EngLang Compiler ] Replacing import statements...")
        return re.sub(r"IMPORT (.+)", r"from \1 import *", code)

    @staticmethod
    def replace_init(code):
        """
        This function replaces "INIT" statements in a given code with a Python class constructor
        "__init__" statement.

        :param code: a string containing the code to be compiled
        :return: the modified code with the "INIT" statements replaced with a Python class constructor
        "__init__" method.
        """
        print("[ EngLang Compiler ] Replacing init statements...")
        return re.sub(r"INIT (.+)", r"def __init__(self, \1):", code)

    @staticmethod
    def replace_class_with_indent(code):
        """
        This function replaces "CLASS" statements with "class" and removes "END CLASS" in a given code.

        :param code: The input code that needs to be processed and have class statements replaced with
        Python syntax
        :return: the modified code with the class statements replaced with Python syntax.
        """
        print("[ EngLang Compiler ] Replacing class statements...")
        return re.sub(r"CLASS (.+)", r"class \1:", code).replace("END CLASS", "")

    @staticmethod
    def replace_function_with_indent(code):
        """
        The function replaces function statements in a given code with properly indented Python function
        definitions.

        :param code: a string containing the code to be processed and modified by the function
        :return: the modified code with the function statements replaced with Python function
        definitions.
        """
        print("[ EngLang Compiler ] Replacing function statements...")
        functions_re = r"(FUNCTION (.+) TAKES (.+)([\s\S]+?))(?=FUNCTION|END PROGRAM)"
        function_definitions = re.findall(functions_re, code)

        for function_block, function, parameters, function_body in function_definitions:
            inside_class = re.search("class [\s\S]+?" + function_block, code)
            new_parameters = f"self, {parameters}" if inside_class else parameters
            new_function = f"def {function}({new_parameters}):"
            code = code.replace(function_block, new_function + function_body)

        return code

    @staticmethod
    def convert_keywords(code):
        """
        This function converts keywords in a given code to Python syntax.

        :param code: a string containing the code to be processed and modified by the function
        :return: the modified code with the keywords replaced with Python syntax.
        """
        print("[ EngLang Compiler ] Converting keywords...")
        code.replace("AND", "and").replace("OR", "or").replace("IN", "in")
        code.replace("NOT", "not").replace("TRUE", "True").replace("FALSE", "False")
        return

    @staticmethod
    def convert_set_statements(code):
        """
        This function converts "SET" statements in code to variable assignments in Python.

        :param code: The code parameter is a string that represents a block of code that may contain
        "SET" statements
        :return: the modified code with the "SET" statements replaced with variable assignments.
        """
        print("[ EngLang Compiler ] Converting set statements...")
        return re.sub(r"SET (.+) TO ", r"\1 = ", code)

    @staticmethod
    def convert_if_statements(code):
        """
        This function converts IF statements in a given code string to Python syntax.

        :param code: a string containing code written in a language that uses "IF", "THEN", "ELSE", and
        "END IF" statements
        :return: the modified code with if statements converted to Python syntax.
        """
        print("[ EngLang Compiler ] Converting if statements...")
        code = re.sub(r"IF (.*) THEN", r"if \1:", code)
        code = code.replace("ELSE", "else:")
        return code.replace("END IF", "")

    @staticmethod
    def convert_while_statements(code):
        """
        This function converts WHILE statements in a given code string to Python syntax.

        :param code: a string containing code written in a language that uses "WHILE" and "END WHILE"
        statements
        :return: the modified code with while statements converted to Python syntax.
        """
        print("[ EngLang Compiler ] Converting while statements...")
        return re.sub(r"WHILE (.*)", r"while \1:", code).replace("END WHILE", "")

    @staticmethod
    def convert_for_statements(code):
        """
        This function converts FOR statements in a given code string to Python syntax.

        :param code: a string containing code written in a language that uses "FOR" and "END FOR"
        statements
        :return: the modified code with for statements converted to Python syntax.
        """
        print("[ EngLang Compiler ] Converting for statements...")
        code.replace(" DO", "")
        return re.sub(r"FOR (.*)", r"for \1:", code).replace("END FOR", "")

    @staticmethod
    def convert_comparison_statements(code):
        """
        The function replaces comparison statements in a given code with their corresponding symbols.

        :param code: a string containing the code to be modified
        :return: the modified code with the comparison statements replaced with their corresponding
        symbols.
        """
        print("[ EngLang Compiler ] Replacing comparison statements...")
        re.sub(r"IS GREATER THAN", ">", code)
        re.sub(r"IS LESS THAN", "<", code)
        re.sub(r"IS GREATER THAN OR EQUAL TO", ">=", code)
        re.sub(r"IS LESS THAN OR EQUAL TO", "<=", code)
        return re.sub(r"IS NOT EQUAL TO", "!=", code)

    @staticmethod
    def convert_arithmetic_ops(code):
        """
        This function converts the words "PLUS" and "MINUS" in a given code string to their
        corresponding arithmetic operators "+" and "-".

        :param code: a string containing code that needs to be compiled and converted
        :return: the modified code with the arithmetic operations converted from their English language
        equivalents ("PLUS" and "MINUS") to their corresponding mathematical symbols ("+" and "-").
        """
        print("[ EngLang Compiler ] Converting arithmetic operations...")
        code = re.sub(r"PLUS", "+", code)
        code = re.sub(r"MINUS", "-", code)
        code = re.sub(r"TIMES", "*", code)
        code = re.sub(r"DIVIDED BY", "/", code)
        code = re.sub(r"MODULO", "%", code)
        return re.sub(r"TO THE POWER OF", "**", code)

    @staticmethod
    def replace_display(code):
        """
        This function replaces "DISPLAY" statements in code with "print" statements.

        :param code: The code parameter is a string that represents a program written in a programming
        language. The function is designed to replace any display statements in the code with print
        statements
        :return: the modified code with the display statements replaced with print statements.
        """
        print("[ EngLang Compiler ] Replacing display statements...")
        return re.sub(r"DISPLAY ?(.+)", r"print(\1)", code)

    @staticmethod
    def replace_new_and_return(code):
        """
        The function replaces "NEW" statements with empty parentheses and "RETURN" statements with
        "return", removes "END FUNCTION" statements, and replaces "JOIN" statements with "+".

        :param code: a string containing the code to be processed and modified
        :return: the modified code with "NEW" statements replaced with function calls, "RETURN"
        statements replaced with "return" keyword, "END FUNCTION" removed, and "JOIN" replaced with "+".
        """
        print("[ EngLang Compiler ] Replacing new and return statements...")
        code = re.sub(r"NEW (.+)\(\)", r"\1()", code)
        code = code.replace("RETURN", "return").replace("END FUNCTION", "")
        return code.replace("JOIN", "+")

    @staticmethod
    def replace_new_and_return_and_end(code):
        """
        The function replaces certain statements in a given code string and returns the modified string.

        :param code: a string containing the code to be processed and modified
        :return: The modified code with "NEW" statements replaced with function calls, "RETURN"
        statements replaced with "return" keyword, "END FUNCTION" removed, "JOIN" replaced with "+",
        and "END" removed.
        """
        print("[ EngLang Compiler ] Replacing new and return and end statements...")
        code = re.sub(r"NEW (.+)\(\)", r"\1()", code)
        code = code.replace("RETURN", "return").replace("END FUNCTION", "")
        return code.replace("JOIN", "+").replace("END", "")

    @staticmethod
    def convert_variables_to_type(code):
        """
        The function converts variables in a given code to a specified data type.

        :param code: a string containing the code to be compiled
        :return: the modified code with variables converted to their specified data types.
        """
        print("[ EngLang Compiler ] Converting variables to type...")
        conversions = re.findall(r"([\w_]+?)\s+TO\s+(STRING|INT|FLOAT)", code)
        for variable, data_type in conversions:
            if data_type == "STRING":
                conversion_func = "str"
            elif data_type == "INT":
                conversion_func = "int"
            elif data_type == "FLOAT":
                conversion_func = "float"
            code = code.replace(
                f"{variable} TO {data_type}", f"{conversion_func}({variable})"
            )
        return code


def Compiler(code):
    converter = EngLangConverter()
    program_name = converter.get_program_name(code)
    python_code = converter.convert(code)

    return program_name, python_code


def main():
    """
    This function prompts the user for an EngLang file location, author name, and license name, converts
    the EngLang code to Python code using EngLangConverter, writes the Python code to a file with
    metadata, and optionally runs the generated code.
    """
    print("Welcome to MostlyWhat's EngLang Compiler!")
    file_location = input("Enter the EngLang file location (.enlg): ")
    author = input("Enter the code author's name: ")
    file_license = input("Enter the license name: ")

    with open(file_location, "r") as f:
        englang_code = f.read()

    converter = EngLangConverter()
    program_name = converter.get_program_name(englang_code)
    python_code = converter.convert(englang_code)

    output_folder = "./output/"
    output_filename = f"{program_name.lower()}.py"
    output_file = os.path.join(output_folder, output_filename)

    compiler_name = "MostlyWhat's EngLang Compiler"
    language = "EngLang"

    current_date = datetime.now().strftime("%Y-%m-%d")
    with open(output_file, "w") as f:
        f.write(
            f"# Name: {program_name.title()}\n# Author: {author}\n# Language: {language}\n# Compiled: {current_date}\n# Compiler: {compiler_name}\n# License: {file_license}\n\n"
        )
        f.write(python_code)

    print(f"\nGenerated Python file: {output_file}")

    run_code = input("\nDo you want to run the generated code? [y/n]: ")
    if run_code.lower() == "y":
        os.system(f"python {output_file}")


# `if __name__ == "__main__":` is a common Python idiom that checks whether the current script is
# being run as the main program or if it is being imported as a module into another program. If the
# script is being run as the main program, the `main()` function is called, which is the entry point
# of the program. If the script is being imported as a module, the `main()` function is not called
# automatically.
if __name__ == "__main__":
    main()
