import string_manipulate
import pytest

"""

def test_remove_e():
    assert string_manipulate.remove_e("hello") == "hllo"
    assert string_manipulate.remove_e("world") == "world"
    assert string_manipulate.remove_e("") == ""
    assert string_manipulate.remove_e("Helle er her") == "Hll r hr"

"""
"""
Demo of test throwing an Error
"""



def test_string_type():
    x = 123
    with pytest.raises(AttributeError):
        if not isinstance(x, str):
            raise AttributeError("The variable is not a string.")


@pytest.mark.parametrize("str, expected", [
    ("hello", "hllo"), 
    ("world", "world"), 
    ("", ""),
    ("Helle er her","Hll r hr")
    ])
def test_remove_e_parameterized(str, expected):
    assert string_manipulate.remove_e(str) == expected





