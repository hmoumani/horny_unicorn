from random import randint

def shuffle_lst(spl):
    already = []
    len_spl = len(spl)
    ret = []
    while len(ret) < len_spl:
        x = randint(0, len_spl - 1)
        if x in already:
            continue
        ret.append(spl[x])
        already.append(x)
    return ret

def generator(text, sep=" ", option=None):
    if type(text) != str or ((option not in ["shuffle", "unique", "ordered"]) and option != None):
        yield "Error"
        return None
    spl = text.split(sep)
    if option == "unique":
        spl = list(dict.fromkeys(spl))
    elif option == "shuffle":
        spl = shuffle_lst(spl)
    elif option == "ordered":
        spl.sort()
    for elem in spl:
        yield elem


text = "Le Lorem Ipsum est simplement du faux texte."

for word in generator(text, sep=" "):
    print(word)

print("*" * 42)

for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print("*" * 42)

for word in generator(text, sep=" ", option="ordered"):
    print(word)

print("*" * 42)

text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)

print("*" * 42)


text = 1.0
for word in generator(text, sep="."):
    print(word)