# 🎨 Design Patterns - 设计模式示例库

一个全面的设计模式示例库，包含23种经典设计模式的Python实现，配有详细的代码示例、使用场景和最佳实践。

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Patterns](https://img.shields.io/badge/Patterns-23-orange.svg)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)

## ✨ 核心功能

### 📚 创建型模式 (Creational Patterns)
- **单例模式 (Singleton)** - 确保类只有一个实例
- **工厂方法模式 (Factory Method)** - 定义创建对象的接口
- **抽象工厂模式 (Abstract Factory)** - 创建相关对象的家族
- **建造者模式 (Builder)** - 分步骤创建复杂对象
- **原型模式 (Prototype)** - 通过克隆创建对象

### 🔧 结构型模式 (Structural Patterns)
- **适配器模式 (Adapter)** - 接口转换
- **装饰器模式 (Decorator)** - 动态添加功能
- **代理模式 (Proxy)** - 控制对象访问
- **外观模式 (Facade)** - 简化复杂接口
- **桥接模式 (Bridge)** - 分离抽象和实现
- **组合模式 (Composite)** - 树形结构
- **享元模式 (Flyweight)** - 共享对象

### 🎯 行为型模式 (Behavioral Patterns)
- **策略模式 (Strategy)** - 算法族封装
- **观察者模式 (Observer)** - 订阅-发布机制
- **模板方法模式 (Template Method)** - 算法骨架
- **命令模式 (Command)** - 请求封装
- **责任链模式 (Chain of Responsibility)** - 请求传递
- **迭代器模式 (Iterator)** - 遍历集合
- **中介者模式 (Mediator)** - 对象间通信
- **备忘录模式 (Memento)** - 状态保存
- **状态模式 (State)** - 对象状态管理
- **访问者模式 (Visitor)** - 操作分离
- **解释器模式 (Interpreter)** - 语言解释

## 🏗️ 设计模式分类

```
┌─────────────────────────────────────────────────────────┐
│                  设计模式分类体系                        │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│              创建型模式 (Creational)                     │
│  关注对象的创建过程，解耦对象的创建和使用                │
├─────────────────────────────────────────────────────────┤
│  Singleton  │ Factory Method │ Abstract Factory       │
│  Builder    │ Prototype      │                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│              结构型模式 (Structural)                     │
│  关注类和对象的组合，构建更大的结构                      │
├─────────────────────────────────────────────────────────┤
│  Adapter   │ Decorator      │ Proxy   │ Facade         │
│  Bridge    │ Composite      │ Flyweight               │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│              行为型模式 (Behavioral)                     │
│  关注对象之间的通信和职责分配                            │
├─────────────────────────────────────────────────────────┤
│  Strategy  │ Observer       │ Template Method          │
│  Command   │ Chain of Resp. │ Iterator  │ Mediator     │
│  Memento   │ State         │ Visitor  │ Interpreter  │
└─────────────────────────────────────────────────────────┘
```

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行示例

```bash
# 运行所有设计模式示例
python main.py

# 运行特定设计模式
python singleton.py
python strategy.py
python observer.py

# 运行测试
python -m pytest test_patterns.py -v
```

## 📖 详细使用指南

### 1. 单例模式 (Singleton)

**意图：** 确保一个类只有一个实例，并提供一个全局访问点。

**应用场景：**
- 数据库连接池
- 配置管理器
- 日志记录器
- 线程池

```python
from singleton import Singleton

# 获取单例实例
instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)  # True

# 设置值
instance1.set_value("Hello")
print(instance2.get_value())  # "Hello"
```

### 2. 工厂方法模式 (Factory Method)

**意图：** 定义一个创建对象的接口，让子类决定实例化哪个类。

**应用场景：**
- 日志记录器
- 数据库连接
- 文档处理
- UI组件

```python
from factory_method import DocumentFactory

factory = DocumentFactory()

# 创建PDF文档
pdf_doc = factory.create_document("pdf")
print(pdf_doc.open())

# 创建Word文档
word_doc = factory.create_document("word")
print(word_doc.open())
```

### 3. 策略模式 (Strategy)

**意图：** 定义一系列算法，把它们封装起来，并使它们可以互换。

**应用场景：**
- 支付方式
- 排序算法
- 压缩算法
- 路径规划

```python
from strategy import PaymentContext, CreditCardPayment, PayPalPayment

context = PaymentContext(CreditCardPayment())
result = context.execute_payment(100)

context.set_strategy(PayPalPayment())
result = context.execute_payment(100)
```

### 4. 观察者模式 (Observer)

**意图：** 定义对象间的一对多依赖，当一个对象改变状态时，所有依赖者都会收到通知。

**应用场景：**
- 事件处理系统
- 消息队列
- 社交媒体订阅
- 股票价格监控

```python
from observer import YouTubeChannel, Subscriber

channel = YouTubeChannel("技术频道")
subscriber1 = Subscriber("用户1")
subscriber2 = Subscriber("用户2")

channel.attach(subscriber1)
channel.attach(subscriber2)

channel.upload_video("Python教程")
```

### 5. 适配器模式 (Adapter)

**意图：** 将一个类的接口转换成客户希望的另一个接口。

**应用场景：**
- 集成第三方库
- 接口转换
- 遗留代码兼容
- 不同系统间通信

```python
from adapter import MediaPlayer, VLCPlayer, MediaAdapter

player = MediaPlayer()
vlc_player = VLCPlayer()
adapter = MediaAdapter(vlc_player)

player.play("vlc", "movie.vlc")
```

### 6. 装饰器模式 (Decorator)

**意图：** 动态地给一个对象添加一些额外的职责。

**应用场景：**
- UI组件装饰
- 日志记录
- 缓存装饰
- 性能监控

```python
from decorator import SimpleCoffee, MilkDecorator, WhipDecorator

coffee = SimpleCoffee()
coffee = MilkDecorator(coffee)
coffee = WhipDecorator(coffee)

print(coffee.description())  # "简单咖啡, 牛奶, 奶泡"
print(coffee.cost())  # 15.0
```

## 🧪 测试

项目包含完整的单元测试，覆盖所有设计模式：

```bash
# 运行所有测试
python -m pytest test_patterns.py -v

# 运行特定模式测试
python -m pytest test_patterns.py::TestSingleton -v

# 查看测试覆盖率
python -m pytest test_patterns.py --cov=. --cov-report=html
```

测试覆盖：
- ✅ 创建型模式（5种）
- ✅ 结构型模式（7种）
- ✅ 行为型模式（11种）
- ✅ 线程安全测试
- ✅ 性能测试

## 📊 设计模式详解

### 创建型模式

#### 单例模式 (Singleton)

**实现方式：**
1. 懒汉式（延迟加载）
2. 饿汉式（立即加载）
3. 双重检查锁定
4. 元类实现

**线程安全：**
- 使用锁机制
- 使用模块级变量
- 使用元类

```python
class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

#### 工厂方法模式 (Factory Method)

**优点：**
- 符合开闭原则
- 符合单一职责原则
- 提高代码复用性

**缺点：**
- 类的数量增加
- 增加系统复杂性

```python
class DocumentFactory:
    def create_document(self, doc_type: str) -> Document:
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        else:
            raise ValueError(f"不支持的文档类型: {doc_type}")
```

### 结构型模式

#### 适配器模式 (Adapter)

**类型：**
1. 类适配器（多重继承）
2. 对象适配器（组合）

**应用：**
- 接口不兼容
- 遗留代码集成
- 第三方库集成

```python
class MediaAdapter(MediaPlayer):
    def __init__(self, advanced_player: AdvancedMediaPlayer):
        self.advanced_player = advanced_player
    
    def play(self, audio_type: str, filename: str) -> str:
        if audio_type == "vlc":
            return self.advanced_player.play_vlc(filename)
        elif audio_type == "mp4":
            return self.advanced_player.play_mp4(filename)
```

#### 装饰器模式 (Decorator)

**特点：**
- 比继承更灵活
- 动态添加功能
- 多个装饰器组合

**Python装饰器：**
```python
@decorator1
@decorator2
def function():
    pass
```

### 行为型模式

#### 策略模式 (Strategy)

**优点：**
- 算法可以自由切换
- 避免多重条件语句
- 扩展性好

**应用：**
- 支付方式
- 排序算法
- 路径规划

```python
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def execute_payment(self, amount: float) -> str:
        return self._strategy.pay(amount)
```

#### 观察者模式 (Observer)

**优点：**
- 支持广播通信
- 符合开闭原则
- 抽象耦合

**应用：**
- 事件系统
- 消息队列
- 社交媒体

```python
class YouTubeChannel(Subject):
    def __init__(self, name: str):
        self.name = name
        self._subscribers: List[Observer] = []
    
    def attach(self, observer: Observer):
        self._subscribers.append(observer)
    
    def notify(self, message: str):
        for subscriber in self._subscribers:
            subscriber.update(message)
```

## 🎯 实际应用场景

### 1. 数据库连接池（单例模式）

```python
class DatabaseConnectionPool(Singleton):
    def __init__(self):
        self.connections = []
        self.max_connections = 10
    
    def get_connection(self):
        if self.connections:
            return self.connections.pop()
        else:
            return self._create_connection()
    
    def release_connection(self, connection):
        if len(self.connections) < self.max_connections:
            self.connections.append(connection)
```

### 2. 支付系统（策略模式）

```python
class PaymentSystem:
    def __init__(self):
        self.strategies = {
            'credit_card': CreditCardPayment(),
            'paypal': PayPalPayment(),
            'wechat': WeChatPayment()
        }
    
    def pay(self, method: str, amount: float):
        strategy = self.strategies.get(method)
        if strategy:
            return strategy.pay(amount)
        else:
            raise ValueError(f"不支持的支付方式: {method}")
```

### 3. 日志系统（装饰器模式）

```python
class Logger:
    def log(self, message: str):
        print(message)

class TimestampDecorator(Logger):
    def __init__(self, logger: Logger):
        self._logger = logger
    
    def log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._logger.log(f"[{timestamp}] {message}")

class LevelDecorator(Logger):
    def __init__(self, logger: Logger, level: str):
        self._logger = logger
        self._level = level
    
    def log(self, message: str):
        self._logger.log(f"[{self._level}] {message}")
```

### 4. 事件系统（观察者模式）

```python
class EventManager(Subject):
    def __init__(self):
        self._listeners = defaultdict(list)
    
    def subscribe(self, event_type: str, listener: Observer):
        self._listeners[event_type].append(listener)
    
    def unsubscribe(self, event_type: str, listener: Observer):
        self._listeners[event_type].remove(listener)
    
    def notify(self, event_type: str, data: Any):
        for listener in self._listeners[event_type]:
            listener.update(data)
```

## 🔧 最佳实践

### 1. 选择合适的设计模式

```python
# 需求分析
def analyze_requirement(requirement):
    patterns = {
        'single_instance': 'Singleton',
        'object_creation': 'Factory Method',
        'interface_conversion': 'Adapter',
        'dynamic_behavior': 'Decorator',
        'algorithm_selection': 'Strategy',
        'event_notification': 'Observer'
    }
    
    for need, pattern in patterns.items():
        if need in requirement:
            return pattern
    
    return None
```

### 2. 组合使用设计模式

```python
# 单例 + 工厂方法
class SingletonFactory(Singleton):
    def create_product(self, product_type: str):
        pass

# 策略 + 工厂方法
class StrategyFactory:
    def create_strategy(self, strategy_type: str):
        pass

# 观察者 + 单例
class EventManager(Singleton, Subject):
    pass
```

### 3. 避免过度设计

```python
# 简单场景不需要设计模式
class SimpleCalculator:
    def add(self, a, b):
        return a + b

# 复杂场景才使用设计模式
class AdvancedCalculator:
    def __init__(self, strategy: CalculationStrategy):
        self._strategy = strategy
    
    def calculate(self, a, b):
        return self._strategy.calculate(a, b)
```

## 📁 项目结构

```
design-patterns/
├── creational/
│   ├── singleton.py          # 单例模式
│   ├── factory_method.py     # 工厂方法模式
│   ├── abstract_factory.py   # 抽象工厂模式
│   ├── builder.py            # 建造者模式
│   └── prototype.py          # 原型模式
├── structural/
│   ├── adapter.py            # 适配器模式
│   ├── decorator.py          # 装饰器模式
│   ├── proxy.py              # 代理模式
│   ├── facade.py             # 外观模式
│   ├── bridge.py             # 桥接模式
│   ├── composite.py         # 组合模式
│   └── flyweight.py          # 享元模式
├── behavioral/
│   ├── strategy.py           # 策略模式
│   ├── observer.py           # 观察者模式
│   ├── template_method.py    # 模板方法模式
│   ├── command.py            # 命令模式
│   ├── chain_of_responsibility.py # 责任链模式
│   ├── iterator.py           # 迭代器模式
│   ├── mediator.py           # 中介者模式
│   ├── memento.py            # 备忘录模式
│   ├── state.py              # 状态模式
│   ├── visitor.py            # 访问者模式
│   └── interpreter.py        # 解释器模式
├── tests/
│   └── test_patterns.py      # 单元测试
├── examples/
│   ├── database_pool.py      # 数据库连接池示例
│   ├── payment_system.py     # 支付系统示例
│   ├── logging_system.py     # 日志系统示例
│   └── event_system.py       # 事件系统示例
├── main.py                   # 主程序入口
└── requirements.txt           # 依赖列表
```

## 🎓 技术亮点

### 1. 完整的设计模式实现

- **23种经典设计模式** - GoF设计模式完整实现
- **Python特性** - 利用Python语言特性实现
- **类型注解** - 提高代码可读性
- **文档注释** - 详细的代码说明

### 2. 实际应用示例

- **数据库连接池** - 单例模式应用
- **支付系统** - 策略模式应用
- **日志系统** - 装饰器模式应用
- **事件系统** - 观察者模式应用

### 3. 最佳实践指导

- **模式选择指南** - 如何选择合适的设计模式
- **组合使用** - 多个设计模式的组合
- **避免过度设计** - 何时使用设计模式

## 🔮 未来计划

- [ ] 更多设计模式变种
- [ ] 设计模式对比分析
- [ ] 性能基准测试
- [ ] 代码生成器
- [ ] 设计模式检测工具
- [ ] 设计模式推荐系统
- [ ] 多语言实现
- [ ] 在线交互式教程

## 🤝 贡献指南

欢迎贡献代码、报告问题或提出建议！

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

感谢以下资源：
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns)
- [Refactoring Guru](https://refactoring.guru/design-patterns)
- [Python Design Patterns](https://python-patterns.guide/)

## 📞 联系方式

- 项目主页: https://github.com/yourusername/design-patterns
- 问题反馈: https://github.com/yourusername/design-patterns/issues
- 邮箱: your.email@example.com

---

⭐ 如果这个项目对你有帮助，请给个Star！
