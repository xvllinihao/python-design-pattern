from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Observer:

    @abstractmethod
    def update(self, subject: Subject) -> None:

        pass


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:

        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:

        pass

    @abstractmethod
    def notify(self) -> None:

        pass

class ConcreteSubject(Subject):

    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        print("Subject: Detached an observer")
        self._observers.remove(observer)

    def notify(self) -> None:

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_bussiness_logic(self) -> None:

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0,10)

        print(f"Subject: My state has changed to: {self._state}")
        self.notify()

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserveB: Reacted to the event")


if __name__ == '__main__':
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_bussiness_logic()
    subject.some_bussiness_logic()

    subject.detach(observer_a)

    subject.some_bussiness_logic()