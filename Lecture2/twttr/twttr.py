"""
    When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
    In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels 
    (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
    
"""

def main():

    phrase = input("Input: ")
    phrase = shorten(phrase)
    print(f"Output: {phrase}")


def shorten(word):
    letter = ("a", "e", "i", "o", "u")
    # letter = ("a", "e", "i", "O", "u")
    for i in word :
        if i.lower() in letter:
            word = word.replace(i, "")
    return word

if __name__ == "__main__":
    main()