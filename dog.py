class Cachorro:
    cachorros_cadastrados = []
    def __init__(self, nome, raca, idade, cor):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.cor = cor
        Cachorro.cachorros_cadastrados.append(self)

    @classmethod
    def listar_cachorros(cls):
        if not cls.cachorros_cadastrados:
            print("Nenhum cachorro cadastrado")
            return
        
        print("\n------------------- Cachorros cadastrados -------------------")
        for i, cachorro in enumerate(cls.cachorros_cadastrados,1):
            print(f"{i}. {cachorro.nome} | {cachorro.raca} | {cachorro.idade} anos | {cachorro.cor}")
        print("---------------------------------------------------------------")

        
        