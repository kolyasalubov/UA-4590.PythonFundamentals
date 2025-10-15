class Human():
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}!"
    
    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def message():
        return "Random message"