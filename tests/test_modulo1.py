import pytest
from progetto.modulo1 import funzione_doppio, funzione_quadrato, ClasseParzialmenteImplementata

def test_funzione_doppio():
    assert funzione_doppio(5) == 10
    assert funzione_doppio(10) == 20

def test_funzione_quadrato():
    assert funzione_quadrato(5) == 25
    assert funzione_quadrato(4) == 16

def test_metodo_esistente_classe():
    istanza = ClasseParzialmenteImplementata("John")
    assert istanza.metodo_esistente() == "Ciao, sono John!"

def test_metodo_da_completare_classe():
    istanza = ClasseParzialmenteImplementata("John")
    assert istanza.metodo_da_completare(" è buono all'esame") == "John è buono all'esame"