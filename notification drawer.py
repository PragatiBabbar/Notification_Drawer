from pynotifier import Notification


def me():
    Notification(
        title='Hey!!!',
        description='This is a notification made by Pragati using Python.',
        duration=5,  # Duration in seconds
        urgency=Notification.URGENCY_CRITICAL
    ).send()


me()
