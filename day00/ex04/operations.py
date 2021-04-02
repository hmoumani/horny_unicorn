import sys

if len(sys.argv) > 3:
    print("""InputError: too many arguments

Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")
    exit()
if len(sys.argv) < 3:
    print("""Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")
    exit()
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("""InputError: only numbers

Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")
    exit()



num1, num2 = int(sys.argv[1]), int(sys.argv[2])

print("Sum:\t\t{}".format(num1 + num2))
print("Difference:\t{}".format(num1 - num2))
print("Product:\t{}".format(num1 * num2))
print("Quotient:\t{}".format(num1 / num2 if num2 != 0 else "ERROR (div by zero)"))
print("Remainder:\t{}".format(num1 % num2 if num2 != 0 else "ERROR (modulo by zero)"))