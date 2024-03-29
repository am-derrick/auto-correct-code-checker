def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Generate test cases for the factorial function
test_cases_factorial = [
    (0, "1\n"),   # Factorial of 0 is 1
    (1, "1\n"),   # Factorial of 1 is 1
    (5, "120\n"), # Factorial of 5 is 120
    (10, "3628800\n"), # Factorial of 10 is 3628800
]

# Write test cases to a file
with open("test_cases_factorial.txt", "w") as file:
    for input_data, expected_output in test_cases_factorial:
        file.write(f"{input_data}\t{expected_output}")
