def somar(numeros):
    if numeros == "":
        return 0
    total = 0
    for n in numeros.split(","):
        total += int(n)
    return total


    