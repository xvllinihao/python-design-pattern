from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton
    """

    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def business_logic(self):
        print(self.value)

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    process_1 = Thread(target=test_singleton, args=("FOO",))
    process_2 = Thread(target=test_singleton, args=("BAR",))

    process_1.start()
    process_2.start()