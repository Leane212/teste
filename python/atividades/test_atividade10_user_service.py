import pytest
from unittest.mock import Mock
from python.atividades.atividade10_user_service import User, UserService, UserManager  

def test_fetch_user_info_valida():
    mock_user_service = Mock(spec=UserService)
    user_manager = UserManager(mock_user_service)
    
    user_id = 1
    user = User(user_id=user_id, name="Leane")
    mock_user_service.get_user_info.return_value = user
    
    result = user_manager.fetch_user_info(user_id)
    assert result == user
    mock_user_service.get_user_info.assert_called_once_with(user_id)

def test_fetch_user_info_invalido():
    mock_user_service = Mock(spec=UserService)
    user_manager = UserManager(mock_user_service)
    
    user_id = 2
    mock_user_service.get_user_info.return_value = None
    
    with pytest.raises(ValueError) as e:
        user_manager.fetch_user_info(user_id)
    assert str(e.value) == 'User not found'