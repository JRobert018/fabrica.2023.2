#crie um progama que receba uma idade e retorne se pode obter a carteira de mtorista.
#pega a idade da pessoa 
idade = input("Informe a sua idade:")
#vai tentar nesses criterios.
try:

    if int (idade) >= 18:
        print(f"Você tem a idade para tirar sua CNH({idade}anos).")
    else:
        print(f"Você não tem a idade minima(18anos) pra tirar a CNH, sua idade({idade}anos)")
#se for colocado algo errado irá apresentar essa mensagem ao usuário.
except ValueError:
        print("Coloque um número válido")