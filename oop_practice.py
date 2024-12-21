# class Talaba:
#     def __init__(self,ismi,yoshi):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.fanlar = []
#     def fan_qosh(self,fan):
#         self.fanlar.append(fan)
#     def info(self):
#         return (f"Talaba ismi {self.ismi}"
#                 f"Talaba yoshi {self.yoshi}"
#                 f" O'qiydigan fanlari {', '.join(self.fanlar) if self.fanlar else 'yoq'}")
# talaba1 = Talaba('Shavkatjon Mirzavaliyev ', 26)
# talaba1.fan_qosh('Matematika')
# talaba1.fan_qosh("Fizika")
# print(talaba1.info())
# class Fan:
#     def __init__(self,nomi,soatlar_soni):
#         self.nomi = nomi
#         self.soatlar_soni = soatlar_soni
#     def info(self):
#         return (f"Fanning nomi: {self.nomi}"
#                 f"\nFanning Soatlar soni: {self.soatlar_soni}")
# fan1 = Fan('Fizika', 30)
# fan2 = Fan('Tarix', 45)
# fan3 = Fan('Ingliz tili', 80)
# print(fan1.info())
# print(fan2.info(), fan3.info())
# class Talaba:
#     def __init__(self,ismi,familyasi,fani):
#         self.ismi = ismi
#         self.familyasi = familyasi
#         self.fani = fani
#     def info(self):
#         return (f"Talaba ismi: {self.ismi}"
#                 f"\nTalanba familyasi: {self.familyasi}"
#                 f"\nO'qiydigan fani: {self.fani.nomi}"
#                 f"\nFanning soatlari: {self.fani.soatlar_soni}")
# fan1 = Fan('Fizika',300)
# talaba1 = Talaba('Shaxnoz','Valiyeva', fan1)
# print(talaba1.info())
# class BankXisobi():
#     def __init__(self,hisob_raqam,balans):
#         self.__hisob_raqam = hisob_raqam
#         self.__balans = balans
#     def balans_olish(self):
#         return (f"Sizning hisobingiz {self.__balans}")
#     def balans_qosh(self,miqdor):
#         if miqdor > 0:
#             self.__balans += miqdor
#         else:
#             print("0 dan katta raqam kiriting")
#     def yechib_ol(self,miqdor1):
#         if self.__balans > miqdor1:
#             self.__balans -= miqdor1
#         else:
#             print('Balansda buncha miqdorda pul yoq')
#     def info(self):
#         return (f"Hisob raqam {self.__hisob_raqam}"
#                 f"\nBalans {self.__balans}")
# hisob = BankXisobi("987654321", 100000)
#
# # Balansni olish
# print(hisob.balans_olish())  # 100000
#
# # Depozit kiritish
# hisob.balans_qosh(50000)
# print(hisob.balans_olish())  # 150000
#
# # Hisobdan pul yechish
# hisob.yechib_ol(200000)  # Xato: Balans yetarli emas
# hisob.yechib_ol(30000)
# print(hisob.balans_olish())  # 120000
#
# # Hisob ma'lumotlarini chiqarish
# print(hisob.info())
# class Talaba:
#     def __init__(self,ismi,yoshi,kursi=1):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.kursi = kursi
#     def info(self):
#         return (f"Talabaning ismi {self.ismi}"
#                 f"\nTalabaning yoshi {self.yoshi}"
#                 f"\nTalabaning kursi {self.kursi}")
#     def kurs_oshir(self,bosqich):
#         if 1 <= self.kursi < 4:
#             self.kursi += 1
#         else:
#             print('Talaba allaqchon 4-kursda')
#     def kurs_belgilash(self,belgila):
#         if belgila in [1,2,3,4]:
#             self.kursi += belgila
#         else:
#             print("Siz 1 dan 4 gacha raqam kirita olasiz")
# # Talaba obyektini yaratamiz
# talaba1 = Talaba("Shavkatjon", 20)
#
# # Ma'lumotlarni chop qilish
# print(talaba1.info())
#
#
#
# # Notog‘ri kursni belgilang
# talaba1.kurs_belgilash(5)  # Xato chiqadi
#
# # To‘g‘ri kursni belgilang
# talaba1.kurs_belgilash(3)
# # print(talaba1.info())
# class Doira:
#     doira_soni = 0
#     def __init__(self,radius):
#         self.radius = radius
#         Doira.doira_soni += 1
#     def diametr(self):
#         return self.radius * 2
#     @classmethod
#     def yangi_doira(cls,diametr):
#         return cls(diametr / 2)
#     @staticmethod
#     def yuzasi(radius):
#         import math
#         math.pi*radius**2
#
# doira = Doira(200)
# print(doira.diametr())
# doira2 = Doira.yangi_doira(400)
# # print(f"Doiraning radiusi {doira2.radius}")
# class Hayvon:
#     hayvonlar_soni = 0
#     def __init__(self,ism,yoshi,turi):
#         self.ism = ism
#         self.yoshi = yoshi
#         self.turi = turi
#     def info(self):
#         return (f"Hayvon ism {self.ism}"
#                 f"Hayvon yoshi {self.yoshi}"
#                 f"Hayvon turi {self.turi}")
#     def ovqatlan(self):
#         return (f"{self.ism} ovqatlanyapti")
# hayvon1 = Hayvon('Sara',5,'Mushuk')
# print(hayvon1.ovqatlan())
class Book:
    def __init__(self,nomi,mualifi):
        self.nomi = nomi
        self.mualifi = mualifi
    def __str__(self):
         return (f"{self.nomi} by {self.mualifi}")
p = Book('Hamza', "Alisher Navoiy")
print(p)







