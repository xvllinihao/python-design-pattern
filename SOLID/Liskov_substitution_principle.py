# child class must be subsitutable for its parent class

from abc import ABC, abstractmethod
from dataclasses import dataclass
from creational_patterns.singleton import SingletonMeta


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send {message} to {self.email}")


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"send {message} to {self.phone}")


@dataclass()
class Contact:
    name: str
    email: str
    phone: str


class NotificationManager(metaclass=SingletonMeta):

    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '408-888-9999')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send("Hello john")

    notification_manager.notification = email_notification
    notification_manager.send("Hi John")

