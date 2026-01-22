from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify(self, message: str):
        pass

class YouTubeChannel(Subject):
    def __init__(self, name: str):
        self.name = name
        self._subscribers: List[Observer] = []
    
    def attach(self, observer: Observer):
        if observer not in self._subscribers:
            self._subscribers.append(observer)
            print(f"{observer.name} 订阅了 {self.name}")
    
    def detach(self, observer: Observer):
        if observer in self._subscribers:
            self._subscribers.remove(observer)
            print(f"{observer.name} 取消订阅 {self.name}")
    
    def notify(self, message: str):
        print(f"\n{self.name} 发布新视频: {message}")
        for observer in self._subscribers:
            observer.update(message)
    
    def upload_video(self, title: str):
        self.notify(title)

class Subscriber(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, message: str):
        print(f"  -> {self.name} 收到通知: {message}")

def observer_demo():
    print("=" * 50)
    print("观察者模式 (Observer Pattern)")
    print("=" * 50)
    
    channel = YouTubeChannel("技术频道")
    
    subscriber1 = Subscriber("小明")
    subscriber2 = Subscriber("小红")
    subscriber3 = Subscriber("小刚")
    
    channel.attach(subscriber1)
    channel.attach(subscriber2)
    channel.attach(subscriber3)
    
    channel.upload_video("Python教程第1集")
    
    print("\n小红取消订阅...")
    channel.detach(subscriber2)
    
    channel.upload_video("Python教程第2集")
    
    print("\n应用场景:")
    print("- 事件处理系统")
    print("- GUI框架")
    print("- 消息订阅系统")
    print("- 社交媒体动态")

if __name__ == "__main__":
    observer_demo()
