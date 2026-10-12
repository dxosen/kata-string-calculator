def somar(numeros):
    if numeros == "":
        return 0
    if numeros.startswith("//"):
         separador = numeros[2]
         numeros = numeros[4:]
         numeros = numeros.replace(separador, ",")
    numeros = numeros.replace("\n", ",")
    total = 0
    for n in numeros.split(","):
        total += int(n)
    return total