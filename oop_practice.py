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
class BankXisobi():
    def __init__(self,hisob_raqam,balans):
        self.__hisob_raqam = hisob_raqam
        self.__balans = balans
    def balans_olish(self):
        return (f"Sizning hisobingiz {self.__balans}")
    def balans_qosh(self,miqdor):
        if miqdor > 0:
            self.__balans += miqdor
        else:
            print("0 dan katta raqam kiriting")
    def yechib_ol(self,miqdor1):
        if self.__balans > miqdor1:
            self.__balans -= miqdor1
        else:
            print('Balansda buncha miqdorda pul yoq')
    def info(self):
        return (f"Hisob raqam {self.__hisob_raqam}"
                f"\nBalans {self.__balans}")
hisob = BankXisobi("987654321", 100000)

# Balansni olish
print(hisob.balans_olish())  # 100000

# Depozit kiritish
hisob.balans_qosh(50000)
print(hisob.balans_olish())  # 150000

# Hisobdan pul yechish
hisob.yechib_ol(200000)  # Xato: Balans yetarli emas
hisob.yechib_ol(30000)
print(hisob.balans_olish())  # 120000

# Hisob ma'lumotlarini chiqarish
print(hisob.info())








