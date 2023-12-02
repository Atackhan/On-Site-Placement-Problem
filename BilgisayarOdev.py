departmanlar= [[0, 20, 70, 40, 20, 90, 40, 20, 5],
         [20, 0, 60, 80, 40, 80, 20, 10, 10],
         [30, 20, 0, 120, 30, 5, 50, 20, 5],
         [40, 80, 120, 0, 10, 20, 80, 55, 20],
         [20, 40, 70, 10, 0, 50, 20, 10, 5],
         [90, 80, 20, 20, 50, 0, 90, 20, 20],
         [40, 20, 120, 90, 20, 90, 0, 10, 25],
         [20, 10, 20, 55, 10, 20, 10, 0, 5],
         [5, 10, 5, 20, 5, 10, 25, 5, 0]]

alanlar = [[0, 35, 20, 25, 45, 35, 85, 60, 75],
         [85,60, 35, 70, 40, 0, 50, 70, 95],
         [10, 35, 0, 25, 35, 15, 75, 40, 50],
         [25, 30, 25, 0, 10, 40, 20, 40, 35],
         [65, 20, 35, 10, 0, 50, 30, 50, 45],
         [95, 50, 15, 40, 50, 0, 20, 25, 35],
         [35, 50, 35, 20, 30, 20, 0, 20, 15],
         [60, 70, 40, 40, 50, 25, 20, 0, 10],
         [15, 65, 50, 35, 45, 35, 15, 10, 0]]

deger1 = 0
deger2 = 0
deger3 = 0
deger4 = 0
say = 0

liste1 = [int(item) for item in input("Sıralama Giriniz").split(",")]
liste2 = [int(item) for item in input("Sıralama Giriniz").split(",")]

while len(liste1) != 9:
    print("1'den 9'a kadar farklı değerler giriniz")
    liste1 = [int(item) for item in input("Departman Sıralamasını Girin:").split(",")]

while len(liste2) != 9:
    print("1'den 9'a kadar farklı değerler giriniz")
    liste2 = [int(item) for item in input("Departman Sıralamasını Girin:").split(",")]

for i in range(0, len(liste1)):
    if say > 0:
        print("lütfen birbirinden farklı 1'den 9'a değerler giriniz")
        break
    else:
        for j in range(0, len(liste1)):
            if (liste1)[i] == (liste1)[j] and i != j:
                say = say + 1
                break

for i in range(0, len(liste2)):
    if say > 0:
        print("lütfen birbirinden farklı 1'den 9'a değerler giriniz")
        break
    else:
        for j in range(0, len(liste2)):
            if (liste2)[i] == (liste2)[j] and i != j:
                say = say + 1
                break
if say == 0:
    liste3 = []
    liste4 = []
    liste5 = []
    liste6 = []
    ml = []

    a = list.copy(liste1)
    b = list.copy(liste2)
    import random

    rassal = random.randint(0, len(liste1) - 1)

    for i in range(0, rassal):
        liste3.append(liste1[i])
        liste4.append(liste2[i])

    for j in range(0, rassal):
        a.remove(liste4[j])
        b.remove(liste3[j])
    liste3.extend(b)
    liste4.extend(a)

    deger1 = random.randint(0, len(liste1) - 1)
    deger2 = random.randint(0, len(liste1) - 1)
    while deger1 == deger2:
        deger1 = random.randint(0, len(liste1) - 1)
        deger2 = random.randint(0, len(liste1) - 1)

    deger3 = random.randint(0, len(liste1) - 1)
    deger4 = random.randint(0, len(liste1) - 1)
    while deger1 == deger2:
        deger1 = random.randint(0, len(liste1) - 1)
        deger2 = random.randint(0, len(liste1) - 1)

    c = list.copy(liste3)
    d = list.copy(liste4)

    e = c[deger1]
    f = c[deger2]
    g = d[deger3]
    h = d[deger4]

    c.pop(deger1)
    c.insert(deger1, f)

    c.pop(deger2)
    c.insert(deger2, e)

    d.pop(deger3)
    d.insert(deger3, h)

    d.pop(deger4)
    d.insert(deger4, g)

    liste5.extend(c)
    liste6.extend(d)

    print(liste1)
    print(liste2)
    print(liste3)
    print(liste4)
    print(liste5)
    print(liste6)

    X = [liste1, liste2, liste3, liste4, liste5, liste6]

    for k in range(0, len(X)):
        maliyet = 0
        for i in range(0, len(X[k])):
            if say > 0:
                print("lütfen birbirinden farklı 1'den 9'a değerler giriniz")
                break
            else:
                for j in range(0, len(X[k])):
                    if (X[k])[i] == (X[k])[j] and i != j:
                        say = say + 1
                        break
                    if (X[k])[i] < 1 or (X[k])[i] > 9:
                        say = say + 1
                        break

        if say == 0:
            if len(X[k]) == 9:
                for i in range(0, len(X[k])):
                    if i + 1 >= len(X[k]):
                        break
                    else:
                        x = (X[k])[i]
                        y = (X[k])[i + 1]
                        gidis= departmanlar[x - 1][y - 1]
                        alinan_yol = alanlar [x - 1][y - 1]
                        maliyet = maliyet + (gidis * alinan_yol)
                print(maliyet)
                ml.append(maliyet)
                if len(ml) == 6:
                    index = ml.index(min(ml))
                    print("En düşük maliyetli sıralama {}'dir ve maliyeti={}'dir".format(X[index], min(ml)))

            else:
                print("1'den 9'a kadar farklı değerler giriniz")



