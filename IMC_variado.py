## Se estiver bagunçado é pq eu fiquei com preguiça de arrumar depois que terminei.
## Falando isso desde o início pra pedir desculpas de antemão, professor. KKKKKKKKK.

repetição = True
while repetição:
    nome = input("Qual o seu nome? ")
    peso = float(input("Qual o seu peso? "))
    altura = float(input("Qual a sua altura? "))

    imc = peso / (altura * altura)
    print(f"O IMC de {nome} é {imc:.2f}")


    if nome == "parar" or peso == "parar" or altura == "parar":
        repetição = False