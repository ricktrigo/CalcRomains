import pytest
import CalcRomains


def test_input_1_caractere():
    assert CalcRomains.convertir_caractere("M") == 1000
    assert CalcRomains.convertir_caractere("X") == 10

def test_input_2_caracteres():
    assert CalcRomains.convertir_chaine("II") == 2
    assert CalcRomains.convertir_chaine("XX") == 20

def test_input_n_caracteres():
    assert CalcRomains.convertir_chaine_avec_soustraction("MCMXLIV") == 1944
