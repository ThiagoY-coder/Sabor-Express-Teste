from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Thiago', 10)
restaurante_praca.receber_avaliacao('Jorge', 4)
restaurante_praca.receber_avaliacao('Yngrid', 8)
"""
O código acima cria uma instancia da classe Restaurante chamada restaurante_praca, com o nome 'praça' e a categoria 'gourmet'. Em seguida, são adicionada três avaliações ao resturante, sendo a primeira e a ultima invalida pois esta acima da nota maxima de 5, e a segunda é valida pois está dentro do intervalo permitido.
"""
restaurante_praca.alternar_status()
"""
O código acima altera o status do restaurante para ativo, pois ele inicia como inativo por padrão.
"""

def main():
    Restaurante.listar_restaurantes()

"""
A função main() é responsalvel por dizer ao programa tudo que deve ser feito no programa, nesse caso, ela chama a função listar_restaurantes() da classe Restaurante, que exibe no console a lista de restaurantes cadastrados e outros dados dos restaurantes.
"""
if __name__ == '__main__':
    main()

"""
A condicional if __name__ == '__main__': é utilizada para garantir que a função main() seja executada apenas quando o arquivo app.py for executado diretamente, e não quando ele for importado como um módulo em outro arquivo.
"""