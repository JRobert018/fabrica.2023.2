#Crie um programa que leia uma velocidade de um carro e mult se passar com a velocidadee maior que 80km\h
# E a multa aumenta 7R$ por km acima do limite.

velocidade = int(input("Qual erá a velocidade do veiculo(km/h)?:"))
try:
    if velocidade > 80:
        print(f"A velocidade do veiculo era de {velocidade}km/h e foi multado no valor de {(velocidade - 80) * 7}R$.")
    else:
        print(f"Estava dentro do limite de velocidade {velocidade}km/h.")
except ValueError:
    print("erro")