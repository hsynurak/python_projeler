from random import randint

def carpim(x,y,r):
    dogru = 0
    yanlis = 0
    result = str(x*y)
    if result == r:
        dogru += 1
        print("\t\t Cevap Doğru \n Karne: %s doğru, %s yanlış" %(dogru, yanlis))
    else:
        yanlis += 1
        print("\t\t Cevap Yanlış, doğru cevap %s olacak. \n Karne: %s doğru, %s yanlış" %(result, dogru, yanlis))
        

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