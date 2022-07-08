# 1-) Aşağıdaki verilen başlıklarla değişken oluşturunuz. 
# müşteri adı
# müşteri soyadı
# müşteri adı ve soyadı
# müşteri cinsiyeti
# müşteri tc kimlik numarası
# müşteri doğum yılı
# müşteri adresi
# müşteri yaşı

# CEVAPLAR

musteriAdi = "Eren"
musteriSoyadi = "Yabacı"
musteriAdSoyadi= musteriAdi + "" + musteriSoyadi # ortada kullandığım +""+ iki değişkeni ekrana yansıttımgımızda aralarında boşluk olmasını sağlar.
musteriCinsiyeti = True  # true değeri erkek olarak kabul edilir bu bir bool türdür.
musteriTc = "10254032658" # herhangi bir işlem yapılmayacağı için tc numarası string olarak tutulur.
musteriDogumYili = 2001 #hesaplama yapılacağı için integer olarak tutmamız gerekir hesaplama yapılmayacaksa string olarak tutulmalıdır.
musteriAdresi = "Tokat Merkez"
musteriYasi = 2022 - musteriDogumYili # mevcut bulunuluan yıldan doğum yılı çıkartılarak yaş bulunur.

# 2-) Aşagıdaki siparişlerin toplam bilgisini hesaplayınız.

# Sipariş 1 => 110 Tl
# Sipariş 2 => 1100.5 Tl
# Sipariş 3 => 356.95 Tl

# CEVAPLAR

siparis1 = 110
siparis2 = 1100.5
siparis3 = 356.95
# toplama işlemi yaptığım için değişkenleri integer ve float cinsinden girmek zorundayım.

toplam = siparis1+siparis2+siparis3 # burda yaptığım işlem yapılacak değişkenleri bir değişken içine toplamak

print("Toplam:", toplam) # burda yaptığım ise ekrana yazılacak toplama işleminin başına toplam : yazmak için önce "toplam :" yazdım sonra virgül koyup yukarıda birleştirdiğim değişkenin ismini yazdım.

