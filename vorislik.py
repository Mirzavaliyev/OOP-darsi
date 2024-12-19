# class Animal:
#     def __init__(self,nomi):
#         self.nomi = nomi
#     def speak(self):
#         return f"{self.nomi} ovoz chiqarmoqda"
# class Dog(Animal):
#     def speak(self):
#         return f"{self.nomi} vovilamoqda"
# animal1 = Animal('qandaydir hayvon')
# print(animal1.speak())
# animal2 = Dog('It')
# print(animal2.speak())
# class Cat(Animal):
#     def speak(self):
#         return f"{self.nomi} miyovlayapti"
# animal3 = Cat('Mushuk')
# print(animal3.speak())
# class Bird(Animal):
#     def __init__(self,name,can_fly):
#         super().__init__(name)
#         self.can_fly = can_fly
#     def speak(self):
#         if self.can_fly:
#             return f"{self.nomi} ucha oladi"
#         else:
#             return f"{self.nomi} ucha olmaydi "
# animal4 = Bird('Qaldirgoch',False)
# print(animal4.speak())
# class Author:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class Book(Author):
#     def __init__(self,title,genre,author):
#         self.title = title
#         self.genre = genre
#         self.author.name
#     def info(self):
#         return (f"Kitob nomi: {self.title}"
#                 f"Kitob janri: {self.genre}"
#                 f"Kitob muallifi: {self.author}")
# author1 = Author("Alisher Navoiy", 69)
# kitob1 = Book('Hamza','Romance', author1)
# # print(kitob1)
# class Brand:
#     def __init__(self,name,country):
#         self.name = name
#         self.country = country
# class Phone:
#     def __init__(self,model,price,brand):
#         self.model = model
#         self.price = price
#         self.brand = brand
#     def info(self):
#         return (f"Model: {self.model}"
#                 f"\nPrice: {self.price}"
#                 f"\nBrand {self.brand.name}"
#                 f"Brand country: {self.brand.country}")
# brand1 = Brand('Samsung', 'Northern Korea')
# phone1 = Phone('S21 ultra',2000,brand1)
# print(phone1.info())




