import pytest
from python.atividades.atividade13_factorial import factorial

def test_n_menor_0():
    with pytest.raises(ValueError) as e:
        factorial(-1)
    assert str(e.value) == 'n must be a non-negative integer'

def test_n_igual_0():
    assert factorial(0) == 1

def test_fatorial():
    n = 5
    assert factorial(n) == 120