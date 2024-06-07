from unittest.mock import Mock
import pytest 
from python.atividades.atividade07_db import Database, User, UserService


def test_usuario_save_success():
    mock_db = Mock(spec=Database)
    user_service = UserService(mock_db)    #instanciar
    user = User(name="Leane", email="leane@gmail.com")
    user_service.save_user(user)
    
    mock_db.save_user.assert_called_once_with(user)

def test_usuario_save_without_name():
    mock_db = Mock(spec=Database)
    user_service = UserService(mock_db)
    user = User(name="", email="leane@gmail.com")

    with pytest.raises(ValueError) as e:
        user_service.save_user(user)
    assert str(e.value) == 'User must have a name and email'

def test_usuario_save_without_email():
    mock_db = Mock(spec=Database)
    user_service = UserService(mock_db)
    user = User(name="Leane", email="")

    with pytest.raises(ValueError) as e:
        user_service.save_user(user)
    assert str(e.value) == 'User must have a name and email'