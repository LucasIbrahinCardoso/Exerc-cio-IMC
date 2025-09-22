lista = []
tipos = ["Baixo peso", "Peso normal", "Sobrepeso", "Obesidade grau 1", "Obesidade grau 2", "Obesidade grau 3"]

def testador(coiso):
    if coiso < 18.5:
        return 0
    if coiso >= 18.5 and coiso < 25:
        return 1
    if coiso >= 25 and coiso < 30:
        return 2
    if coiso >= 30 and coiso < 35:
        return 3
    if coiso >= 35 and coiso < 40:
        return 4
    if coiso >= 40:
        return 5
while True:
    nome = input("Digite seu nome: ")
    if nome == "parar":
        break
    lista.append(nome)

    peso = (input("Digite seu peso: "))
    if peso == "parar":
        lista.remove(nome)
        break        
    lista.append(peso)

    altura = (input("Digite sua altura: "))
    if altura == "parar":
        for j in range(0, len(lista), 1):
            if j == len(lista) - 2:
                lista.pop(j + 1)
                lista.pop(j)
        break
    lista.append(altura)

    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura * altura)
    lista.append(imc)
for l in range(0, len(lista), 4):
    if l == 0:
        qual_imc = testador(lista[3])
        print(f"O IMC de {lista[l]} é {tipos[qual_imc]}")
    else:
        qual_imc = testador(lista[l + 3])
        print(f"O IMC de {lista[l]} é {tipos[qual_imc]}")