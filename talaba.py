# class Talaba:
#     """Talaba haqidagi malumot"""
#     def __init__(self,ism,familiya,t_yil):
#         self.ism = ism
#         self.familiya = familiya
#         self.t_yil = t_yil
#     def tanishtir(self):
#         print(f"Salom men {self.ism} {self.familiya} {self.t_yil} - yilda tug'ilganman")
#     def ismayt(self):
#         print(self.ism)
#         return self.ism
#
# talaba4 = Talaba("Hasan","Akbarov",2004)
# talaba4.tanishtir()
# talaba4.ismayt()
# class User:
#     def __init__(self,name,surname,email,phone):
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.phone = phone
#     def all_info(self):
#         print(f"Name: {self.name} \nSurname: {self.surname}")
#         print(f"Email: {self.email} \nPhone: {self.phone}")
#     def name_uz(self):
#         return self.name
# user1 = User('Shavkatjon','Mirzavaliyev','shavkatziyo@mail.com',934954500)
# user1.all_info()
# user1.name_uz()
# class Avto:
#     def __init__(self,type,color,cost,condition):
#
#         self.type = type
#         self.color = color
#         self.cost = cost
#         self.condition = condition
#         self.kilometr = 0
#     def avto_info(self):
#         return (f'Model: {self.type} '
#                 f'\nColor: {self.color} '
#                 f'\nCost: {self.cost} '
#                 f'\nCondition: {self.condition}'
#                 f'\nKilometr: {self.kilometr}')
#     def update_km(self,km):
#         if self.kilometr <= km:
#             self.kilometr = km
#         else:
#             print("Kilometr avalgisidan kichik bo'lishi mumkin emas")
#     def add_km(self,km):
#         if km > 0:
#             self.kilometr += km
#         else:
#             print("Kilometr manfiy son bo'la olmaydi")
#
#
# avto1 = Avto('Lombargini','red',2000,'old')
# avto1.update_km(5000)
# print(avto1.avto_info())
# avto1.add_km(4000)
# # print(avto1.avto_info())
# class Avtosalon:
#     def __init__(self,nomi,manzili,s_avto,turi):
#         self.nomi = nomi
#         self.manzili = manzili
#         self.s_avto = s_avto
#         self.turi = 'Samalyotlar'
#     def avtosalon_info(self ):
#         return (f"Nomi: {self.nomi}"
#             f"\nManzili: {self.manzili}"
#             f"\nSavdodagi avtomabil {s elf.s_avto}"
#                 f"\nAvtomobillar: {self.turi}")
#     def add_avto(self,turi):
#         self.turi = turi
# avto2 = Avtosalon('Shevrolet','Dostlikda','Damas,nexia','Yaxshi')
# avto2.add_avto('Samalyot')
# print(avto2.avtosalon_info())
# class Hona:
# #     def __init__(self,hajm,rangi,sigimi):
# #         self.hajm = hajm
# #         self.rangi = rangi
# #         self.sigimi = sigimi
# #     def hona_info(self):
# #         return (f"Honani hajmi: {self.hajm}"
# #                 f"\nHonani rangi: {self.rangi}"
# #                 f"\nHonani sigimi: {self.sigimi}")
# # class Uy:
# #     def __init__(self,hona):
# #         self.hona = hona
# #     def uy_info(self):
# #         return self.hona.hona_info()
# # hona1 = Hona('140kv','qizil','13 ta')
# # uy1 = Uy(hona1)
# # print(uy1.uy_info())
class Kitob:
    def __init__(self,nomi,muallifi,narxi):
        self.nomi = nomi
        self.muallifi = muallifi
        self.narxi = narxi
    def kitob_info(self):
        return (f"Kitob nomi: {self.nomi}"
                f"Kitob muallifi: {self.muallifi}"
                f"Kitob narxi: {self.narxi}")
class Kutubxona:
    def __init__(self,nom):
        self.nom = nom
        self.kitoblar = []
    def kitob_qoshish(self,kitob):
        """Bu yerda kitob qoshamiz"""
        self.kitoblar.append(kitob)
    def kutubxona_info(self):
        """Bu yerda kutubxona malumotlari"""
        info = "Kitob xaqidagi malumotlar"
        for kitob in self.kitoblar:
            info += kitob.kitob_info() + "\n"
        return info
# Kitob obyektlari yaratish
kitob1 = Kitob('Hamza', 'Alisher Navoiy', '300 ming')
kitob2 = Kitob('O‘tkan kunlar', 'Abdulla Qodiriy', '400 ming')
kitob3 = Kitob('Javohirlar xazinasi', 'Zahiriddin Muhammad Bobur', '500 ming')
kutubxona1 = Kutubxona('Shaxrisabz kutubxonasi')
kutubxona1.kitob_qoshish(kitob1)
kutubxona1.kitob_qoshish(kitob2)
kutubxona1.kitob_qoshish(kitob3)
print(kutubxona1.kutubxona_info())


