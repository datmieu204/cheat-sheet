# Behavioral Patterns - Các Mẫu Thiết Kế Hành Vi

## Tổng Quan

Các mẫu thiết kế hành vi (Behavioral Patterns) tập trung vào cách các objects giao tiếp và phân phối trách nhiệm giữa chúng. Những mẫu này không chỉ mô tả cấu trúc của objects hoặc classes mà còn mô tả các patterns của communication giữa chúng, giúp tăng tính linh hoạt trong việc thực hiện communication này.

## Các Mẫu Thiết Kế Được Cài Đặt

### 1. Command Pattern ([command.py](command.py))

#### Mục đích

Biến một request thành một object độc lập chứa tất cả thông tin về request đó. Điều này cho phép parameterize clients với các requests khác nhau, queue hoặc log requests, và hỗ trợ undo operations.

#### Đặc điểm chính

- Encapsulate request như một object
- Tách biệt sender và receiver
- Hỗ trợ queuing, logging, undo/redo
- Command object chứa receiver và parameters
- Invoker không cần biết chi tiết về request

#### Thành phần chính

- **Command Interface**: Định nghĩa execute() method
- **ConcreteCommand**: Implement execute(), liên kết Receiver với action
- **Receiver**: Object thực sự thực hiện công việc
- **Invoker**: Yêu cầu command execute
- **Client**: Tạo commands và set receivers

#### Khi nào sử dụng

- **Undo/Redo**: Text editors, graphic editors
- **Macro recording**: Ghi lại sequence of operations
- **Task scheduling**: Job queues, thread pools
- **Transaction management**: Database transactions, rollback
- **GUI buttons**: Mỗi button gắn với một command
- **Remote control**: Universal remote với nhiều devices

#### Ví dụ sử dụng

```python
# Tạo receiver
receiver = Receiver()

# Tạo commands
simple_command = SimpleCommand("Say Hi")
complex_command = ComplexCommand(receiver, "data1", "data2")

# Tạo invoker và set commands
invoker = Invoker()
invoker.set_on_start(simple_command)
invoker.set_on_finish(complex_command)

# Execute
invoker.do_something_important()
```

#### Lợi ích

- **Single Responsibility**: Tách operation invocation khỏi execution
- **Open/Closed**: Thêm commands mới không cần sửa code cũ
- **Undo/Redo**: Dễ dàng implement
- **Deferred execution**: Execute commands sau
- **Composite commands**: Kết hợp nhiều commands

---

### 2. Iterator Pattern ([iterator.py](iterator.py))

#### Mục đích

Cung cấp cách truy cập tuần tự các phần tử của một aggregate object mà không cần expose internal representation của nó.

#### Đặc điểm chính

- Duyệt qua collection mà không expose cấu trúc bên trong
- Hỗ trợ nhiều cách duyệt khác nhau
- Interface thống nhất cho các loại collections khác nhau
- Python có built-in iterator protocol (`__iter__`, `__next__`)

#### Thành phần chính

- **Iterator Interface**: `__next__()` method
- **Concrete Iterator**: Implement traversal algorithm
- **Iterable Interface**: `__iter__()` method trả về iterator
- **Concrete Collection**: Return concrete iterator

#### Khi nào sử dụng

- **Traverse complex structures**: Trees, graphs, custom collections
- **Multiple traversal algorithms**: Forward, backward, filtered
- **Unified interface**: Duyệt các collections khác nhau cùng một cách
- **Lazy loading**: Không load hết data vào memory
- **Data streaming**: Process data theo chunks

#### Ví dụ sử dụng

```python
# Tạo collection
collection = WordsCollection()
collection.add_item("B")
collection.add_item("A")
collection.add_item("C")

# Forward iteration
for item in collection:
    print(item)  # A, B, C (sorted)

# Reverse iteration
reverse_iterator = collection.get_reverse_iterator()
for item in reverse_iterator:
    print(item)  # C, B, A
```

#### Python Iterator Protocol

```python
class MyIterator:
    def __iter__(self):
        return self

    def __next__(self):
        if self._position >= len(self._data):
            raise StopIteration
        value = self._data[self._position]
        self._position += 1
        return value
```

#### Generators (Python's Iterator Sugar)

```python
def my_generator():
    yield 1
    yield 2
    yield 3

for item in my_generator():
    print(item)
```

---

### 3. Observer Pattern ([observer.py](observer.py))

#### Mục đích

Định nghĩa one-to-many dependency giữa objects sao cho khi một object thay đổi state, tất cả dependents của nó được notify và update tự động.

#### Đặc điểm chính

- Subject duy trì list of observers
- Observers subscribe/unsubscribe để nhận updates
- Subject notify tất cả observers khi state thay đổi
- Loose coupling giữa subject và observers
- Push model (subject push data) hoặc Pull model (observers pull data)

#### Thành phần chính

- **Subject**: Quản lý observers, notify khi có thay đổi
- **Observer Interface**: update() method
- **ConcreteSubject**: Lưu state, notify observers khi state thay đổi
- **ConcreteObserver**: Implement update() để đồng bộ với subject

#### Khi nào sử dụng

- **Event handling**: GUI events, user interactions
- **Model-View pattern**: MVC, MVVM architectures
- **Pub/Sub systems**: Message queues, event buses
- **Data binding**: Automatic UI updates
- **Real-time updates**: Stock prices, news feeds, notifications
- **Distributed systems**: Event-driven microservices

#### Ví dụ sử dụng

```python
# Tạo subject
subject = ConcreteSubject()

# Tạo observers
observer1 = ConcreteObserverA()
observer2 = ConcreteObserverB()

# Subscribe
subject.attach(observer1)
subject.attach(observer2)

# Thay đổi state → observers được notify tự động
subject.some_business_logic()

# Unsubscribe
subject.detach(observer1)
```

#### Push vs Pull Model

**Push Model**: Subject gửi detailed data

```python
def update(self, subject: Subject, data: Any):
    # Subject push data đến observer
    self.process(data)
```

**Pull Model**: Observer lấy data từ subject

```python
def update(self, subject: Subject):
    # Observer pull data từ subject
    data = subject.get_state()
    self.process(data)
```

#### Observer vs Pub/Sub

| Observer                  | Pub/Sub                           |
| ------------------------- | --------------------------------- |
| Observers biết về subject | Publishers không biết subscribers |
| Direct coupling           | Event channel trung gian          |
| Synchronous               | Có thể asynchronous               |
| Single application        | Distributed systems               |

---

### 4. State Pattern ([state.py](state.py))

#### Mục đích

Cho phép một object thay đổi behavior khi internal state thay đổi. Object sẽ xuất hiện như thể đã thay đổi class của nó.

#### Đặc điểm chính

- Encapsulate state-specific behavior trong các State classes
- Context delegate behavior cho current State object
- State transitions có thể do Context hoặc State objects quyết định
- Tránh large conditional statements (if/else, switch/case)

#### Thành phần chính

- **Context**: Duy trì reference đến current State, delegate requests
- **State Interface**: Định nghĩa interface cho các states
- **ConcreteState**: Implement behavior cho mỗi state cụ thể

#### Khi nào sử dụng

- **State machines**: Workflow systems, game character states
- **Document states**: Draft, moderation, published
- **Connection states**: Connected, disconnected, connecting
- **Order processing**: Pending, processing, shipped, delivered
- **Media player**: Playing, paused, stopped
- **UI states**: Enabled, disabled, loading

#### Ví dụ sử dụng

```python
# Tạo context với initial state
context = Context(ConcreteStateA())

# Request làm state transition
context.request1()  # StateA → StateB
context.request2()  # StateB → StateA
```

#### State Diagram Example

```
[Draft] ─submit→ [Moderation] ─approve→ [Published]
   ↑                  │
   └──────reject──────┘
```

#### State vs Strategy

| State                               | Strategy                              |
| ----------------------------------- | ------------------------------------- |
| State tự transition sang state khác | Strategy không thay đổi strategy khác |
| State biết về nhau                  | Strategies độc lập                    |
| Behavior thay đổi theo state        | Behavior do client chọn               |
| Context delegate                    | Context dùng strategy                 |

---

### 5. Strategy Pattern ([strategy.py](strategy.py))

#### Mục đích

Định nghĩa một họ algorithms, encapsulate mỗi cái, và làm cho chúng interchangeable. Strategy cho phép algorithm thay đổi độc lập với clients sử dụng nó.

#### Đặc điểm chính

- Encapsulate algorithms trong các Strategy classes
- Context sử dụng Strategy interface
- Strategies có thể thay đổi runtime
- Client chọn strategy phù hợp
- Alternative cho inheritance với nhiều subclasses

#### Thành phần chính

- **Context**: Duy trì reference đến Strategy
- **Strategy Interface**: Common interface cho tất cả algorithms
- **ConcreteStrategy**: Implement các algorithms cụ thể

#### Khi nào sử dụng

- **Multiple algorithms**: Sorting, compression, encryption
- **Payment processing**: Credit card, PayPal, crypto
- **Route planning**: Fastest, shortest, scenic
- **Validation**: Different validation rules
- **Export formats**: PDF, Excel, CSV, JSON
- **Pricing strategies**: Regular, discount, seasonal

#### Ví dụ sử dụng

```python
# Tạo context với strategy A
context = Context(ConcreteStrategyA())
context.do_some_business_logic()
# Output: a,b,c,d,e (sorted)

# Thay đổi strategy runtime
context.strategy = ConcreteStrategyB()
context.do_some_business_logic()
# Output: e,d,c,b,a (reverse sorted)
```

#### Real-world Example: Payment

```python
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using Credit Card")

class PayPalStrategy(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal")

# Client chọn strategy
checkout = Checkout(CreditCardStrategy())
checkout.process_payment(100.0)
```

#### Strategy vs State vs Command

| Pattern      | Purpose                    |
| ------------ | -------------------------- |
| **Strategy** | Interchangeable algorithms |
| **State**    | State-dependent behavior   |
| **Command**  | Encapsulate requests       |

---

### 6. Template Method Pattern ([tempalate_method.py](template_method.py))

**Lưu ý**: File có typo trong tên: `tempalate_method.py` nên là `template_method.py`

#### Mục đích

Định nghĩa skeleton của một algorithm trong một method, defer một số steps cho subclasses. Template Method cho phép subclasses redefine một số steps của algorithm mà không thay đổi structure của algorithm.

#### Đặc điểm chính

- Base class định nghĩa algorithm structure
- Subclasses implement specific steps
- "Don't call us, we'll call you" (Hollywood Principle)
- Hooks cho optional customization
- Code reuse thông qua inheritance

#### Thành phần chính

- **AbstractClass**: Định nghĩa template method và primitive operations
- **ConcreteClass**: Implement primitive operations
- **Template Method**: Định nghĩa skeleton, gọi primitive operations
- **Hooks**: Optional methods subclasses có thể override

#### Khi nào sử dụng

- **Frameworks**: Framework định nghĩa workflow, app implement steps
- **Data processing**: Common structure, different implementations
- **Testing**: Test case setup → execute → teardown
- **Data mining**: Connect → extract → parse → analyze → close
- **Game development**: Initialize → start → update → render → cleanup

#### Ví dụ sử dụng

```python
# Template method định nghĩa algorithm structure
class AbstractClass:
    def template_method(self):
        self.base_operation1()
        self.required_operations1()  # Subclass implement
        self.base_operation2()
        self.hook1()                  # Optional override
        self.required_operations2()   # Subclass implement
        self.base_operation3()
        self.hook2()                  # Optional override

# Subclass implement required operations
class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass1: Operation1")

    def required_operations2(self):
        print("ConcreteClass1: Operation2")
```

#### Template Method Structure

```
template_method() [final]
├── base_operation1()        [implemented]
├── required_operation1()    [abstract - must implement]
├── base_operation2()        [implemented]
├── hook1()                  [optional - can override]
├── required_operation2()    [abstract - must implement]
├── base_operation3()        [implemented]
└── hook2()                  [optional - can override]
```

#### Types of Operations

1. **Concrete Operations**: Implemented trong abstract class
2. **Abstract Operations**: Must be implemented bởi subclasses
3. **Hooks**: Empty hoặc default implementation, có thể override

#### Real-world Example: Data Processing

```python
class DataProcessor(ABC):
    def process(self):
        data = self.read_data()      # Abstract
        parsed = self.parse_data(data)  # Abstract
        analyzed = self.analyze_data(parsed)  # Concrete
        self.send_report(analyzed)   # Concrete
        self.post_process()          # Hook

    @abstractmethod
    def read_data(self): pass

    @abstractmethod
    def parse_data(self, data): pass

    def post_process(self):
        pass  # Hook - optional

class CSVProcessor(DataProcessor):
    def read_data(self):
        return read_csv_file()

    def parse_data(self, data):
        return parse_csv(data)

class JSONProcessor(DataProcessor):
    def read_data(self):
        return read_json_file()

    def parse_data(self, data):
        return parse_json(data)
```

#### Template Method vs Strategy

| Template Method          | Strategy                |
| ------------------------ | ----------------------- |
| Sử dụng inheritance      | Sử dụng composition     |
| Compile-time flexibility | Runtime flexibility     |
| Controls structure       | Encapsulates algorithm  |
| Subclass override steps  | Client chooses strategy |

---

## So Sánh Các Patterns

### Communication Patterns

| Pattern                     | Communication Style                      |
| --------------------------- | ---------------------------------------- |
| **Command**                 | One sender → One receiver (encapsulated) |
| **Observer**                | One subject → Many observers             |
| **Chain of Responsibility** | Sender → Chain of handlers               |
| **Mediator**                | Many objects ↔ Central mediator          |

### Algorithm Patterns

| Pattern             | Algorithm Control                |
| ------------------- | -------------------------------- |
| **Strategy**        | Client chọn algorithm            |
| **Template Method** | Superclass định nghĩa structure  |
| **State**           | State object quyết định behavior |
| **Command**         | Encapsulate algorithm as object  |

### Responsibility Patterns

| Pattern             | Responsibility Distribution              |
| ------------------- | ---------------------------------------- |
| **Visitor**         | Add operations without modifying classes |
| **Iterator**        | Sequential access                        |
| **Memento**         | Save/restore state                       |
| **Template Method** | Define algorithm structure               |

---

## Khi nào sử dụng mỗi pattern?

### Decision Guide

```
Cần encapsulate requests?
  └─ YES → Command

Cần notify nhiều objects về changes?
  └─ YES → Observer

Behavior thay đổi theo state?
  └─ YES → State

Cần switch algorithms runtime?
  └─ YES → Strategy

Cần traverse collection?
  └─ YES → Iterator

Cần định nghĩa algorithm skeleton?
  └─ YES → Template Method
```

### Use Case Matrix

| Use Case            | Recommended Pattern |
| ------------------- | ------------------- |
| Undo/Redo           | Command             |
| Event system        | Observer            |
| State machine       | State               |
| Plugin system       | Strategy            |
| Data traversal      | Iterator            |
| Framework extension | Template Method     |

---

## Best Practices

### Command Pattern

- Keep commands simple và focused
- Consider composite commands cho macro operations
- Implement memento pattern cho complex undo
- Use command queue cho async execution

### Iterator Pattern

- Trong Python, prefer generators khi có thể
- Implement `__iter__` và `__next__` properly
- Raise `StopIteration` khi hết elements
- Consider lazy loading cho large datasets

### Observer Pattern

- Cẩn thận với memory leaks (unsubscribe khi không cần)
- Consider weak references
- Avoid cyclic dependencies
- Document notification order nếu quan trọng

### State Pattern

- Mỗi state class nên self-contained
- Document state diagram rõ ràng
- Consider state factory cho complex initialization
- Use enum cho state types

### Strategy Pattern

- Strategies nên stateless nếu có thể
- Use dependency injection
- Consider strategy factory
- Document khi nào dùng strategy nào

### Template Method Pattern

- Document which methods must be overridden
- Use meaningful names cho hooks
- Keep template method final (không cho override)
- Consider providing default hook implementations

---

## Anti-patterns và Pitfalls

### Command

❌ **Bloated commands**: Commands chứa quá nhiều logic
✅ **Solution**: Delegate logic cho receiver

### Observer

❌ **Memory leaks**: Observers không unsubscribe
✅ **Solution**: Use weak references hoặc explicit cleanup

### State

❌ **State explosion**: Quá nhiều states
✅ **Solution**: Combine states, use hierarchical state machines

### Strategy

❌ **Wrong abstraction**: Strategy interface không phù hợp
✅ **Solution**: Refactor interface dựa trên common operations

### Iterator

❌ **Modifying collection during iteration**
✅ **Solution**: Use copy hoặc concurrent collections

### Template Method

❌ **Rigid structure**: Không có hooks cho customization
✅ **Solution**: Thêm hooks ở các điểm quan trọng

---

## Ví Dụ Thực Tế Kết Hợp Patterns

### Example 1: Text Editor

```
Command (undo/redo) + Observer (UI updates) + State (tool modes)
```

### Example 2: Game Engine

```
State (character states) + Observer (events) + Strategy (AI behavior)
+ Template Method (game loop)
```

### Example 3: Data Pipeline

```
Template Method (pipeline structure) + Strategy (processors)
+ Iterator (data streaming) + Command (operations)
```

### Example 4: Web Framework

```
Template Method (request handling) + Observer (middleware)
+ Strategy (routing) + Command (actions)
```

---

## Cách chạy các ví dụ

```bash
# Chạy ví dụ Command
python command.py

# Chạy ví dụ Iterator
python iterator.py

# Chạy ví dụ Observer
python observer.py

# Chạy ví dụ State
python state.py

# Chạy ví dụ Strategy
python strategy.py

# Chạy ví dụ Template Method
python tempalate_method.py
```

---

## Tài Liệu Tham Khảo

- [Design Patterns: Elements of Reusable Object-Oriented Software (Gang of Four)](https://en.wikipedia.org/wiki/Design_Patterns)
- [Refactoring Guru - Behavioral Patterns](https://refactoring.guru/design-patterns/behavioral-patterns)
- [Python Design Patterns Guide](https://python-patterns.guide/)
- [Head First Design Patterns](https://www.oreilly.com/library/view/head-first-design/0596007124/)

---

## Các Pattern Khác (Chưa Implement)

Dưới đây là các behavioral patterns phổ biến khác chưa có trong repository:

### Chain of Responsibility

Pass request dọc theo chain of handlers cho đến khi có handler xử lý

### Mediator

Centralize complex communications giữa các objects

### Memento

Capture và restore object state mà không vi phạm encapsulation

### Visitor

Add operations cho objects mà không thay đổi classes của chúng

### Interpreter

Implement specialized language hoặc grammar

---

**Lưu ý quan trọng**: Behavioral patterns về communication và responsibility distribution. Chọn pattern phù hợp với communication needs của hệ thống. Đừng force patterns nếu simple solution đủ tốt - "Keep it simple" vẫn là nguyên tắc quan trọng nhất!
