class Filme:
    def __init__(self, nome, ano, duracao, imdb):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__imdb = imdb
        self.__likes = 0
   
    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1
   
    @property
    def nome(self):
        return self.__nome

    @property
    def imdb(self):
        return self.__imdb
   
    @imdb.setter
    def imdb(self, imdb):
        self.__imdb = imdb
   
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

class Serie:
    def __init__(self, nome, ano, temporada, imdb):
        self.nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.imdb = imdb
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1
   
    @property
    def nome(self):
        return self.__nome
   
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

cloverfield = Filme("Cloverfield: Monstro", 2008, 85, 7.0)
lorax = Filme("O Lorax: Em Busca da Trúfula Perdida", 2012, 86, 6.4)
pequenos_espioes_4 = Filme("Pequenos Espiões 4", 2011, 89, 3.5)
inception = Filme("A Origem", 2010, 148, 8.8)
matrix = Filme("Matrix", 1999, 136, 8.7)
interstellar = Filme("Interestelar", 2014, 169, 8.6)
toy_story = Filme("Toy Story", 1995, 81, 8.3)
up_altas_aventuras = Filme("Up: Altas Aventuras", 2009, 96, 8.2)
shrek = Filme("Shrek", 2001, 90, 7.9)
pantera_negra = Filme("Pantera Negra", 2018, 134, 7.3)