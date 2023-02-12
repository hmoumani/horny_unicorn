import sys

def decimal_places(f):
    str_f = str(f)
    decimal_index = str_f.find(".")
    if decimal_index == -1:
        return 0
    return len(str_f[decimal_index + 1:])

def truncate_float(f):
    return ('{}' if decimal_places(f) <= 4 else '{:.4f}...').format(f)

if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    exit()
if len(sys.argv) < 3:
    print("""Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")
    exit()
try:
    num1, num2 = int(sys.argv[1]), int(sys.argv[2])
except ValueError:
    print("AssertionError: only integers")
    exit()



print("Sum:\t\t{}".format(num1 + num2))
print("Difference:\t{}".format(num1 - num2))
print("Product:\t{}".format(num1 * num2))
print("Quotient:\t{}".format(truncate_float(num1 / num2) if num2 != 0 else "ERROR (div by zero)"))
print("Remainder:\t{}".format(num1 % num2 if num2 != 0 else "ERROR (modulo by zero)"))