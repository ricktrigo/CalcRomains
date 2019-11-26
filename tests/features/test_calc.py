import pytest
import CalcRomains


def test_input_():
    assert CalcRomains.convertir_caractere("M") == 1000
    assert CalcRomains.convertir_caractere("X") == 10
