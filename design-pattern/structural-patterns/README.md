# Structural Patterns - Các Mẫu Thiết Kế Cấu Trúc

## Tổng Quan

Các mẫu thiết kế cấu trúc (Structural Patterns) liên quan đến cách các lớp và đối tượng được kết hợp để tạo thành các cấu trúc lớn hơn. Các mẫu này giúp đảm bảo rằng nếu một phần của hệ thống thay đổi, toàn bộ cấu trúc không cần phải thay đổi. Chúng tập trung vào việc đơn giản hóa cấu trúc bằng cách xác định mối quan hệ giữa các entities.

## Các Mẫu Thiết Kế Được Cài Đặt

### 1. Adapter Pattern ([adapter.py](adapter.py))

#### Mục đích

Cho phép các interface không tương thích làm việc cùng nhau. Adapter đóng vai trò như một wrapper chuyển đổi interface của một lớp thành interface mà client mong đợi.

#### Đặc điểm chính

- Chuyển đổi interface của một class thành interface khác
- Cho phép các class không tương thích làm việc cùng nhau
- Wrap một object hiện có với interface mới
- Sử dụng multiple inheritance hoặc composition

#### Khi nào sử dụng

- **Tích hợp hệ thống legacy**: Khi cần sử dụng class hiện có nhưng interface không tương thích với code mới
- **Third-party libraries**: Khi muốn sử dụng library bên ngoài nhưng interface không phù hợp
- **Multiple data sources**: Chuẩn hóa interface cho các nguồn dữ liệu khác nhau (APIs, databases)
- **Payment gateways**: Tạo interface thống nhất cho nhiều payment providers khác nhau

#### Ví dụ thực tế

```python
# Adaptee có interface không tương thích
adaptee = Adaptee()  # specific_request() -> ".eetpadA..."

# Adapter chuyển đổi interface
adapter = Adapter()  # request() -> "Adapter: (TRANSLATED) Special..."

# Client code làm việc với interface thống nhất
client_code(adapter)
```

#### Các loại Adapter

- **Class Adapter**: Sử dụng multiple inheritance
- **Object Adapter**: Sử dụng composition (chứa reference đến adaptee)

---

### 2. Bridge Pattern ([bridge.py](bridge.py))

#### Mục đích

Tách biệt abstraction khỏi implementation để cả hai có thể thay đổi độc lập. Thay vì tạo một hệ thống phân cấp lớp lớn, Bridge chia thành hai hệ thống phân cấp riêng biệt.

#### Đặc điểm chính

- Tách abstraction và implementation thành hai hierarchies riêng
- Composition thay vì inheritance
- Abstraction chứa reference đến Implementation
- Cho phép thay đổi implementation runtime

#### Khi nào sử dụng

- **Đa nền tảng**: Ứng dụng cần chạy trên nhiều platforms (Windows, Linux, MacOS)
- **Multiple dimensions of variation**: Device và Remote control cho TV, Radio, etc.
- **Database drivers**: Tách logic truy vấn khỏi database cụ thể (MySQL, PostgreSQL, MongoDB)
- **UI frameworks**: Tách components khỏi rendering engine

#### Problem without Bridge

```
Shape
├── CircleWindows
├── CircleLinux
├── SquareWindows
└── SquareLinux
    (Sẽ tạo n × m classes nếu có n shapes và m platforms!)
```

#### Solution with Bridge

```
Shape (Abstraction)          Platform (Implementation)
├── Circle                   ├── Windows
└── Square                   └── Linux
    (Chỉ cần n + m classes!)
```

#### Ví dụ sử dụng

```python
# Tạo implementation cụ thể
implementation = ConcreteImplementationA()

# Tạo abstraction với implementation
abstraction = Abstraction(implementation)
abstraction.operation()

# Dễ dàng thay đổi implementation
implementation = ConcreteImplementationB()
abstraction = ExtendedAbstraction(implementation)
```

---

### 3. Composite Pattern ([composite.py](composite.py))

#### Mục đích

Cho phép tạo cấu trúc cây để biểu diễn phân cấp part-whole. Composite cho phép client xử lý các đối tượng đơn lẻ và tổ hợp đối tượng một cách đồng nhất.

#### Đặc điểm chính

- Tạo cấu trúc cây các objects
- Xử lý objects đơn lẻ (Leaf) và composite objects theo cách giống nhau
- Client không cần biết đang làm việc với Leaf hay Composite
- Recursive composition

#### Khi nào sử dụng

- **File systems**: Files và folders (folder chứa files và folders con)
- **Organization charts**: Employees và departments
- **UI components**: Containers chứa các widgets hoặc containers khác
- **Graphics**: Shapes đơn giản và grouped shapes
- **Menu systems**: Menu items và submenus

#### Cấu trúc

```
Component (interface)
├── Leaf (không có children)
└── Composite (có children)
    ├── Leaf
    ├── Composite
    │   ├── Leaf
    │   └── Leaf
    └── Leaf
```

#### Ví dụ sử dụng

```python
# Tạo cây components
tree = Composite()

# Branch 1
branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())

# Branch 2
branch2 = Composite()
branch2.add(Leaf())

# Tạo cây
tree.add(branch1)
tree.add(branch2)
tree.add(Leaf())

# Xử lý toàn bộ cây như một đối tượng duy nhất
tree.operation()
```

---

### 4. Decorator Pattern ([decorator.py](decorator.py))

#### Mục đích

Cho phép thêm hành vi mới vào đối tượng bằng cách đặt chúng vào trong các wrapper objects chứa các hành vi đó. Decorator cung cấp một giải pháp linh hoạt thay thế cho subclassing.

#### Đặc điểm chính

- Thêm responsibilities mới cho objects dynamically
- Wrapping objects với decorators
- Có thể stack nhiều decorators
- Tuân theo Interface Segregation Principle
- Alternative linh hoạt hơn so với inheritance

#### Khi nào sử dụng

- **I/O Streams**: BufferedReader, GZipInputStream wrapping FileInputStream
- **Logging**: Thêm logging vào functions mà không thay đổi code
- **Authorization**: Thêm permission checks
- **Caching**: Thêm caching layer
- **Validation**: Thêm input validation
- **UI enhancements**: Thêm scrollbars, borders cho components

#### Ví dụ thực tế

```python
# Component cơ bản
simple = ConcreteComponent()
# Output: "ConcreteComponent"

# Thêm decorator A
decorator1 = ConcreteDecoratorA(simple)
# Output: "ConcreteDecoratorA(ConcreteComponent)"

# Thêm decorator B (wrapping decorator A)
decorator2 = ConcreteDecoratorB(decorator1)
# Output: "ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))"
```

#### Python Decorators

Python có built-in decorator syntax:

```python
@ConcreteDecoratorA
@ConcreteDecoratorB
def my_function():
    pass
```

---

### 5. Facade Pattern ([facade.py](facade.py))

#### Mục đích

Cung cấp một interface đơn giản, thống nhất cho một tập hợp các interfaces trong một subsystem. Facade định nghĩa interface high-level giúp subsystem dễ sử dụng hơn.

#### Đặc điểm chính

- Đơn giản hóa interface phức tạp
- Giảm sự phụ thuộc giữa client và subsystem
- Không ngăn cản truy cập trực tiếp vào subsystem
- Có thể có nhiều facades cho cùng một subsystem

#### Khi nào sử dụng

- **Complex libraries**: Đơn giản hóa việc sử dụng thư viện phức tạp
- **Layered architecture**: Tạo entry point cho mỗi layer
- **Legacy code**: Wrap legacy code với interface hiện đại
- **Video conversion**: Ẩn chi tiết của codecs, containers, formats
- **E-commerce checkout**: Đơn giản hóa payment, shipping, inventory processes

#### Ví dụ

```python
# Thay vì:
subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
subsystem1.operation1()
subsystem2.operation1()
subsystem1.operation_n()
subsystem2.operation_z()

# Sử dụng Facade:
facade = Facade(subsystem1, subsystem2)
facade.operation()  # Làm tất cả những điều trên
```

#### Facade vs Adapter

| Facade                     | Adapter                    |
| -------------------------- | -------------------------- |
| Đơn giản hóa interface     | Thay đổi interface         |
| Làm việc với nhiều classes | Làm việc với một class     |
| Định nghĩa interface mới   | Match với interface có sẵn |

---

### 6. Flyweight Pattern ([flyweight.py](flyweight.py))

#### Mục đích

Sử dụng sharing để hỗ trợ hiệu quả một số lượng lớn các objects có kích thước nhỏ. Tiết kiệm RAM bằng cách chia sẻ các phần chung của state giữa nhiều objects.

#### Đặc điểm chính

- **Intrinsic state**: State được chia sẻ, không thay đổi, lưu trong Flyweight
- **Extrinsic state**: State unique cho mỗi object, được truyền vào methods
- FlyweightFactory quản lý pool of flyweights
- Tiết kiệm memory đáng kể khi có nhiều objects tương tự

#### Khi nào sử dụng

- **Game development**: Hàng nghìn particles, bullets, trees cùng loại
- **Text editors**: Chia sẻ character formatting data
- **Graphics**: Rendering nhiều objects giống nhau
- **Caching**: String interning, database connections
- **Large datasets**: Khi có nhiều objects với data giống nhau

#### Ví dụ thực tế

```python
# Intrinsic state (shared): brand, model, color
# Extrinsic state (unique): plates, owner

factory = FlyweightFactory([
    ["BMW", "M5", "red"],
    ["BMW", "X6", "white"],
])

# Reuse flyweight cho BMW M5 red
add_car("CL234IR", "James", "BMW", "M5", "red")  # Reuse
add_car("CL567AB", "John", "BMW", "M5", "red")   # Reuse

# Create new flyweight
add_car("CL890CD", "Jane", "Audi", "A4", "black")  # New
```

#### Memory Savings

```
Without Flyweight:
1,000,000 cars × 100 bytes = 100 MB

With Flyweight:
100 unique models × 100 bytes = 10 KB (shared)
1,000,000 records × 10 bytes = 10 MB (unique)
Total = ~10 MB (90% savings!)
```

---

### 7. Proxy Pattern ([proxy.py](proxy.py))

#### Mục đích

Cung cấp một placeholder hoặc surrogate cho một object khác để kiểm soát quyền truy cập vào nó. Proxy có cùng interface với object gốc.

#### Đặc điểm chính

- Kiểm soát truy cập đến object gốc
- Có thể thêm logic trước/sau khi gọi object gốc
- Lazy initialization
- Cùng interface với RealSubject

#### Các loại Proxy

1. **Virtual Proxy**: Lazy loading objects tốn kém
2. **Protection Proxy**: Access control và permissions
3. **Remote Proxy**: Đại diện cho object ở remote location (RPC, REST API)
4. **Logging Proxy**: Log các requests
5. **Caching Proxy**: Cache kết quả
6. **Smart Reference**: Đếm references, cleanup khi không còn sử dụng

#### Khi nào sử dụng

- **Lazy initialization**: Trì hoãn tạo object tốn kém cho đến khi cần thiết
- **Access control**: Kiểm tra permissions trước khi cho phép truy cập
- **Logging**: Log tất cả requests đến object
- **Caching**: Cache kết quả của operations tốn kém
- **Remote objects**: Database connections, web services
- **Resource management**: Connection pooling

#### Ví dụ sử dụng

```python
# Sử dụng trực tiếp
real_subject = RealSubject()
real_subject.request()

# Sử dụng qua Proxy
proxy = Proxy(real_subject)
proxy.request()
# Output:
# Proxy: Checking access prior to firing a real request.
# RealSubject: Handling request.
# Proxy: Logging the time of request.
```

#### Proxy vs Decorator

| Proxy                            | Decorator               |
| -------------------------------- | ----------------------- |
| Kiểm soát truy cập               | Thêm responsibilities   |
| Quản lý lifecycle                | Wrapping behaviors      |
| Có thể không tạo object gốc ngay | Luôn wrap object có sẵn |
| Cùng interface                   | Có thể extend interface |

---

## So Sánh Các Patterns

### Adapter vs Bridge vs Facade vs Proxy

| Pattern     | Purpose                           | Structure          |
| ----------- | --------------------------------- | ------------------ |
| **Adapter** | Chuyển đổi interface              | Wrap một object    |
| **Bridge**  | Tách abstraction & implementation | Hai hierarchies    |
| **Facade**  | Đơn giản hóa interface            | Wrap nhiều objects |
| **Proxy**   | Kiểm soát truy cập                | Same interface     |

### Decorator vs Composite

| Decorator                | Composite            |
| ------------------------ | -------------------- |
| Thêm responsibilities    | Tạo cấu trúc cây     |
| Có thể có nhiều wrappers | Part-whole hierarchy |
| Focus vào enhancement    | Focus vào structure  |

---

## Khi nào sử dụng mỗi pattern?

### Decision Tree

```
Cần chuyển đổi interface?
  └─ YES → Adapter

Cần tách abstraction khỏi implementation?
  └─ YES → Bridge

Cần đơn giản hóa subsystem phức tạp?
  └─ YES → Facade

Cần tạo cấu trúc cây?
  └─ YES → Composite

Cần thêm behavior dynamically?
  └─ YES → Decorator

Cần tiết kiệm memory với nhiều objects?
  └─ YES → Flyweight

Cần kiểm soát truy cập?
  └─ YES → Proxy
```

---

## Best Practices

### Adapter

- Ưu tiên object adapter (composition) hơn class adapter (inheritance)
- Document rõ những gì được adapted
- Cân nhắc tạo two-way adapter nếu cần

### Bridge

- Sử dụng khi có nhiều dimensions of variation
- Giữ abstraction và implementation độc lập
- Sử dụng dependency injection cho flexibility

### Composite

- Implement parent reference cẩn thận (có thể gây circular references)
- Cân nhắc visitor pattern cho operations phức tạp
- Validate tree structure integrity

### Decorator

- Giữ decorator interface giống với component
- Có thể chain nhiều decorators
- Cẩn thận với ordering (thứ tự decorators quan trọng)

### Facade

- Không ẩn hoàn toàn subsystem (cho phép advanced users)
- Có thể tạo nhiều facades cho use cases khác nhau
- Giữ facade stateless nếu có thể

### Flyweight

- Chỉ sử dụng khi có nhiều objects tương tự nhau
- Tách biệt intrinsic và extrinsic state rõ ràng
- Cân nhắc thread safety cho FlyweightFactory

### Proxy

- Document rõ proxy behavior (caching, logging, etc.)
- Cân nhắc transparent proxy vs explicit proxy
- Handle errors từ real subject properly

---

## Ví Dụ Thực Tế Kết Hợp

### Ví dụ 1: Image Loading System

```
Proxy (lazy loading) + Flyweight (sharing textures) + Composite (grouping)
```

### Ví dụ 2: UI Framework

```
Composite (hierarchy) + Decorator (scrollbars, borders) + Facade (simple API)
```

### Ví dụ 3: Database Access

```
Adapter (different DBs) + Proxy (connection pooling) + Bridge (query abstraction)
```

---

## Cách chạy các ví dụ

```bash
# Chạy ví dụ Adapter
python adapter.py

# Chạy ví dụ Bridge
python bridge.py

# Chạy ví dụ Composite
python composite.py

# Chạy ví dụ Decorator
python decorator.py

# Chạy ví dụ Facade
python facade.py

# Chạy ví dụ Flyweight
python flyweight.py

# Chạy ví dụ Proxy
python proxy.py
```

---

## Tài Liệu Tham Khảo

- [Design Patterns: Elements of Reusable Object-Oriented Software (Gang of Four)](https://en.wikipedia.org/wiki/Design_Patterns)
- [Refactoring Guru - Structural Patterns](https://refactoring.guru/design-patterns/structural-patterns)
- [Python Design Patterns Guide](https://python-patterns.guide/)

---

**Lưu ý quan trọng**: Structural patterns giúp tổ chức code tốt hơn, nhưng đừng over-engineer. Sử dụng patterns khi chúng thực sự giải quyết vấn đề bạn đang gặp phải, không phải vì muốn sử dụng patterns.
