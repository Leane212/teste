class EmailService:
    def send_email(self, recipient, subject, body):
        pass

class EventHandler:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def handle_event(self, event):
        if not isinstance(event, dict) or 'type' not in event:
            raise ValueError("Invalid event format")
        self.email_service.send_email('test@example.com', 'Event Occurred', str(event))
