# GÖREV 2

text = "The goal is to turn data into information, and information into insight."
UpperText = text.upper()
UpperText = UpperText.replace(",", " ")
UpperText = UpperText.replace(".", " ")
UpperText = UpperText.split()
print(UpperText)

###################################################
# GÖREV 3

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# 1
len(lst)
# 2
print(lst[0], lst[10])
# 3
new_lst = [lst[0], lst[1], lst[2], lst[3]]  # = lst[0:4] de olur.
# 4
lst.pop(8)
# 5
lst.append("B")
# 6
lst.insert(8, "N")
print(lst)

###################################################
# GÖREV 4

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# 1
dict.keys()
# 2
dict.values()
# 3
dict.update({"Daisy": ["England", 13]})  #dict["Daisy"][1] = 13 ÇOK DAHA İYİ
print(dict)
# 4
dict.update({"Ahmet": ["Turkey", 24]})
# 5
dict.pop("Antonio")
print(dict)

###################################################
# GÖREV 5

l = [2, 13, 18, 93, 22]


def func(list=l):
    even_list = []
    odd_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list


even_list, odd_list = func(l)

###################################################
# GÖREV 6

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

muhendislik = ogrenciler[0:3]
tip = ogrenciler[3:6]

for i, ogrenci in enumerate(muhendislik, 1):
    print(f"Mühendislik Fakültesi {i} . öğrenci: {ogrenci}")

for i, ogrenci in enumerate(tip, 1):
    print(f"Tıp Fakültesi {i} . öğrenci: {ogrenci}")


# bu daha efektif
""" for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x) """

###################################################
# GÖREV 7

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

zipped = list(zip(ders_kodu, kredi, kontenjan))
print(zipped)

for ders in zipped:
    print(f"Kredisi {ders[1]} olan {ders[0]} kodlu dersin kontenjanı {ders[2]} kişidir.")


# daha az variable
"""for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")"""

###################################################
# GÖREV 8

kume1 = {"data", "python"}  # bunlar set
kume2 = {"data", "function", "qcut", "lambda", "python", "miuul"}

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))