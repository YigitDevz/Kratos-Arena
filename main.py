import random
import os

gladyatör={"isim" : "Kratos","can":100 ,"hasar":30,"altın":50,"max_can":100}

def sayi_al(mesaj):
    while True:
        giris = input(mesaj).strip()
        if giris == "":
            os.system("clear")
            print("\nBoş bırakma, bir sayı gir!")
            continue
        try:
            return int(giris)
        except ValueError:
            os.system("clear")
            print("\nGeçerli bir tam sayı girmelisin!")
            
#Dukkan

def dukkan(): 
  while True:
     profil=False
     os.system("clear")
     print(f"Altin Miktariniz:{gladyatör['altın']}")
     
     x=sayi_al("\nBir secim yapiniz: \nKalkan icin 1e basiniz(50altin),\nKilic icin 2 ye basiniz(50 altin),\nCanini yenilemek icin 3 e basiniz(75 altin),\nKutu Acmak için 4 e basiniz(100 altin),\nÇıkış yapmak için 5 e basiniz")
     
     if x==1 and gladyatör["altın"]>= 50:
         gladyatör["altın"]-=50
         gladyatör ["max_can"]+=25
         gladyatör["can"]+=25
         if gladyatör["can"]>gladyatör["max_can"]:
             gladyatör["can"]=gladyatör["max_can"]
         print(f"\nCan Kotan Arttırıldı,Yeni Can Kotan: {gladyatör['max_can']}")
        
     elif x==2 and gladyatör["altın"]>=50:
         gladyatör["hasar"]+=10
         gladyatör["altın"]-=50
         print("\nKılıç Satın alindi,Hasar Arttirildi")
       
     elif x==3 and gladyatör["altın"]>=75:
        gladyatör["can"]=gladyatör["max_can"]
        gladyatör["altın"]-=75
        print("\nCan İksiri Satın Alindi,Canın Fullendi")
        
 #Kutu sistemi       
     elif x==4:
        if gladyatör["altın"]<100:
            print("\nYetersiz Bakiye")
        else:
            gladyatör["altın"]-=100
        
            sans_havuzu=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]

            def kutu_acma(gladyatör):
              sayı=random.choice(sans_havuzu)
              print("\nŞans Kutusu Açılıyor")
    
              if sayı==27:
               gladyatör["altın"]+=500
               print("\n500 Altın KAZANDİNİZ!!")
              elif sayı==36:
               gladyatör["hasar"]+=100
               print("\nHasariniz +100 ARTTIRILDI")
              elif sayı==38:
                  gladyatör["can"]+=100
                  gladyatör["max_can"]+=100
                  print("\nKalkan +100 ARTTİRİLDİ")
              else:
               print("\nKutu Boş Cikti")
            
            kutu_acma(gladyatör)
            input("\nDevam Etmek İcin Entera basiniz")
        
     elif x==5:
        print("Dükkandan çıkılıyor")
        os.system("clear")
        profil=True
        if profil==True:
         print(f"\nKalan Canınız: {gladyatör['can']}/{gladyatör ['max_can']}") 
         print(f"\nAltin miktariniz: {gladyatör ['altın']}") 
         print(f"\nHasarınız: {gladyatör['hasar']}")  
         input("\nDevam etmek icin enter'a basiniz")
         os.system("clear")
         break
         
     elif x==6:
        print("Admin mod açılıyor")
        gladyatör["altın"]+=1000000
        
        
     else:
      print("Gecersiz Giris")
      
     

     
#Bosslar
void={"isim":"Void","can":50,"hasar":25,"altın":50}
eternal={"isim":"Eternal","can":100,"hasar":50,"altın":100} 
light={"isim":"Light","can":200,"hasar":100,"altın":250} 
darkness={"isim":"Darkness","can":500,"hasar":200,"altın":500}
dragon={"isim":"Dragon","can":1000,"hasar":500,"altın":1000}

#savaş

def savas(gladyatör,boss):
    if boss["isim"]=="Void":
        boss["can"]=50
    elif boss["isim"]=="Eternal":
        boss["can"]=100
    elif boss ["isim"]=="Light":
         boss["can"]=200
    elif boss["isim"]=="Darkness":
         boss["can"]=500
    elif boss["isim"]=="Dragon":
         boss["can"]=1000
     
    print(f"Savaş Başladı: {gladyatör['isim']} vs {boss['isim']}")
    while True:
       alınan_hasar=boss["hasar"]
       savundum=False 
       boss_savunma= False
       boss_hamlesi=random.choice(["saldır","savun"])
       
       print(f"Canın: {gladyatör['can']}/{gladyatör['max_can']}")
       print(f"{boss['isim']} Canı: {boss['can']}")
       
       hamle=sayi_al("Hamle Seç(1:Saldırı 2:Savunma)")
       os.system("clear")
       
       if hamle==2:
           savundum=True
           print(f"{gladyatör['isim']} Savunma Pozisyonuna Geçti")
           
       if boss_hamlesi=="savun":
           boss_savunma=True
           print(f"{boss['isim']} Savunmaya geçti")
       
       if hamle==1:
            vurulan=(gladyatör ["hasar"]//2 if boss_savunma else gladyatör ["hasar"])
            boss["can"]-=vurulan
            print(f"{gladyatör ['isim']} {boss['isim']} e {vurulan} vurdu!")
            print(f"Bossun Kalan Canı: {boss['can']}")
            
       if boss["can"]<=0:
            gladyatör["altın"]+=boss["altın"]
            print(f"{gladyatör['isim']} {boss['altın']} Kazandı!")
            print(f"{gladyatör['isim']} KAZANDİ")
            input("Devam Etmek İçin Enter'a Basiniz")
            break
            
       if boss_hamlesi=="saldır":
             alınan=boss["hasar"]//2 if savundum else boss["hasar"]
             gladyatör["can"]-=alınan_hasar
             print(f"{boss['isim']} SALDIRDI ve {alınan} vurdu")
             print(f"Kalan canınız: {gladyatör ['can']}") 
             
       else:
            print(f"{boss['isim']} Bu tur saldirmadi") 
            
       if gladyatör["can"]<=0:
            print("Kaybettiniz")     
            exit()

#arena
            
while True:
 print("Dukkana Hos geldiniz")       
 dukkan()     
 print("---ARENAYA HOŞGELDİNİZ---")
 print("1. Void (Kolay)")
 print("2. Eternal (Orta)")
 print("3. Light (Zor)")
 print("4. Darkness(Cehennem)")
 print("5. Dragon(İmkansiz)")

 secim=sayi_al("Bir Boss Seçiniz")
 os.system("clear")

 if secim==1:
    if gladyatör["hasar"]<=10 or gladyatör["can"]<=10:
        print("\nBu boss icin yeteri kadar gucunuz yok")
        input("\nYeniden denemek için enter'a basiniz")
        dukkan()
        
    else:        
     savas(gladyatör,void)
    
 elif secim==2:
    if gladyatör ["hasar"]<=50 or gladyatör["can"]<=50:
        print("\nBu boss icin yeteri kadar gucunuz yok ")
        input("\nYeniden denemek icin enter'a basiniz")
        dukkan()
        
    else:    
     savas(gladyatör,eternal)
    
 elif secim==3:
      if gladyatör ["hasar"]<=150 or gladyatör["can"]<=150:
        print("\nBu boss icin yeteri kadar gucunuz yok ")
        input("\nYeniden denemek icin enter'a basiniz")
        dukkan()
        
      else:
       savas(gladyatör,light)
    
 elif secim==4:
      if gladyatör ["hasar"]<=300 or gladyatör["can"]<=300:
        print("\nBu boss icin yeteri kadar gucunuz yok ")
        input("\nYeniden Denemek icin enter'a basiniz")
        dukkan()
        
      else:
       savas(gladyatör,darkness)
    
 elif secim==5:
      if gladyatör ["hasar"]<=500 or gladyatör["can"]<=500:
        print("\nBu boss icin yeteri kadar gucunuz yok ")
        input("\nYeniden denemek icin enter'a basiniz")
        dukkan()
        
      else:   
       savas(gladyatör,dragon)
 else:
    print("Geçersiz Giriş")
