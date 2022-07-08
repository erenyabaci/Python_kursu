name = "Eren"
surname = "Yabacı"
age = 21

# selamlama = "Merhaba benim adım "+ name + " Soyadım " + surname + "  \nYaşım " + str(age) 

# bu şekilde yazılan kod karmaşıktır paythonda format komutu ile bu komutu daha basit bir şekilde nasıl yazılır onu görücez.

# selamlama = ("Merhaba benim adım {} soyadım {} yaşım {} ".format(name, surname, age)) 
# selamlama = ("Merhaba benim adım {n} soyadım {s} yaşım {a} ".format(n=name, s=surname, a=age)) 
selamlama = (f"Merhaba benim adım {name} soyadım {surname} yaşım {age} ") 

# gibi yazılır bu sayade integer bir ifadeyi stringe çevirmek zorunda kalmayız otomatik çevirir değişkenler arasına boşluk koymayız son derece basittir.
print(selamlama)

