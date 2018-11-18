import random
n = random.randint(1, 99)
liczba = int(input("Wybierz liczbe z przedziału 1 do 99: "))
while n != "liczba":
    print
    if liczba < n:
        print ("Liczba za mala")
        liczba = int(input("Wybierz liczbe z przedziału 1 do 99: "))
    elif liczba > n:
        print ("Liczba za duza")
        liczba = int(input("Wybierz liczbe z przedziału 1 do 99: "))
    else:
        print ("Poprawna odpowiedz")
        break
    print
