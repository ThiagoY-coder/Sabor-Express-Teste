class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

"""
Classe de avaliação representa uma avaliação feita por um cliente a um restaurante. Ela armazena o nome do cliente e a nota atribuida, que deve estar entre 0 e 5. A classe é utilizada dentro da classe Restaurante para gerenciar as avaliações rececbidas.
"""