import pytest
from python.atividades.atividade06_point import Point

def test_distance_point():
    point1 = Point(10,20)
    distance = point1.distance_to(point1)
    assert distance == 0

def test_deve_retornar_erro():
    point1 = Point(10,None)
    with pytest.raises(ValueError) as e:
        point1.distance_to(None)
    assert str(e.value) == 'Argument must be a Point'


