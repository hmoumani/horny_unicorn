import string 
def text_analyzer(*argv):
    "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
    if len(argv) > 1:
        return print("ERROR")
    if (len(argv) == 0):
        text = input("What is the text to analyse?")
    else:
        text = argv[0]
    print("The text contains {} characters:".format(len(text)))
    print("- {} upper letters".format(len([c for c in text if c.isupper()])))
    print("- {} lower letters".format(len([c for c in text if c.islower()])))
    print("- {} punctuation marks".format(len([c for c in text if c in string.punctuation])))
    print("- {} spaces".format(len([c for c in text if c == ' '])))

text_analyzer("""Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.""")

text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")

text_analyzer("python", "2.0")

print(text_analyzer.__doc__)


text_analyzer()