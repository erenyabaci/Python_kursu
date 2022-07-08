from tkinter import W


website = "http://www.sadikturan.com"
course  = "Phyton kursu: Baştan Sona Phyton Programlama Rehberiniz (40 saat)"

#1-) coruse karakter dizisinde kaç karakter bulunmaktadır ?

#2-) website içinden www karakterlerini alın.

#3-) website içinden com karakterlerini alın.

#4-) coruse içinden ilk 15 ve son 15 karakteri alın 

#5-) coruse ifadesindeki karakterleri tersten yazdırın 


name, surname, age, job= "Bora", "yılmaz", 32, "mühendis"

# Yukarıda verilen değişkenler ile ekrana aşağıgaki ifadeleyi yazdırın 

#6-) Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim  mühendis.


#1-) Cevap

# print(len(course))

#2-) Cevap

www1 = website[0:7] # burada 0 dan başla 7. karaktere kadar göster dedik
www2 = website[11:65] # burada 11. karakterden başla 65.karaktere kadar göster dedik daha sonra aşağıda olduğu gibi str topladık

wwwCıkıs = www1 + www2 #str toplama yaptık

print(wwwCıkıs) # burada www dizinden silmiş olduk 

#3-) Cevap 

comcıkıs = website[0:-4]

print(comcıkıs)# burda 0.ıncı karakterden başla -4 karaktere kadar göster dedik yani sondan -4 çıkardı

print(wwwCıkıs[0:-4]) #burdada 34.satırda yaptığımız www çıkarma işleminin üstüne bide sondan -4 karakter daha sildik yani com uda silmiş olduk.

#4-) Cevap 
print(course[14:51]) # burda 14 den başla 51 e kadar göster dedik

#5-) Cevap

print(course[::-1]) # değişkeni tersten yazdrımış oluruz [::-1 komutu ile]

#6-) Cevap

birlestirme =("Benim adım {} {}, Yaşım {} ve Mesleğim {}".format(name, surname, age, job))

print(birlestirme)