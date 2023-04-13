import sys
import string 

if len(sys.argv) != 3:
    print("ERROR")
    exit()
try:
    if int(sys.argv[2]) < 0:
        raise ValueError("ERROR")
except Exception:
    print("ERROR")
    exit()

sys.argv[1] = ''.join([c for c in sys.argv[1] if c not in string.punctuation])

print([elem for elem in sys.argv[1].split() if len(elem) > int(sys.argv[2])])
