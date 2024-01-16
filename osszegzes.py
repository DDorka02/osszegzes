def feladat():
    while n < 0:
        n = int(input("N = "))
    osszeg = 0
    for i in range(0, n+1):
        osszeg += i
    print(f"Az első {n} db természetes szám összege: {osszeg}")
