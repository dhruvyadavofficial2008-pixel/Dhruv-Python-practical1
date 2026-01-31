# ===============================================
# Exception Handling Learning Program
# Name: Dhruv Yadav
# Roll No: F126
# ===============================================

import logging
logging.basicConfig(filename="error.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

print("=== Exception Handling Demo by Dhruv Yadav (F126) ===\n")

# 1. Basic ZeroDivisionError handling
print("1. Basic ZeroDivisionError:")
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print()

# 2. Multiple exceptions: ZeroDivisionError and ValueError
print("2. Multiple exceptions:")
try:
    value = int(input("Enter a number: "))
    result = 50 / value
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")

print()

# 3. Generic Exception for FileNotFoundError
print("3. File handling exception:")
try:
    file = open("non_existent_file.txt", "r")
except Exception as e:
    print(f"An error occurred: {e}")

print()

# 4. try-except-else-finally
print("4. try-except-else-finally:")
try:
    num = int(input("Enter a number: "))
    result = 120 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

print()

# 5. Custom Exception class and handling
print("5. Custom NegativeNumberError:")
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return num

try:
    number = int(input("Enter a positive number: "))
    check_positive(number)
    print("Valid number entered!")
except NegativeNumberError as e:
    print(f"Error: {e}")

print()

# 6. Logging exceptions
print("6. Logging ZeroDivisionError:")
try:
    x = 70 / 0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError occurred: %s", e)
    print("An error occurred. Check error.log for details.")

print("\n=== End of Demo ===")
