class Animal:
    def __init__(self,nomi):
        self.nomi = nomi
    def speak(self):
        return f"{self.nomi} ovoz chiqarmoqda"
class Dog(Animal):
    def speak(self):
        return f"{self.nomi} vovilamoqda"
animal1 = Animal('qandaydir hayvon')
print(animal1.speak())
animal2 = Dog('It')
print(animal2.speak())
class Cat(Animal):
    def speak(self):
        return f"{self.nomi} miyovlayapti"
animal3 = Cat('Mushuk')
print(animal3.speak())
class Bird(Animal):
    def __init__(self,name,can_fly):
        super().__init__(name)
        self.can_fly = can_fly
    def speak(self):
        if self.can_fly:
            return f"{self.nomi} ucha oladi"
        else:
            return f"{self.nomi} ucha olmaydi "
animal4 = Bird('Qaldirgoch',False)
print(animal4.speak())