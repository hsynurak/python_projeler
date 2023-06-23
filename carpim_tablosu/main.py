from random import randint

"""
fonksiyonda girilen x ve y değerlerinin çarpımının sonucunun r değerine eşit olup olmadığını kontrol eder.
r değerine eşit ise doğru mesajını verir
eğer eşit değilse yanlış mesajı verir ve doğrusunu gösterir.
"""
def carpim(x,y,r):
    result = str(x*y)
    if result == r:
        print("\t\t Cevap Doğru ")
    else:
        print("\t\t Cevap Yanlış, doğru cevap %s olacak. " )
        

"""
fonksiyonda basla() fonksiyonu içerisinde seviye seçimi yapıldıktan sonra seçilen seviyeye göre random sayılar üretilir.
bu random sayılar ile üretilen işlemlere cevap sorulur.
seçilen seviyelerin her biri için 10 adet işlem sorulur. 10 işlem cevaplandıktan sonra tekrar seviye seçimi yapılmasına olanak sağlanır.
"""
def basla(range1, range2):
    for i in range(0,5):
        for j in range(0,5):
            num1 = randint(range1, range2)
            num2 = randint(range1, range2)
            print("%s*%s işleminin sonucu nedir?" %(num1, num2))
            sonuc = input("Sonuc: ")
            carpim(num1, num2, sonuc)
            if i==1 and j==4:
                print("\n\n Bu seviyede yeterince örnek gördünüz. Başka bir seviye seçebilirsiniz :) \n\n")
                seviye()
                
            
"""
Bu fonksiyon ile seviye seçilmesi istenir.
Bu seviyeye göre basla() fonksiyonu uygun parametreler ile çağırılır.
"""           
def seviye():
    print("Seviye Seçiniz")
    print("Kolay seviye için 1")
    print("Orta seviye için 2")
    print("Zor seviye için 3")
    print("Çok zor seviye için 4")

    seviye = input("\t\t Seviye: ")
    
    if seviye == "1":
        basla(1,6)
    elif seviye == "2":
        basla(6,11)
    elif seviye == "3":
        basla(11,26)
    elif seviye == "4":
        basla(26,51)
    else:
        print("Hatalı seviye seçimi yaptınız. Lütfen tekrar deneyiniz.")
        seviye()    
        
        
        
seviye()