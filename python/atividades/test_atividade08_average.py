import pytest
from python.atividades.atividade08_average import calculate_average

def test_media_da_lista():
    numbers = [1,1.5,4,3]
    assert calculate_average(numbers) == 2.375

def test_deve_retornar_erro():
    numbers = []
    with pytest.raises(ValueError) as e:
        calculate_average(numbers)
    assert str(e.value) == 'The list of numbers cannot be empty'