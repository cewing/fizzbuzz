Feature: Simple FizzBuzz
    Implement a simple version of the FizzBuzz game

    Scenario Outline: FizzBuzz [just enough]
        Given the number <input>
        When I call FizzBuzz
        Then I see the output <output>

    Examples:
    | input | output   |
    | 0     | 0        |
    | 1     | 1        |
    | 3     | Fizz     |
    | 5     | Buzz     |
    | 6     | Fizz     |
    | 10    | Buzz     |
    | 15    | FizzBuzz |
