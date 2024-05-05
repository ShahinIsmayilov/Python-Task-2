"Task1"#(Verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın.)

# def ededin_kvadrati(siyahı):
#     for num in siyahı:
#         if num > 0 and (int(num ** 0.5)) ** 2 == num:
#             print(f"{num} ədədi, {int(num ** 0.5)} ədədin kvadratıdır.")

# siyahı = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# ededin_kvadrati(siyahı)


"Task2"#(Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın.)

# def təkrarlanmayan_elementlər(siyahı):
#     təkrarlanmayanlar = []
#     for element in siyahı:
#         if siyahı.count(element) == 1:
#             təkrarlanmayanlar.append(element)
#     return təkrarlanmayanlar

# siyahı = input("Zəhmət olmasa bir siyahı daxil edin: ")
# print("Təkrarlanmayan elementlər:", təkrarlanmayan_elementlər(siyahı))


"Task3"#(Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın.)

# def reqemlerin_hasili(input):
#     hasil = 1
#     for vuruq in input:
#         if '0' <= vuruq <= '9':
#             hasil *= int(vuruq)
#     return hasil

# reqem = input("Zəhmət olmasa bir ədəd daxil edin: ")
# print("Rəqəmlərin bir-birlərinə hasili:", reqemlerin_hasili(reqem))


"Task4"#(Verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın.)

# def bolenler(num):
#     bolenler = [i for i in range(1, num + 1) if num % i == 0]    
#     return bolenler

# eded = int(input("Bir ədəd daxil edin: "))
# print(f"{eded} ədədin bölənləri:", bolenler(eded))


"Task5"#(Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.)

# aylar = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avqust", "sentyabr", "oktyabr", "noyabr", "dekabr"]

# ay_uzunluğu= {ay: len(ay) for ay in aylar}

# print(ay_uzunluğu)


"Task6"#(Verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da istifadə edəbilərsiz).)

# def adlarin_kicik_herfleri(adlar):
#     kicik_ad_siyahisi = []
    
#     for ad in adlar:
#         kicik_ad_siyahisi.append(ad.split()[0].lower())
#     return kicik_ad_siyahisi

# adlar = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# kicik_herfli_adlar_listesi = adlarin_kicik_herfleri(adlar)

# print(kicik_herfli_adlar_listesi)


"Task7"#(Verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.)

# siyahi1 = [1, 2, 3]
# siyahi2 = [4, 5, 6]

# ortalamalar = [(siyahi1[i] + siyahi2[i]) / 2 for i in range(len(siyahi1))]
# print("Ortalamalar:", ortalamalar)