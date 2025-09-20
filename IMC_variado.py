## Se estiver bagunçado é pq eu fiquei com preguiça de arrumar depois que terminei.
## Falando isso desde o início pra pedir desculpas de antemão, professor. KKKKKKKKK.

lista = []
repetição = True
while repetição:
    nome = input("Digite seu nome: ")
    if nome == "parar":
        break
    lista.append(nome)

    peso = (input("Digite seu peso: "))
    if peso == "parar":
        lista.remove(lista[-1])
        lista.remove(lista[-1])
    if peso == "parar":
        break
    lista.append(peso)

    altura = (input("Digite sua altura: "))
    if altura == "parar":
        lista.remove(lista[-1])
        lista.remove(lista[-1])


    if altura == "parar":
        break
    lista.append(altura)

    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura * altura)
    lista.append(imc)

    print(f"O IMC de {nome} é {imc:.2f}")
    




print(lista)