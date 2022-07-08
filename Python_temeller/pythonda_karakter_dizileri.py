name = "Eren"
surname = "Yabacı"
age = 21

selamlama = "Merhaba benim adım "+ name + " Soyadım " + surname + "  \nYaşım " + str(age) 
#burda str(age) yazmamdaki sebeb string toplama yapıyorum age bir integer değer bundan dolayı int to str yaptım
# \n ile konulduğu yerden sonra alt satıra geçme komutudur.
print(selamlama)


#pythonda karakter dizisi 0 dan başlar 1234.... yada 0 dan başlar -1 -2 -3 gibi gider + yönde giderse soldan sağa - yönde olursa sağdan sola sayar.

print(selamlama[2])#bu şekilde köşeli parantez açarsak köeşli parantezin içine yazdığımız karakter numarası ekrana yazılır yani 2. karakter ekrana yazılır.

print(len(selamlama))#len komutu ingilizce lenght yani uzunlıktan gelir istediğimiz bir değikenin yada metinin yada kodun artık her neyse karakter uzunluğunu bize verir.

print(selamlama[0:]) # bu şekilde bir değer yazıp sonuna : iki nokta korsak yazılan değerden sonra hepsini ekrana yazar.

print(selamlama[0:10])# bu şekilde ilk değer yani 0 dan başla : iki nokta 10'a kadar göster 10 dahil değil demek.

print(selamlama[0:48:2])# burda 0 dan başla 48'e kadar 48 dahil değil 2 şer 2 şer atlayarak göster demek

print(selamlama[len(selamlama)-6]) # der isek sondan 6. karakteri göser demek

print(selamlama[::-1]) #dersek eğer seçilen değişkeni tersen yazdırmış oluruz 

