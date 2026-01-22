from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"支付 ${amount:.2f} - 信用卡")
        return f"信用卡支付成功: ${amount:.2f}"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"支付 ${amount:.2f} - PayPal")
        return f"PayPal支付成功: ${amount:.2f}"

class WeChatPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"支付 ${amount:.2f} - 微信支付")
        return f"微信支付成功: ${amount:.2f}"

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def execute_payment(self, amount: float):
        return self._strategy.pay(amount)

def strategy_demo():
    print("=" * 50)
    print("策略模式 (Strategy Pattern)")
    print("=" * 50)
    
    context = PaymentContext(CreditCardPayment())
    
    amount = 100.50
    
    print("\n使用信用卡支付:")
    result = context.execute_payment(amount)
    print(result)
    
    print("\n切换到PayPal支付:")
    context.set_strategy(PayPalPayment())
    result = context.execute_payment(amount)
    print(result)
    
    print("\n切换到微信支付:")
    context.set_strategy(WeChatPayment())
    result = context.execute_payment(amount)
    print(result)
    
    print("\n应用场景:")
    print("- 支付系统")
    print("- 排序算法")
    print("- 数据压缩")
    print("- 路径规划")

if __name__ == "__main__":
    strategy_demo()
