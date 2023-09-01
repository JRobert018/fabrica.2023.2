from abc import ABC,abstractclassmethod

class IAnimal(ABC):

    @abstractclassmethod
    def falar(self):
        """"defina na classe fiha"""  


    @abstractclassmethod
    def andar(self):
        """""defina na classe filha."""

class Cachorro(IAnimal):
    def falar (self):
        print("AuAu")
    
    def andar(self):
        print("Ando em 4 patas.")

class Pessoa:
    def __init__(self,nome:str,idade:int):
        self._nome = nome
        self.idade = idade
        self. __humano = True
    
    def fala_pessoa(self):
        print("falando")



#animal = IAnimal()
pingo = Cachorro()
pingo.falar()
pingo.andar()