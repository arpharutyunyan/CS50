import sys
import pytest
sys.path.insert(0, "/workspaces/64978874/fuel")

from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

    with pytest.raises(ValueError):
        convert("cat/dog")


def test_gauge():
    assert gauge(100) =="F"
    assert gauge(99) =="F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"




if __name__ == "__main__":
    main()