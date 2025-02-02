# 10/15 --> 1,3,4,6,7,8,9,10,11,13
# 1. Write a program to print "Hello, World!" and experiment with string formatting
print("Q1: Print 'Hello, World!' and experiment with string formatting")
print("Hello, World!")
name = "World"
print(f"Hello, {name}!")

# 3. Write a Python program to swap two variables without using a third variable
print("\nQ3: Swap two variables without using a third variable")
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")

# 4. Write a program to check whether a given number is positive, negative, or zero
print("\nQ4: Check whether a given number is positive, negative, or zero")
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 6. Write a program to display the Fibonacci sequence up to a certain number
print("\nQ6: Display the Fibonacci sequence up to a certain number")
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
limit = int(input("Enter the limit for Fibonacci sequence: "))
fibonacci(limit)

# 7. Develop a program to check whether a number is prime
print("\nQ7: Check whether a number is prime")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# 8. Create a Python function to reverse a given string
print("\nQ8: Reverse a given string")
def reverse_string(s):
    return s[::-1]
string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")

# 9. Write a function to count the occurrences of a specific character in a string
print("\nQ9: Count the occurrences of a specific character in a string")
def count_char(s, char):
    return s.count(char)
string = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")
print(f"The character '{char_to_count}' appears {count_char(string, char_to_count)} times.")

# 10. Write a Python program to find the greatest of three numbers
print("\nQ10: Find the greatest of three numbers")
def greatest_of_three(a, b, c):
    return max(a, b, c)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(f"The greatest number is: {greatest_of_three(num1, num2, num3)}")

# 11. Build a program to calculate the sum of digits of a given number
print("\nQ11: Calculate the sum of digits of a given number")
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  
        n = n // 10 
    return total
number = int(input("Enter a number: "))
print(f"The sum of digits is: {sum_of_digits(number)}")

# 13. Write a Python function to check if a string is a palindrome
print("\nQ13: Check if a string is a palindrome")
def is_palindrome(s):
    return s == s[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

