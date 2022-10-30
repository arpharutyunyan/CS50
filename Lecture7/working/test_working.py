from working import convert
import pytest

def main():
    test_convert()


def test_convert():

    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM - 08:70 PM")




if __name__ == "__main__":
    main()