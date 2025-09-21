lista = []
repetição = True
while repetição:
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
    
for i in range(0, len(lista), 4):
    print(f"{lista[i]} tem IMC de {lista[i+3]}")