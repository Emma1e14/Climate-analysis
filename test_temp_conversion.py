from temp_conversion import fahr_to_celsius
from temp_conversion import fahr_to_kelvin

def test_fahr_to_celius():
    assert fahr_to_celsius(32) == 0

def test_fahr_to_kelvin():
    assert fahr_to_kelvin(32) == 273.15
