mesaj = "Ben Eren Yabacı 22 yaşındayım"

# mesaj = mesaj.split(" ") #split komutu cümleyi dizin şeklinde bölmemize yarar parantez içine ne yazarsak oralardan böler boşluk karakteri korsak boşluk har yazarsak harf noktalama işareti dersek ordan böler

# -------------------------------------------------------------------Join methodu ---------------------------------------------------------------------
# mesaj = 'Ben', 'Eren', 'Yabacı', '22', 'yaşındayım'

# mesaj = " ".join(mesaj)              # ilk başta karakterler arasını ne konulacak o seçili " " boşluk karakteri koymuşum ben daha sonra .join() yazıp birleşecek değişkeni parantez içine yazmışım .join(mesaj) gibi

# ------------------------------------------------------------------Upper methodu ---------------------------------------------------------------------

#mesaj = mesaj.upper()                 # tüm değişkeni büyük harfe çevirir.

#-------------------------------------------------------------------Lower methodu ---------------------------------------------------------------------

#mesaj = mesaj.lower()                # tüm değişknei küçük harfe çevirir


#---------------------------------------------------------------- Capitalize methodu ------------------------------------------------------------------

#mesaj = mesaj.capitalize()           # değişkenin ilk harfini büyük yapar

#-------------------------------------------------------------------title methodu----------------------------------------------------------------------


# mesaj= mesaj.title()                # değişkenin ilk harflerini büyük yapar.


#------------------------------------------------------------------Center methodu----------------------------------------------------------------------

#mesaj= mesaj.center(100) # bu komutta değişkeni 100 karakterlin alana ortalar boşluk karakteri ile

#mesaj= mesaj.center(100, "*") # bu komutta ise değişkeni 100 karakterlik alana * lar ile ortalar diğer koddaki gibi boşluk gözükmez yıldız gözükür.

#------------------------------------------------------------------startswith methodu------------------------------------------------------------------

#mesaj = mesaj.startswith("B") # değişkenin hangi harf yada hangi kelime ile başladığını bool yani true yada false ile bize söyleyen methoddur .
#mesaj = mesaj.startswith("Ben")


#------------------------------------------------------------------endswith methodu------------------------------------------------------------------

#mesaj = mesaj.endswith("m")               # değişkenin hangi harf yada kelime ile bittiğini bool komuutu ile yani true yada false ile bize söyleyen methoddur . 
#mesaj = mesaj.endswith("yaşındayım")


#-------------------------------------------------------------------replace methodu-------------------------------------------------------------------

# mesaj = mesaj.replace("Eren", "Kerim")        # bu method değişkendeki bir karakteri yada değeri değiştirmemize yarar


#-------------------------------------------------------------------ljust methodu-------------------------------------------------------------------

# mesaj = mesaj.ljust(100) sağdan sola doğru 100  karakter boşluk bırak anlamına gelen method
# mesaj = mesaj.ljust(100, "*")  #sağdan sola doğru 100  karakter boşluk bırak boşlukara * koy anlamına gelen method

#-------------------------------------------------------------------rjust methodu-------------------------------------------------------------------

# mesaj = mesaj.rjust(100) #soldan sağa doğru 100  karakter boşluk bırak anlamına gelen method
# mesaj = mesaj.rjust(100, "*")  #soldan sağa  doğru 100  karakter boşluk bırak boşlukara * koy anlamına gelen method





print(mesaj)