import pytest
import CalcRomains


def test_input_1_caractere():
    assert CalcRomains.convertir_caractere("M") == 1000
    assert CalcRomains.convertir_caractere("X") == 10

def test_input_2_caracteres_identiques():
    assert CalcRomains.convertir_chaine("II") == 2
    assert CalcRomains.convertir_chaine("XX") == 20

def test_input_n_caracteres():
    assert CalcRomains.convertir_chaine("MMCLXI") == 2161
    assert CalcRomains.convertir_chaine("MMDCLXXVI") == 2676

def test_input_n_caracteres_identiques():
    assert CalcRomains.convertir_chaine("MMMMMM") == 6000
    assert CalcRomains.convertir_chaine("XXXXXXXXXX") == 100

def test_input_2_caracteres_avec_soustraction():
    assert CalcRomains.convertir_chaine_avec_soustraction("IV") == 4
    assert CalcRomains.convertir_chaine_avec_soustraction("CM") == 900

