from .notification_channel import NotificationChannel


class EmailNotificationChannel(NotificationChannel):
    def send(self):
        return super().send()