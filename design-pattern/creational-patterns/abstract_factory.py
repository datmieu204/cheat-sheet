# design-pattern/creational-patterns/abstract_factory.py

"""
- Cung cấp một giao diện để tạo các họ đối tượng liên quan hoặc phụ thuộc mà không cần chỉ định các lớp cụ thể của chúng. Điều này giúp tách biệt việc tạo đối tượng khỏi việc sử dụng đối tượng, làm tăng tính linh hoạt và khả năng mở rộng của mã.
- Cho phép thay đổi họ đối tượng được sử dụng trong một ứng dụng mà không cần thay đổi mã sử dụng các đối tượng đó, giúp dễ dàng chuyển đổi giữa các họ đối tượng khác nhau.
- Ứng dụng:
    + Giao diện người dùng đa nền tảng: Khi phát triển ứng dụng cho nhiều nền tảng (như Windows, macOS, Linux), mẫu Abstract Factory có thể được sử dụng để tạo các thành phần giao diện người dùng phù hợp với từng nền tảng mà không cần thay đổi mã chính của ứng dụng.
    + Hệ thống plugin: Trong các hệ thống hỗ trợ plugin, mẫu Abstract Factory có thể được sử dụng để tạo các đối tượng plugin khác nhau dựa trên loại plugin được chọn, giúp dễ dàng mở rộng hệ thống bằng cách thêm các plugin mới.
    + Quản lý cấu hình: Khi một ứng dụng cần hỗ trợ nhiều cấu hình khác nhau (như chế độ phát triển, chế độ sản xuất), mẫu Abstract Factory có thể được sử dụng để tạo các đối tượng cấu hình phù hợp với từng môi trường mà không cần thay đổi mã chính của ứng dụng.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    """
    Abstract Factory Interface
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

"""
Concrete Factories
"""

class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factory 1
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
    
class ConcreteFactory2(AbstractFactory):
    """
    Concrete Factory 2
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
    
"""
Interfaces for Products
"""

class AbstractProductA(ABC):
    """
    Abstract Product A Interface
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass

"""
Concrete Products A
"""

class ConcreteProductA1(AbstractProductA):
    """
    Concrete Product A1
    """

    def useful_function_a(self) -> str:
        return "The result of the product A1."
    
class ConcreteProductA2(AbstractProductA):
    """
    Concrete Product A2
    """

    def useful_function_a(self) -> str:
        return "The result of the product A2."
    
class AbstractProductB(ABC):
    """
    Abstract Product B Interface
    """

    @abstractmethod
    def useful_function_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        pass

class ConcreteProductB1(AbstractProductB):
    """
    Concrete Product B1
    """

    def useful_function_b(self) -> str:
        return "The result of the product B1."
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"
    
class ConcreteProductB2(AbstractProductB):
    """
    Concrete Product B2
    """

    def useful_function_b(self) -> str:
        return "The result of the product B2."
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
    
def client_code(factory: AbstractFactory) -> None:
    """
    Client code works with factories and products only through abstract types.
    This lets you pass any factory or product subclass to the client code without breaking it.
    """

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}")

if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\nClient: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())