#crie um progama que receba uma idade e retorne se pode obter a carteira de mtorista.

idade = input("Informe a sua idade:")
try:

    if int (idade) >= 18:
        print(f"Você tem a idade para tirar sua CNH({idade}anos).")
    elif int(idade) < 18:
        print(f"Você não tem a idade minima(18anos) pra tirar a CNH, sua idade({idade}anos)")
except ValueError:
        raise print("Coloque um número válido")
   