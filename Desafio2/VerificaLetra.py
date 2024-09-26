linha = input("Escreva uma String para contar quantas letras A existem: ")
linha_minusucla = linha.lower()

n = 0
if "a" in linha_minusucla:
    for i in range(len(linha_minusucla)):
        if linha_minusucla[i] == "a":
            n += 1
    print(f"A letra A está presente na String inserida, há {n} letras A.")
else:
    print(f"A letra A não está presente na String inserida, há {n} letras A.")