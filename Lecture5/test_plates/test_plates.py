import sys

sys.path.insert(0, "/workspaces/64978874/plates")

from plates import is_valid

def main():
    test_isValid()

def test_isValid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("50CS") == False
    assert is_valid("50") == False


if __name__ == "__main__":
    main()