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
class Fan:
    def __init__(self,nomi,soatlar_soni):
        self.nomi = nomi
        self.soatlar_soni = soatlar_soni
    def info(self):
        return (f"Fanning nomi: {self.nomi}"
                f"\nFanning Soatlar soni: {self.soatlar_soni}")
fan1 = Fan('Fizika', 30)
fan2 = Fan('Tarix', 45)
fan3 = Fan('Ingliz tili', 80)
print(fan1.info())
print(fan2.info(), fan3.info())
class Talaba:
    def __init__(self,ismi,familyasi,fani):
        self.ismi = ismi
        self.familyasi = familyasi
        self.fani = fani
    def info(self):
        return (f"Talaba ismi: {self.ismi}"
                f"\nTalanba familyasi: {self.familyasi}"
                f"\nO'qiydigan fani: {self.fani.nomi}"
                f"\nFanning soatlari: {self.fani.soatlar_soni}")
fan1 = Fan('Fizika',300)
talaba1 = Talaba('Shaxnoz','Valiyeva', fan1)
print(talaba1.info())






