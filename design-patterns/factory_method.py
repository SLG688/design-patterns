from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def save(self, content: str):
        pass

class PDFDocument(Document):
    def open(self):
        return "打开PDF文档"
    
    def save(self, content: str):
        return f"保存内容到PDF: {content}"

class WordDocument(Document):
    def open(self):
        return "打开Word文档"
    
    def save(self, content: str):
        return f"保存内容到Word: {content}"

class ExcelDocument(Document):
    def open(self):
        return "打开Excel文档"
    
    def save(self, content: str):
        return f"保存内容到Excel: {content}"

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self, doc_type: str) -> Document:
        pass

class SimpleDocumentFactory(DocumentFactory):
    def create_document(self, doc_type: str) -> Document:
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        elif doc_type == "excel":
            return ExcelDocument()
        else:
            raise ValueError(f"不支持的文档类型: {doc_type}")

class AdvancedDocumentFactory(DocumentFactory):
    def __init__(self):
        self._creators = {}
        self._register_default_creators()
    
    def _register_default_creators(self):
        self.register_document("pdf", PDFDocument)
        self.register_document("word", WordDocument)
        self.register_document("excel", ExcelDocument)
    
    def register_document(self, doc_type: str, creator_class):
        self._creators[doc_type] = creator_class
    
    def create_document(self, doc_type: str) -> Document:
        creator_class = self._creators.get(doc_type)
        if creator_class:
            return creator_class()
        raise ValueError(f"不支持的文档类型: {doc_type}")

def factory_method_demo():
    print("=" * 50)
    print("工厂方法模式 (Factory Method Pattern)")
    print("=" * 50)
    
    factory = SimpleDocumentFactory()
    
    print("\n创建PDF文档:")
    pdf_doc = factory.create_document("pdf")
    print(pdf_doc.open())
    print(pdf_doc.save("这是PDF内容"))
    
    print("\n创建Word文档:")
    word_doc = factory.create_document("word")
    print(word_doc.open())
    print(word_doc.save("这是Word内容"))
    
    print("\n高级工厂（支持动态注册）:")
    advanced_factory = AdvancedDocumentFactory()
    
    class PowerPointDocument(Document):
        def open(self):
            return "打开PowerPoint文档"
        
        def save(self, content: str):
            return f"保存内容到PowerPoint: {content}"
    
    advanced_factory.register_document("ppt", PowerPointDocument)
    
    ppt_doc = advanced_factory.create_document("ppt")
    print(ppt_doc.open())
    print(ppt_doc.save("这是PPT内容"))
    
    print("\n应用场景:")
    print("- 文档处理系统")
    print("- 数据库连接创建")
    print("- 日志记录器创建")
    print("- UI组件创建")

if __name__ == "__main__":
    factory_method_demo()
