from numb3rs import validate

def main():
    test_validate()


def test_validate():

    assert validate("255.255.255.255") == True

    assert validate("1000.255.255.255") == False
    assert validate("255.1000.255.255") == False
    assert validate("255.212.512.112") == False
    assert validate("cat") == False
    assert validate("254.157.200.452") == False



if __name__ == "__main__":
    main()