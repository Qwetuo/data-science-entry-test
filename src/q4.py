def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    result = s[::-1]
    print(result) 
    return result


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
string_reverse("Hello World")
string_reverse("Python")