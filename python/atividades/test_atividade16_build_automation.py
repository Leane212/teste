from unittest.mock import patch, MagicMock
from python.atividades.atividade16_build_automation import automation_build, InstallationEnum, StatusEnum

def setup_mock_session(mock_db_context, automation_id, automation_name, robots=None):
    mock_session = MagicMock()
    mock_db_context.return_value.__enter__.return_value = mock_session
    
    mock_automation = MagicMock()
    mock_automation.id = automation_id
    mock_automation.name = automation_name
    mock_session.query.return_value.filter_by.return_value.first.return_value = mock_automation
    
    if robots is None:
        robots = []
    mock_session.query.return_value.filter_by.return_value.all.return_value = robots
    
    return mock_session

def test_automation_build_no_robots():
    with patch('python.atividades.atividade16_build_automation.db_context') as mock_db_context:
        setup_mock_session(mock_db_context, automation_id=1, automation_name='Automação teste')
        
        result = automation_build(1)
        
        assert result == 'Automation Automação teste has no robots to execute.'

def test_automation_build_all_robots_installed():
    with patch('python.atividades.atividade16_build_automation.db_context') as mock_db_context, \
        patch('python.atividades.atividade16_build_automation.orchestration_create') as mock_orchestration_create:
        
        mock_session = setup_mock_session(mock_db_context, automation_id=1, automation_name='Automação teste', robots=[MagicMock(installed=InstallationEnum.INSTALLED.value)])
        
        result = automation_build(1)
        
        assert mock_session.query.return_value.filter_by.return_value.first.return_value.status == StatusEnum.RUNNING.value
        mock_session.commit.assert_called_once()
        mock_orchestration_create.assert_called_once_with(1)
        assert result == 'Automation Automação teste builded successfully'

def test_automation_build_robots_not_installed():
    with patch('python.atividades.atividade16_build_automation.db_context') as mock_db_context, \
         patch('python.atividades.atividade16_build_automation.send_to_pack') as mock_send_to_pack, \
         patch('python.atividades.atividade16_build_automation.orchestration_create') as mock_orchestration_create, \
         patch('python.atividades.atividade16_build_automation.automation_build') as mock_automation_build:
        
        mock_session = setup_mock_session(mock_db_context, automation_id=1, automation_name='Automação teste', robots=[MagicMock(installed=InstallationEnum.NOT_INSTALLED.value)])
        
        result = automation_build(1)
        
        assert mock_session.query.return_value.filter_by.return_value.first.return_value.status == StatusEnum.RUNNING.value
        mock_session.commit.assert_called_once()
        mock_send_to_pack.assert_called_once_with(mock_session.query.return_value.filter_by.return_value.all.return_value[0].id)
        mock_orchestration_create.assert_not_called()
        mock_automation_build.assert_called_once_with(automation_id=1)
        assert result == 'there is robots to install, building automation 1 again'
