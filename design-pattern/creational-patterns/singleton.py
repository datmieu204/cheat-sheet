# design-pattern/creational-patterns/singleton.py

"""
- Giúp quản lý việc tạo đối tượng để đảm bảo rằng chỉ có một thể hiện (instance) của một lớp được tạo ra trong suốt vòng đời của ứng dụng.
- Tránh hard-code các thể hiện toàn cục và cung cấp một điểm truy cập toàn cục đến thể hiện đó.

- Ứng dụng:
    + Quản lý kết nối cơ sở dữ liệu: Đảm bảo rằng chỉ có một kết nối duy nhất được sử dụng trong toàn bộ ứng dụng.
    + Quản lý cấu hình ứng dụng: Cung cấp một thể hiện duy nhất để truy cập và quản lý các thiết lập cấu hình.
    + API client: Đảm bảo rằng chỉ có một thể hiện của client để quản lý các yêu cầu đến một dịch vụ bên ngoài.
"""

from threading import Lock, Thread

class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}
    _lock: Lock = Lock()

    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
    def __new__(cls):
        with cls._lock:
            if cls._instances is None:
                instance = super().__new__(cls)
                cls._instances = instance
                # Example
                # cls._instance = super(SingletonMeta, cls).__new__(cls)
                # cls._instance.api_key = "YOUR_KEY"
                # cls._instance.client = "GoogleGenAIClient_Instance"
        return cls._instances

class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str = None) -> None:
        """The Singleton class can have any initialization arguments."""
        if value:
            self.value = value
    
    def some_business_logic(self) -> None:
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        # ...

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)

if __name__ == "__main__":
    # The client code.

    thread1 = Thread(target=test_singleton, args=("FOO",))
    thread2 = Thread(target=test_singleton, args=("BAR",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # singleton1 = Singleton("FOO")
    # singleton2 = Singleton("BAR")