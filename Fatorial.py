numero = int(input("Número: "))
fatorial = 1

print (f"O resultado de {numero}! = ", end="")

while numero > 0:
    
    fatorial *= numero
    print(f"{numero}", end = " ")
    print(f" x " if numero > 1 else "=", end = " ")
    numero -= 1
    
print(fatorial)