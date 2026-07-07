from modelos.avaliacao import Avaliacao

class Restaurante:
    """
    Representa um restaurante no sistema.

    Esta classe gerencia as informações básicas de um restaurante, seu estado 
    de funcionamento (ativo/inativo) e as avaliações recebidas pelos clientes. 
    Mantém também um registro de todas as instâncias de restaurantes criadas.

    Attributes:
        restaurantes (list): Lista estática (da classe) que armazena todas as 
                             instâncias de Restaurante criadas.
    """
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma nova instância de Restaurante.

        Args:
            nome (str): O nome do restaurante. Será formatado no estilo 'Title'.
            categoria (str): A categoria gastronômica do restaurante (ex: 'Italiana', 'Japonesa').
        """
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """
        Retorna uma representação em formato de string do restaurante.

        Returns:
            str: O nome do restaurante e sua categoria formatados para exibição.
        """
        return f'{self._nome.ljust(20)} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """
        Exibe no console uma tabela formatada com todos os restaurantes cadastrados.
        
        A tabela inclui os cabeçalhos: Nome do Restaurante, Categoria, Avaliação e Status.
        """
        print(f'{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """
        Informa o status atual do restaurante de forma textual.

        Returns:
            str: Retorna 'Ativo' se o atributo _ativo for True, caso contrário 'Inativo'.
        """
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alternar_status(self):
        """
        Alterna o status de funcionamento do restaurante.
        
        Se estiver ativo (True), passa para inativo (False), e vice-versa.
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma nova avaliação para o restaurante.

        A avaliação só é aceita se a nota estiver no intervalo permitido (entre 0 e 5).

        Args:
            cliente (str): O nome do cliente que fez a avaliação.
            nota (int/float): A nota dada pelo cliente (de 0 a 5).
        """
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        """
        Calcula e retorna a média das notas das avaliações do restaurante.

        Returns:
            float: A média aritmética das notas arredondada para 1 casa decimal.
            str: Retorna a mensagem 'Sem avaliações' caso o restaurante não tenha recebido nenhuma.
        """
        if not self._avaliacao:
            return 'Sem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media