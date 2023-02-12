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

print([elem.strip(string.punctuation) for elem in sys.argv[1].split() if len(elem.strip(string.punctuation)) > int(sys.argv[2])])
