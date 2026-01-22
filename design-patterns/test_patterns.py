import unittest
from abc import ABC, abstractmethod
from typing import List
import threading

class TestSingleton(unittest.TestCase):
    def test_single_instance(self):
        from singleton import Singleton
        
        instance1 = Singleton()
        instance2 = Singleton()
        
        self.assertIs(instance1, instance2)
    
    def test_thread_safety(self):
        from singleton import Singleton
        
        instances = []
        
        def create_instance():
            instances.append(Singleton())
        
        threads = []
        for _ in range(10):
            t = threading.Thread(target=create_instance)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        first_instance = instances[0]
        for instance in instances[1:]:
            self.assertIs(instance, first_instance)

class TestStrategy(unittest.TestCase):
    def test_strategy_execution(self):
        from strategy import PaymentContext, CreditCardPayment, PayPalPayment
        
        context = PaymentContext(CreditCardPayment())
        result1 = context.execute_payment(100)
        self.assertIn("信用卡", result1)
        
        context.set_strategy(PayPalPayment())
        result2 = context.execute_payment(100)
        self.assertIn("PayPal", result2)
    
    def test_runtime_strategy_change(self):
        from strategy import PaymentContext, CreditCardPayment, WeChatPayment
        
        context = PaymentContext(CreditCardPayment())
        result1 = context.execute_payment(50)
        
        context.set_strategy(WeChatPayment())
        result2 = context.execute_payment(50)
        
        self.assertNotEqual(result1, result2)

class TestObserver(unittest.TestCase):
    def test_observer_notification(self):
        from observer import YouTubeChannel, Subscriber
        
        channel = YouTubeChannel("测试频道")
        subscriber1 = Subscriber("用户1")
        subscriber2 = Subscriber("用户2")
        
        channel.attach(subscriber1)
        channel.attach(subscriber2)
        
        channel.upload_video("测试视频")
        
        self.assertEqual(len(channel._subscribers), 2)
    
    def test_observer_detach(self):
        from observer import YouTubeChannel, Subscriber
        
        channel = YouTubeChannel("测试频道")
        subscriber = Subscriber("测试用户")
        
        channel.attach(subscriber)
        self.assertEqual(len(channel._subscribers), 1)
        
        channel.detach(subscriber)
        self.assertEqual(len(channel._subscribers), 0)

class TestFactoryMethod(unittest.TestCase):
    def test_factory_creation(self):
        from factory_method import DocumentFactory, PDFDocument, WordDocument
        
        factory = DocumentFactory()
        
        pdf_doc = factory.create_document("pdf")
        self.assertIsInstance(pdf_doc, PDFDocument)
        
        word_doc = factory.create_document("word")
        self.assertIsInstance(word_doc, WordDocument)
    
    def test_factory_extension(self):
        from factory_method import DocumentFactory
        
        class ExcelDocument:
            def open(self):
                return "打开Excel文档"
        
        factory = DocumentFactory()
        factory.register_document("excel", ExcelDocument)
        
        excel_doc = factory.create_document("excel")
        self.assertEqual(excel_doc.open(), "打开Excel文档")

class TestAdapter(unittest.TestCase):
    def test_adapter_compatibility(self):
        from adapter import MediaPlayer, AudioPlayer, MediaAdapter
        
        player = MediaPlayer()
        
        audio_player = AudioPlayer()
        result1 = player.play("mp3", "song.mp3")
        self.assertIn("播放MP3", result1)
        
        adapter = MediaAdapter()
        result2 = player.play("mp4", "video.mp4")
        self.assertIn("播放MP4", result2)

class TestDecorator(unittest.TestCase):
    def test_decorator_functionality(self):
        from decorator import SimpleCoffee, MilkDecorator, WhipDecorator
        
        coffee = SimpleCoffee()
        self.assertEqual(coffee.cost(), 10)
        self.assertEqual(coffee.description(), "简单咖啡")
        
        coffee = MilkDecorator(coffee)
        self.assertEqual(coffee.cost(), 12)
        self.assertEqual(coffee.description(), "简单咖啡, 牛奶")
        
        coffee = WhipDecorator(coffee)
        self.assertEqual(coffee.cost(), 15)
        self.assertEqual(coffee.description(), "简单咖啡, 牛奶, 奶泡")

if __name__ == '__main__':
    unittest.main()
