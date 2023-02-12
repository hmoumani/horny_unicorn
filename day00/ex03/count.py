import string 
import sys

def text_analyzer(text=None):
    "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
    if not text:
        text = input("What is the text to analyse?\n")
    if not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return
    print("The text contains {} characters:".format(len(text)))
    print("- {} upper letters".format(len([c for c in text if c.isupper()])))
    print("- {} lower letters".format(len([c for c in text if c.islower()])))
    print("- {} punctuation marks".format(len([c for c in text if c in string.punctuation])))
    print("- {} spaces".format(len([c for c in text if c == ' '])))

# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")

# text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")

# text_analyzer(42)

# print(text_analyzer.__doc__)

if __name__ == "__main__":
    text_analyzer(sys.argv[1] if len(sys.argv) > 1 else None)