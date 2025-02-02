# 1/3 --> 1
#1. Write a Python program to handle file not found and divide-by-zero exceptions.
def handle_exceptions():
    try:
        my_file = 'non_existent_file.txt'  
        with open(my_file, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
    try:
        numerator = 10
        denominator = 0  
        result = numerator / denominator
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. The denominator cannot be zero.")
handle_exceptions()
