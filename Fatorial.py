def numero():
    numero = int(input("Número: "))
    fatorial = 1
    while numero > 0:
        fatorial *= numero
        numero -= 1
    return fatorial
print(numero())
