'''

Daire alanı : π r²
Daire Çevresi : 2π r

*yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r:3.14)


'''


pi = 3.14
yarıçap = float(input("Yarı Çap : "))
 
alan = pi * (yarıçap** 2 )
 
çevre = pi * 2 * yarıçap


print("Alanı:", alan)
print("Çevresi:", çevre)


#eğer string birleştirme yapmak istersek yani alan ve çevre sonuçlarını tek bir print komutu ile göstermek istersek kodumuz şu sekilde olmalıdır.


print("Alan:", str(alan), "Çevresi:",  str(çevre)) # bu şekilde alan ve çevre değişkenlerini veri tipi değiştirme ile str ye dönüştürmemiz gerekir.