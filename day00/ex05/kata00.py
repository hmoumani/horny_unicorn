kata = (19,42,21)

if len(kata) == 0:
    print("The kata is empty")
else:
    print("The {} number are: {}".format(len(kata), ", ".join(str(i) for i in kata)))