import pytest
from python.atividades.atividade11_custom_sort import custom_sort

def test_ordem_decre():
    numbers = [1,2.3,4,3]
    assert custom_sort(numbers) == [4, 3, 2.3, 1]