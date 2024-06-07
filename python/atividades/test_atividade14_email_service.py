import pytest
from unittest.mock import Mock
from python.atividades.atividade14_email_service import EmailService, EventHandler 

def test_handle_event_sends_email():
    mock_email_service = Mock(spec=EmailService)
    event_handler = EventHandler(mock_email_service)
    
    event = {'type': 'user_signup', 'user_id': 123}

    event_handler.handle_event(event)
    mock_email_service.send_email.assert_called_once_with('test@example.com', 'Event Occurred', str(event))

