import sys

sys.path.insert(0, "/workspaces/64978874/twttr")

from twttr import shorten

def main():
    test_shorten();




def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("PYTHON") == "PYTHN"





if __name__ == "__main__":
    main()