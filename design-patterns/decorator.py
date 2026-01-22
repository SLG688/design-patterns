from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass

class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 10.0
    
    def description(self) -> str:
        return "简单咖啡"

class CoffeeDecorator(Coffee, ABC):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    @abstractmethod
    def cost(self) -> float:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass

class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 2.0
    
    def description(self) -> str:
        return f"{self._coffee.description()}, 牛奶"

class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.0
    
    def description(self) -> str:
        return f"{self._coffee.description()}, 糖"

class WhipDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 3.0
    
    def description(self) -> str:
        return f"{self._coffee.description()}, 奶泡"

class VanillaDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.5
    
    def description(self) -> str:
        return f"{self._coffee.description()}, 香草"

def decorator_demo():
    print("=" * 50)
    print("装饰器模式 (Decorator Pattern)")
    print("=" * 50)
    
    print("\n简单咖啡:")
    coffee = SimpleCoffee()
    print(f"描述: {coffee.description()}")
    print(f"价格: ¥{coffee.cost()}")
    
    print("\n加牛奶:")
    coffee = MilkDecorator(coffee)
    print(f"描述: {coffee.description()}")
    print(f"价格: ¥{coffee.cost()}")
    
    print("\n再加糖:")
    coffee = SugarDecorator(coffee)
    print(f"描述: {coffee.description()}")
    print(f"价格: ¥{coffee.cost()}")
    
    print("\n再加奶泡:")
    coffee = WhipDecorator(coffee)
    print(f"描述: {coffee.description()}")
    print(f"价格: ¥{coffee.cost()}")
    
    print("\n再加香草:")
    coffee = VanillaDecorator(coffee)
    print(f"描述: {coffee.description()}")
    print(f"价格: ¥{coffee.cost()}")
    
    print("\n应用场景:")
    print("- 动态添加功能")
    print("- UI组件装饰")
    print("- 日志记录")
    print("- 缓存装饰")
    print("- 性能监控")

if __name__ == "__main__":
    decorator_demo()
