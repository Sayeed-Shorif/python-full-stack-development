class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} eats regularly"
    def intro(self):
        return f"Name : {self.name} and age : {self.age}"
    
Sayeed =  Human('sayeed', 43)

print(Sayeed.eat())
print(Sayeed.intro())