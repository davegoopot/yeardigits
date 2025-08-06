# GitHub Copilot Instructions for Year Digits

## Project Overview
A brief description of the project

## Development Guidelines

1. *Use test-driven development (TDD)*
  - Write a failing test before writing the code to implement a feature. Only write one test at a time before checking that it fails
  - Run the test
  - Write the minimum code necessary to pass the test.
  - Run the tests again to ensure all tests pass.
  - Refactor the code if necessary, ensuring that all tests still pass.
3. Try not to write comments. Instead prefer to write self-documenting code that is clear and easy to understand. If a function is called `test_get_nginx_version_uses_custom_certificate` do not write a comment that says `# Test that get_nginx_version uses custom certificate`. Instead, the function name itself should be clear enough to understand what it does.
  - If you must write a comment, use it to explain why something is done, not what is done.
  - Prefer longer names for functions and variables to code comments.
4. Write short methods.
5. Allow only a few methods per class.
6. Do one thing. Each class, function, or method should be responsible for only one thing.
7. Use the rule-of-three for avoiding code duplication (DRY): Code duplicated once is acceptable; code duplicated more than once should be abstracted into one place to be re-used.
8. Methods should be at a uniform level of abstraction:
  - Functions should be either a list of high-level instructions describing a process or the implementation of one step of the process. Do not do both in the same function.
  - Always use Command-query separation (CQS) pattern. A function could be either be a command that performs an action, or a query that returns data to the caller, but not both. In other words, asking a question should not change the answer.


## AI Assistant Guidelines
When helping with this project:
1. Do the absolute minimum to complete the request. Do not spend time speculatively implementing features that have not been explicitly asked for
2. In particular *if asked to write a failing test DO NOT IMPLEMENT THE CODE TO PASS THE TEST at the same time*.
3. Suggest appropriate error handling
4. Follow established patterns in the codebase
5. Consider security best practices
6. Ask for clarification when requirements are unclear
