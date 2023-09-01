#"def" abre a função e logo nomeamos a variavel.
def soma(x:int | float, y:int |float) -> int|float:
    """"Soma x + y e retorna o resultado."""
    #resultado = x + y
    return x + y
def print_subtracao(x: int |float, y: int | float) -> None: 
    """"Soma x + y e mostra o resulado na print"""
    print(f"{x-y}")

def soma_sem_parametro()-> int|float:
    x=5
    y=5

a = soma(1,2)
