> **Status - 🚧 Alpha - Work in Progress**
>
> You can use it, and feedback is more than welcome! Note that some breaking changes may still be introduced before reaching a stable version.
>
> **EngLang Website** - [https://mostlywhat.github.io/EngLang/](https://mostlywhat.github.io/EngLang/)
> For more information about EngLang, including documentation, tutorials, and examples, visit our website.
>
> **Download Alpha Builds** - [GitHub Releases](https://github.com/MostlyWhat/EngLang/releases)
>
> (We can't guarantee that these builds are stable, so use at your own risk.)

# EngLang: An English-Based Programming Language

<a href="https://github.com/MostlyWhat/EngLang">
  <img src="assets/logo.png" alt="Logo" width="200" height="200"></img>
</a>

**EngLang** is an experimental programming language that uses English words and phrases to make programming more accessible to beginners and non-technical users. Rather than relying on complex syntax and arcane commands, EngLang allows users to express their ideas in natural language.

## Principles

The goal of EngLang is to make programming more accessible by removing some of the barriers to entry that exist in traditional programming languages. By using English words and phrases, EngLang eliminates the need to learn a new syntax and grammar. This makes it easier for beginners to understand and use the language.

EngLang is designed to be easy to learn and use, but it is still a powerful programming language. It supports all of the features and functions that you would expect from a modern programming language, including variables, control structures, and functions.

## Technical Details

Under the hood, EngLang is actually a compiler that translates English code into Python. This allows it to take advantage of the power and flexibility of Python while still providing a more accessible interface.

When you write code in EngLang, the compiler first parses your code and translates it into an abstract syntax tree (AST). It then uses this AST to generate equivalent Python code, which can be executed just like any other Python code.

## Getting Started

To get started with EngLang, you can download the latest version of the compiler from our GitHub repository. Once you have installed the compiler, you can start writing code in EngLang just like you would in any other programming language.

Here is an example of a simple EngLang program that calculates the sum of two numbers:

```EngLang
PROGRAM EXAMPLE

    SET x TO 5
    SET y TO 3

    DISPLAY "The sum of " JOIN x JOIN " and " JOIN y JOIN " is " JOIN (x + y)

END PROGRAM
```

When you run this program through the EngLang compiler, it will generate the following Python code:

```python
x = 5
y = 3
print("The sum of " + str(x) + " and " + str(y) + " is " + str(x + y))
```

As you can see, the EngLang code has been translated into equivalent Python code that performs the same task.

## Roadmap

### Work in Progress (Alpha Version)

Our program is currently in its alpha stage, which means that it's still in the early stages of development. We're actively working on improving the functionality and adding new features, but there may be bugs and limitations that we're still working on. We welcome any feedback and bug reports from our users to help us improve the program.

See [ROADMAP.md](ROADMAP.md) for more information about the current status of the project.

## Disclaimer

EngLang is still in development and is not yet ready for use. We are working hard to create a stable and reliable product, but please be aware that there may be bugs and other issues in the current version. Use at your own risk.

## Contributing

If you are interested in contributing to EngLang, we would love to hear from you! You can contribute by submitting bug reports, feature requests, or pull requests to our GitHub repository.

## License

EngLang is licensed under the Apache 2.0 License. See the LICENSE file for more details.
