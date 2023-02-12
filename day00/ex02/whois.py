import sys

if len(sys.argv) < 2:
    exit()
try:
    assert len(sys.argv) == 2, "more than one argument are provided"
    int(sys.argv[1])
except AssertionError as e:
    print("AssertionError:", e)
    exit()
except ValueError as e:
    print("AssertionError: argument is not an integer")
    exit()

if (int(sys.argv[1]) == 0):
    print("I'm Zero.")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")