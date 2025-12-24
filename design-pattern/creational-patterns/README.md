# Creational Patterns - Các Mẫu Thiết Kế Khởi Tạo

## Tổng Quan

Các mẫu thiết kế khởi tạo (Creational Patterns) liên quan đến cơ chế tạo đối tượng, cố gắng tạo đối tượng theo cách phù hợp với tình huống. Thay vì khởi tạo đối tượng trực tiếp bằng constructor, các mẫu này cung cấp cơ chế tạo đối tượng linh hoạt và có thể tái sử dụng, giúp tăng tính linh hoạt và khả năng mở rộng của mã nguồn.

## Các Mẫu Thiết Kế Được Cài Đặt

### 1. Singleton Pattern ([singleton.py](singleton.py))

#### Mục đích

Đảm bảo rằng một lớp chỉ có duy nhất một thể hiện (instance) trong suốt vòng đời của ứng dụng và cung cấp một điểm truy cập toàn cục đến thể hiện đó.

#### Đặc điểm chính

- Sử dụng `metaclass` để kiểm soát việc tạo instance
- Thread-safe với việc sử dụng `Lock` để đồng bộ hóa
- Tránh hard-code các thể hiện toàn cục
- Cung cấp lazy initialization (khởi tạo khi cần thiết)

#### Khi nào sử dụng

- **Quản lý kết nối cơ sở dữ liệu**: Đảm bảo chỉ có một kết nối duy nhất được sử dụng trong toàn bộ ứng dụng
- **Quản lý cấu hình ứng dụng**: Cung cấp một thể hiện duy nhất để truy cập và quản lý các thiết lập cấu hình
- **API client**: Đảm bảo chỉ có một thể hiện của client để quản lý các yêu cầu đến một dịch vụ bên ngoài
- **Logger**: Đảm bảo tất cả các phần của ứng dụng sử dụng cùng một instance logger
- **Cache Manager**: Quản lý cache toàn cục cho ứng dụng

#### Ví dụ sử dụng

```python
# Tạo instance đầu tiên
singleton1 = Singleton("FOO")

# Cố gắng tạo instance thứ hai
singleton2 = Singleton("BAR")

# singleton1 và singleton2 trỏ đến cùng một đối tượng
assert singleton1 is singleton2
```

---

### 2. Factory Method Pattern ([factory_method.py](factory_method.py))

#### Mục đích

Định nghĩa một giao diện để tạo đối tượng, nhưng để các lớp con quyết định lớp nào sẽ được khởi tạo. Factory Method cho phép một lớp trì hoãn việc khởi tạo đến các lớp con.

#### Đặc điểm chính

- Tách biệt mã tạo đối tượng khỏi mã sử dụng đối tượng
- Sử dụng kế thừa: việc tạo đối tượng được giao cho các lớp con
- Creator class định nghĩa factory method trả về Product
- Concrete Creators override factory method để tạo các loại Product khác nhau

#### Khi nào sử dụng

- Khi không biết trước chính xác loại đối tượng nào sẽ cần tạo
- Khi muốn cung cấp cho người dùng thư viện khả năng mở rộng các thành phần nội bộ
- Khi muốn tiết kiệm tài nguyên hệ thống bằng cách tái sử dụng các đối tượng hiện có thay vì tạo mới
- **Ví dụ thực tế**: Hệ thống logistics với các phương thức vận chuyển khác nhau (đường bộ, đường biển, đường hàng không)

#### Cấu trúc

```
Creator (abstract)
  └── factory_method() -> Product
  └── some_operation() uses Product

ConcreteCreator1
  └── factory_method() -> ConcreteProduct1

ConcreteCreator2
  └── factory_method() -> ConcreteProduct2
```

---

### 3. Abstract Factory Pattern ([abstract_factory.py](abstract_factory.py))

#### Mục đích

Cung cấp một giao diện để tạo các họ đối tượng liên quan hoặc phụ thuộc mà không cần chỉ định các lớp cụ thể của chúng. Tách biệt việc tạo đối tượng khỏi việc sử dụng đối tượng.

#### Đặc điểm chính

- Tạo các họ (families) đối tượng liên quan
- Sử dụng composition: đối tượng factory được tạo ra và sau đó được sử dụng để tạo các đối tượng khác
- Đảm bảo các sản phẩm được tạo ra tương thích với nhau
- Abstract Factory định nghĩa các phương thức tạo cho mỗi loại sản phẩm

#### Khi nào sử dụng

- **Giao diện người dùng đa nền tảng**: Tạo các thành phần UI phù hợp với từng nền tảng (Windows, macOS, Linux) mà không thay đổi mã chính
- **Hệ thống plugin**: Tạo các đối tượng plugin khác nhau dựa trên loại plugin được chọn
- **Quản lý cấu hình**: Hỗ trợ nhiều cấu hình khác nhau (development, staging, production) với các đối tượng phù hợp
- **Theme system**: Tạo các bộ components nhất quán theo theme (dark theme, light theme)

#### So sánh với Factory Method

| Abstract Factory                         | Factory Method                      |
| ---------------------------------------- | ----------------------------------- |
| Tạo họ đối tượng liên quan               | Tạo một loại đối tượng              |
| Sử dụng composition                      | Sử dụng inheritance                 |
| Có nhiều factory methods                 | Có một factory method               |
| Đảm bảo tính nhất quán giữa các sản phẩm | Tập trung vào việc tạo một sản phẩm |

---

### 4. Builder Pattern ([builder.py](builder.py))

#### Mục đích

Tách biệt việc xây dựng một đối tượng phức tạp khỏi biểu diễn cuối cùng của nó, cho phép cùng một quy trình xây dựng tạo ra các biểu diễn khác nhau.

#### Đặc điểm chính

- Xây dựng đối tượng theo từng bước (step-by-step construction)
- Cho phép tạo các biểu diễn khác nhau của cùng một đối tượng
- Tách biệt mã xây dựng phức tạp khỏi logic nghiệp vụ
- Có thể sử dụng Director để định nghĩa thứ tự các bước xây dựng

#### Khi nào sử dụng

- **Xây dựng tài liệu phức tạp**: Tạo báo cáo, hợp đồng, HTML pages theo từng phần
- **Tạo đối tượng đồ họa**: Xây dựng nhân vật game, 3D models, scenes với nhiều thành phần
- **Cấu hình hệ thống**: Thiết lập các hệ thống phức tạp với nhiều tùy chọn
- **Query builders**: Xây dựng các câu truy vấn SQL phức tạp
- **HTTP request builders**: Tạo HTTP requests với nhiều parameters, headers, body

#### Ví dụ

```python
builder = ConcreteBuilder()
director = Director()
director.builder = builder

# Xây dựng sản phẩm tối giản
director.build_minimal_viable_product()
product = builder.product

# Xây dựng sản phẩm đầy đủ tính năng
director.build_full_featured_product()
product = builder.product
```

#### So sánh với Abstract Factory

| Builder                           | Abstract Factory               |
| --------------------------------- | ------------------------------ |
| Tập trung vào xây dựng từng bước  | Tập trung vào tạo họ đối tượng |
| Trả về sản phẩm ở bước cuối cùng  | Trả về sản phẩm ngay lập tức   |
| Có thể tạo các cấu hình khác nhau | Tạo các sản phẩm hoàn chỉnh    |

---

### 5. Prototype Pattern ([prototype.py](prototype.py))

#### Mục đích

Cho phép sao chép các đối tượng hiện có mà không làm cho mã phụ thuộc vào các lớp cụ thể của chúng. Tạo đối tượng mới bằng cách sao chép một prototype.

#### Đặc điểm chính

- Sử dụng `copy` module của Python với `__copy__()` và `__deepcopy__()`
- **Shallow copy**: Sao chép đối tượng nhưng các thuộc tính tham chiếu vẫn trỏ đến cùng đối tượng gốc
- **Deep copy**: Sao chép đệ quy toàn bộ cây đối tượng
- Tránh chi phí khởi tạo đối tượng phức tạp
- Hữu ích khi việc tạo đối tượng tốn kém về tài nguyên

#### Khi nào sử dụng

- **Tạo bản sao của đối tượng phức tạp**: Khi khởi tạo đòi hỏi nhiều bước cấu hình hoặc tốn kém tài nguyên
- **Quản lý trạng thái đối tượng**: Tạo nhiều phiên bản với các trạng thái khác nhau (undo/redo functionality)
- **Hệ thống đồ họa và game**: Sao chép các đối tượng như nhân vật, items, scenes
- **Configuration objects**: Clone cấu hình với một số thay đổi nhỏ
- **Caching**: Lưu trữ các đối tượng phổ biến và clone khi cần

#### Ví dụ sử dụng

```python
# Tạo đối tượng gốc
original = SomeComponent(
    some_init="Some value",
    some_list_of_objects=[1, 2, 3],
    some_circular_ref=SelfReferencingEntity()
)

# Shallow copy - nhanh nhưng chia sẻ tham chiếu
shallow_copied = copy.copy(original)

# Deep copy - chậm hơn nhưng độc lập hoàn toàn
deep_copied = copy.deepcopy(original)
```

#### Shallow Copy vs Deep Copy

```
Shallow Copy:
original.list     →  [1, 2, 3]  ← shallow_copy.list (cùng object)

Deep Copy:
original.list     →  [1, 2, 3]
deep_copy.list    →  [1, 2, 3]  (object khác, nội dung giống)
```

---

## Khi nào sử dụng mỗi pattern?

### Lựa chọn giữa các patterns

1. **Singleton**: Khi cần đảm bảo chỉ có một instance duy nhất
2. **Factory Method**: Khi cần tạo các đối tượng khác nhau nhưng không biết trước loại cụ thể
3. **Abstract Factory**: Khi cần tạo các họ đối tượng liên quan và đảm bảo chúng tương thích
4. **Builder**: Khi cần xây dựng đối tượng phức tạp theo từng bước với nhiều cấu hình
5. **Prototype**: Khi việc tạo đối tượng mới tốn kém và có thể clone từ đối tượng có sẵn

### Decision Tree

```
Cần kiểm soát số lượng instances?
  └─ YES → Singleton
  └─ NO  → Tiếp tục

Đối tượng có cấu trúc phức tạp?
  └─ YES → Builder
  └─ NO  → Tiếp tục

Cần tạo đối tượng tốn kém?
  └─ YES → Prototype
  └─ NO  → Tiếp tục

Cần tạo họ đối tượng liên quan?
  └─ YES → Abstract Factory
  └─ NO  → Factory Method
```

---

## Best Practices

1. **Singleton**

   - Cẩn thận với multi-threading
   - Tránh lạm dụng (có thể gây khó khăn trong testing)
   - Xem xét dependency injection thay vì Singleton

2. **Factory Method & Abstract Factory**

   - Đặt tên factory methods có ý nghĩa (create..., make..., build...)
   - Giữ factory logic đơn giản
   - Sử dụng type hints để tăng tính rõ ràng

3. **Builder**

   - Cung cấp method chaining cho fluent interface
   - Validate trước khi xây dựng sản phẩm cuối cùng
   - Cân nhắc immutable products

4. **Prototype**
   - Xác định rõ khi nào cần shallow copy vs deep copy
   - Cẩn thận với circular references
   - Document rõ hành vi copy của class

---

## Tài liệu tham khảo

- [Design Patterns: Elements of Reusable Object-Oriented Software (Gang of Four)](https://en.wikipedia.org/wiki/Design_Patterns)
- [Refactoring Guru - Creational Patterns](https://refactoring.guru/design-patterns/creational-patterns)
- [Python Design Patterns](https://python-patterns.guide/)

---

## Cách chạy các ví dụ

Mỗi file Python có thể chạy độc lập:

```bash
# Chạy ví dụ Singleton
python singleton.py

# Chạy ví dụ Factory Method
python factory_method.py

# Chạy ví dụ Abstract Factory
python abstract_factory.py

# Chạy ví dụ Builder
python builder.py

# Chạy ví dụ Prototype
python prototype.py
```

---

**Lưu ý**: Các mẫu thiết kế là các giải pháp chung cho các vấn đề thường gặp trong thiết kế phần mềm. Chúng không phải là code có thể copy-paste mà là các template để giải quyết vấn đề trong nhiều tình huống khác nhau.
