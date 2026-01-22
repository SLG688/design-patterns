import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.value = 0
            self._initialized = True

def singleton_demo():
    print("=" * 50)
    print("单例模式 (Singleton Pattern)")
    print("=" * 50)
    
    instance1 = Singleton()
    instance1.value = 10
    
    instance2 = Singleton()
    instance2.value = 20
    
    print(f"Instance 1 value: {instance1.value}")
    print(f"Instance 2 value: {instance2.value}")
    print(f"Same instance? {instance1 is instance2}")
    
    print("\n应用场景:")
    print("- 日志记录器")
    print("- 配置管理器")
    print("- 数据库连接池")
    print("- 缓存系统")

if __name__ == "__main__":
    singleton_demo()
