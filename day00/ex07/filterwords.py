import sys
import string 

if (len(sys.argv) != 3)or sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("ERROR")
    exit()


print([elem.strip(string.punctuation) for elem in sys.argv[1].split() if len(elem.strip(string.punctuation)) > int(sys.argv[2])])