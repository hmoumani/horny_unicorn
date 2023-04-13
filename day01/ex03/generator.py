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
    '''Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is
        yielded.
    '''
    if not isinstance(text, str) \
            or ((option not in ["shuffle", "unique", "ordered"])
                and option is not None):
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


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."

    print("*" * 21, "Test 1: option=None", "*" * 21)

    for word in generator(text, sep=" "):
        print(word)

    print("*" * 21, "Test 2: option=\"shuffle\"", "*" * 21)

    for word in generator(text, sep=" ", option="shuffle"):
        print(word)

    print("*" * 21, "Test 2: option=\"ordered\"", "*" * 21)

    for word in generator(text, sep=" ", option="ordered"):
        print(word)

    print("*" * 21, "Test 2: option=\"unique\"", "*" * 21)

    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)

    print("*" * 21, "Test 2: option=None, sep=\".\"", "*" * 21)

    text = 1.0
    for word in generator(text, sep="."):
        print(word)
