import random

number = random.randint(1, 10)
word = random.randint(97,122)
generate = random.randint(0, 1)

class CodeGenerator:
    def __init__(self):
        # Случаен избор: 0 = текст, 1 = число
        choice =  generate

        if choice == 0:
            self.data =  number  # текст
        
        else:
            self.data = word  # произволно цяло число
        

    def show(self):
        print("Стойността е:", self.data)
        print("Типът е:", type(self.data).__name__)
