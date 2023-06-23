sayilar = []
ekle = True

"""
ekle isimli değişken True olduğu sürece kullanıcıdan sayı girişi istenir.
verilen sayı -1 ise sayı girişi bitirilir.
girilen değerlerin türlerinde olauşabilcek sıkıntılar için try except bloğu kullanıldı.
"""
while ekle:
     try:
          print("Lütfen kıyaslama yapılacak sayıları giriniz. Sayı girişini bitirmek için -1 basınız.")
          a = int(input())
          if a == -1:
               ekle = False
          else:
               sayilar.append(a)
     except SyntaxError:
          print("Lütfen sayı giriniz.")
     except ValueError:
          print("Lütfen sayı giriniz.") 
                                   
"""
Burada kullanılan try-except-finally bloğu ile değer girilip girilmediği kontrol edilir.
Eğer değer girilirse sayilar[0] indexi bir değer olacaktır ve hata verilmeyecektir.
"""              
try:
     enbuyuk = sayilar[0]
     enkucuk = sayilar[0]
     ortalama = sayilar[0]
except:
     print("Lütfen kiyaslama yapılabilmesi için sayi giriniz")                                  
finally:
     toplam = 0

"""
sayilar listesi içinde bulunan değerler tek tek kontrol edilir.
En büyük ve en küçük değerler bulunur.
"""
for sayi in sayilar:
     if sayi > enbuyuk:
          enbuyuk = sayi
     if sayi < enkucuk:
          enkucuk = sayi
     toplam += sayi

ortalama = toplam / len(sayilar)

print("\nEn büyük sayı: %s \nEn küçük sayı: %s \nOrtalama: %s" %(enbuyuk,enkucuk,ortalama))
           