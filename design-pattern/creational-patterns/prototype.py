# design-pattern/creational-patterns/prototype.py

"""
- Cho phép sao chép các đối tượng hiện có mà không làm cho mã phụ thuộc vào các lớp cụ thể của chúng. Điều này hữu ích khi việc tạo một đối tượng mới tốn kém về mặt tài nguyên hoặc phức tạp.
- Cung cấp một cách để tạo các bản sao của các đối tượng hiện có thông qua một giao diện chung, giúp giảm sự phụ thuộc vào các lớp cụ thể và tăng tính linh hoạt trong việc tạo đối tượng.
- Ứng dụng:
    + Tạo các bản sao của các đối tượng phức tạp: Khi việc tạo một đối tượng mới đòi hỏi nhiều bước cấu hình hoặc tốn kém về tài nguyên, việc sao chép một đối tượng hiện có có thể nhanh hơn và hiệu quả hơn.
    + Quản lý trạng thái đối tượng: Khi cần tạo nhiều phiên bản của một đối tượng với các trạng thái khác nhau, mẫu Prototype cho phép sao chép đối tượng gốc và sau đó điều chỉnh trạng thái của bản sao.
    + Hệ thống đồ họa và trò chơi: Trong các ứng dụng đồ họa hoặc trò chơi, việc sao chép các đối tượng như nhân vật, vật phẩm hoặc cảnh có thể giúp tiết kiệm thời gian và tài nguyên.
"""

import copy

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def self_parent(self, parent):
        self.parent = parent

class SomeComponent:
    """
    Docstring for SomeComponent
    """
    def __init__(self, some_init, some_list_of_objects, some_circular_ref=None):
        self.some_init = some_init
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Tạo một bản sao nông của đối tượng hiện tại.
        """

        # Sao chép các thuộc tính phức tạp
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Tạo một thể hiện mới của lớp hiện tại với các thuộc tính đã sao chép
        new = self.__class__(
            self.some_init,
            some_list_of_objects,
            some_circular_ref,
        )
        new.__dict__.update(self.__dict__)

        return new
    
    def __deepcopy__(self, memo=None):
        """
        Tạo một bản sao sâu của đối tượng hiện tại.
        """

        if memo is None:
            memo = {}

        # Sao chép các thuộc tính phức tạp một cách đệ quy
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Tạo một thể hiện mới của lớp hiện tại với các thuộc tính đã sao chép
        new = self.__class__(
            self.some_init,
            some_list_of_objects,
            some_circular_ref,
        )
        new.__dict__.update(copy.deepcopy(self.__dict__, memo))

        return new
    
if __name__ == "__main__":
    # Tạo một đối tượng gốc
    original = SomeComponent(
        some_init="Some value",
        some_list_of_objects=[1, 2, 3],
        some_circular_ref=SelfReferencingEntity(),
    )

    original.some_circular_ref.self_parent(original)
    # Tạo một bản sao nông của đối tượng gốc
    shallow_copied = copy.copy(original)
    # Tạo một bản sao sâu của đối tượng gốc
    deep_copied = copy.deepcopy(original)
    # Kiểm tra các bản sao
    print("Original:", original)
    print("Shallow Copied:", shallow_copied)
    print("Deep Copied:", deep_copied)
    print("Original's some_list_of_objects id:", id(original.some_list_of_objects))
    print("Shallow Copied's some_list_of_objects id:", id(shallow_copied.some_list_of_objects))
    print("Deep Copied's some_list_of_objects id:", id(deep_copied.some_list_of_objects))
    print("Original's some_circular_ref id:", id(original.some_circular_ref))
    print("Shallow Copied's some_circular_ref id:", id(shallow_copied.some_circular_ref))
    print("Deep Copied's some_circular_ref id:", id(deep_copied.some_circular_ref))
    print("Original's some_circular_ref.parent id:", id(original.some_circular_ref.parent))
    print("Shallow Copied's some_circular_ref.parent id:", id(shallow_copied.some_circular_ref.parent))
    print("Deep Copied's some_circular_ref.parent id:", id(deep_copied.some_circular_ref.parent))