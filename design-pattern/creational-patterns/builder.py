# design-pattern/creational-patterns/builder.py

"""
- Tách biệt việc xây dựng một đối tượng phức tạp khỏi biểu diễn cuối cùng của nó, cho phép cùng một quy trình xây dựng tạo ra các biểu diễn khác nhau. Điều này giúp kiểm soát quá trình xây dựng và làm cho mã dễ bảo trì hơn.
- Cung cấp một cách tiếp cận có cấu trúc để tạo các đối tượng phức tạp bằng cách chia nhỏ quá trình xây dựng thành các bước riêng biệt, giúp tăng tính linh hoạt và khả năng mở rộng của mã.
- Ứng dụng:
    + Xây dựng tài liệu phức tạp: Khi tạo các tài liệu như báo cáo, hợp đồng hoặc trang web, mẫu Builder có thể được sử dụng để xây dựng các tài liệu này theo từng phần, cho phép dễ dàng tùy chỉnh và mở rộng.
    + Tạo đối tượng đồ họa: Trong các ứng dụng đồ họa hoặc trò chơi, mẫu Builder có thể được sử dụng để xây dựng các đối tượng đồ họa phức tạp như nhân vật, cảnh hoặc hiệu ứng đặc biệt theo từng bước.
    + Cấu hình hệ thống: Khi thiết lập các hệ thống phức tạp với nhiều thành phần và tùy chọn cấu hình, mẫu Builder có thể giúp tổ chức quá trình cấu hình này một cách rõ ràng và có cấu trúc.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """
    Builder Interface
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class ConcreteBuilder(Builder):
    """
    Concrete Builder
    """

    def __init__(self) -> None:
        """
        A fresh builder instance.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")

class Product1:
    """
    Product Class
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")

class Director:
    """
    Director Class
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

def client_code(director: Director) -> None:
    builder = ConcreteBuilder()
    director.builder = builder

    print("Standard basic product:")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product:")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product:")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()

if __name__ == "__main__":
    director = Director()
    client_code(director)