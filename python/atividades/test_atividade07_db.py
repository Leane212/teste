from unittest.mock import Mock
import pytest 
from python.atividades.test_atividade07_db import User, DataBase, UserService

def test_usuario_save_sucess():
    mock_db = Mock()
    
