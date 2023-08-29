num = input("Qual número deseja?")#retorna uma string digitada pro usuário
try:
    antecessor = int(num)-1
    sucessor = int(num)+1
except: 
    raise ValueError    
    
print(f"O número digitado foi {num} e seu antecessor é {antecessor} e o sucessor é {sucessor}")

print(type(num))
print(type(antecessor))
print(type(sucessor))