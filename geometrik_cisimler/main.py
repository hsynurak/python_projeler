

def kare(kk):
     yuzeyalanı = kk*kk
     print("Karenin yüzey alanı: %s" %yuzeyalanı)

def dikdortgen(kk,uk):
     yuzeyalanı = kk*uk
     print("Dikdörtgenin yüzey alanı: %s" %yuzeyalanı)
     
def daire(yç):
     yuzeyalanı = 3.14*yç*yç
     print("Dairenin yüzey alanı: %s" %yuzeyalanı)

def yamuk(ak,uk,h):
     yuzeyalanı = (ak+uk)/2*h
     print("Yamuğun yüzey alanı: %s" %yuzeyalanı)

def ucgen(dt,h):
     yuzeyalanı = dt*h/2
     print("Üçgenin yüzey alanı: %s" %yuzeyalanı) 

def paralelkenar(ak,h):
     yuzeyalanı = ak*h
     print("Paralelkenarın yüzey alanı: %s" %yuzeyalanı)

def eskenardortgen(ak,h):
     yuzeyalanı = ak*h
     print("Eşkenar dörtgenin yüzey alanı: %s" %yuzeyalanı)
     
def kup(kk):
     hacim = kk*kk*kk
     print("Küpün hacmi: %s" %hacim)    

def silindir(yç, h):
     hacim  = daire(yç)*h
     print("Silindirin hacmi: %s" %hacim)

def kure(yç):
     hacim = 4/3*3.14*yç*yç*yç

def ucgenprizma(dt,y,h):
     hacim = ucgen(dt,y)*h

def dikdortgenprizma(kk,uk,h):
     hacim = dikdortgen(kk,uk)*h
     

print("Geometrik cisimlerin yüzey alanı ve hacim hesaplamaları için lütfen aşağıdaki seçeneklerden birini seçiniz. (Çıkmak için -1) \n\nKare ==> 1 \nDikdörtgen ==> 2 \nDaire ==> 3 \nYamuk ==> 4 \nÜçgen ==> 5 \nParalelkenar ==> 6 \nEşkenar dörtgen ==> 7 \nKüp ==> 8 \nSilindir ==> 9 \nKüre ==> 10 \nÜçgen prizma ==> 11 \nDikdörtgen prizma ==> 12 ")


test = True
while test:
     secim = int(input("Seçiminiz: "))
     if secim == -1:
          test = False
     else:
          if secim == 1:
               kk = int(input("Karenin kenar uzunluğunu giriniz: "))
               kare(kk)
          elif secim == 2:
               kk = int(input("Dikdörtgenin kısa kenar uzunluğunu giriniz: "))
               uk = int(input("Dikdörtgenin uzun kenar uzunluğunu giriniz: "))
               dikdortgen(kk,uk)
          elif secim == 3:
               yç = int(input("Dairenin yarıçapını giriniz: "))
               daire(yç)
          elif secim == 4:
               ak = int(input("Yamuğun alt kenar uzunluğunu giriniz: "))
               uk = int(input("Yamuğun üst kenar uzunluğunu giriniz: "))
               h = int(input("Yamuğun yüksekliğini giriniz: "))
               yamuk(ak,uk,h)
          elif secim == 5:
               dt = int(input("Üçgenin dikme inen taban uzunluğunu giriniz: "))
               h = int(input("Üçgenin yüksekliğini giriniz: "))
               ucgen(dt,h)
          elif secim == 6:
               ak = int(input("Paralelkenarın alt kenar uzunluğunu giriniz: "))
               h = int(input("Paralelkenarın yüksekliğini giriniz: "))
               paralelkenar(ak,h)
          elif secim == 7:
               ak = int(input("Eşkenar dörtgenin alt kenar uzunluğunu giriniz: "))
               h = int(input("Eşkenar dörtgenin yüksekliğini giriniz: "))
               eskenardortgen(ak,h)
          elif secim == 8:
               kk = int(input("Küpün kenar uzunluğunu giriniz: "))
               kup(kk)
          elif secim == 9:
               yç = int(input("Silindirin yarıçapını giriniz: "))
               h = int(input("Silindirin yüksekliğini giriniz: "))
               silindir(yç,h)
          elif secim == 10:
               yç = int(input("Kürenin yarıçapını giriniz: "))
               kure(yç)
          elif secim == 11:
               dt = int(input("Taban üçgeninin dikme inen taban uzunluğunu giriniz: "))
               y = int(input("Taban üçgeninin yüksekliğini giriniz: "))
               h = int(input("Prizmanın yüksekliğini giriniz: "))
               ucgenprizma(dt,y,h)
          elif secim == 12:
               kk = int(input("Taban dikdörtgeninin kısa kenar uzunluğunu giriniz: "))
               uk = int(input("Taban dikdörtgeninin uzun kenar uzunluğunu giriniz: "))
               h = int(input("Prizmanın yüksekliğini giriniz: "))
               dikdortgenprizma(kk,uk,h)
          else:
               print("Lütfen geçerli bir seçim yapınız.")
          
