def generate_pascals_triangle(n):
    """this function generates a Pascals triangle
    upto n rows"""
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


# Generate test cases for 5 and 7 rows
test_cases = []
for row in generate_pascals_triangle(5):
    test_cases.append((",".join(map(str, row)), "\n"))

"""
for row in generate_pascals_triangle(7):
    test_cases.append((",".join(map(str, row)), "\n"))
"""

# write the test cases to a file
with open("test_cases.txt", "w") as file:
    for input_data, expected_output in test_cases:
        file.write(f"{input_data}\t{expected_output}")
