def factorial_recursive(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
