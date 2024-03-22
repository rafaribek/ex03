def construir_piramide(base):
    piramide = [base]
    while len(base) > 1:
        novo_nivel = [base[i] + base[i+1] for i in range(len(base)-1)]
        piramide.insert(0, novo_nivel)
        base = novo_nivel
    return piramide

def imprimir_piramide(piramide):
    for nivel in piramide:
        print(" ".join(str(tijolo) for tijolo in nivel))

def main():
    base = input("Digite os valores dos tijolos da base da pirâmide separados por espaços: ").split()
    base = [int(valor) for valor in base]
    piramide = construir_piramide(base)
    imprimir_piramide(piramide)

if __name__ == "__main__":
    main()
