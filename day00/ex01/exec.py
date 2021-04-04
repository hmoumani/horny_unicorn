import sys
if len(sys.argv) < 2 :
    exit()

final_list = []
for elem in [elem.split() for elem in sys.argv]:
    final_list.extend(elem)

final_list = final_list[1::][::-1]

for i in range(len(final_list)):
    elem = final_list[i][::-1]
    for c in elem:
        print(c.upper() if c.islower() else c.lower(), end="")
    print(" " if i != len(final_list) - 1 else "", end="")
print()