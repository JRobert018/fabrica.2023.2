#crie um progama que peça um número e mostre seu sucessor e antecessor.
#a váriavel "numero" irá pegar um número inteiro do usuário, já os outros 2(antecessor e sucessor)vão somar e subtrair,para obter os resultados.
numero = int(input("Digite um número inteiro:"))
antecessor = (numero - 1)
sucessor = (numero + 1)
#Os prits vão apresetar a menagem informando qual é o sucessor e antecessor do número escolhido.
print("O número sucessor de:",numero,"é:",sucessor)
print("O número antecessor de:",numero,"é:",antecessor)