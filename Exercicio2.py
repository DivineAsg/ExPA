# Classe para representar um produto
class Produto:

    # Método construtor da classe
    def __init__(self, nome, preco):

        self.nome = nome  # Guarda o nome do produto

        self.preco = preco  # Guarda o preço do produto


produtos = []  # Lista que armazenará todos os produtos


# Função responsável por cadastrar produtos
def cadastrar_produto():

    try:  # Tenta executar o código abaixo

        nome = input("Digite o nome do produto: ")  # Solicita o nome do produto

        preco = float(input("Digite o preço do produto: R$ "))  # Solicita o preço e converte para float

        if preco <= 0:  # Verifica se o preço é inválido

            print("Preço inválido!")  # Exibe mensagem de erro

            return  # Encerra a função

        novo_produto = Produto(nome, preco)  # Cria um objeto da classe Produto

        produtos.append(novo_produto)  # Adiciona o produto na lista

        print("Produto cadastrado com sucesso!")  # Mensagem de sucesso

    except ValueError:  # Captura erro caso o usuário digite texto no preço

        print("Erro: Digite um valor numérico válido!")  # Mensagem de erro


# Função para listar os produtos cadastrados
def listar_produtos():

    if len(produtos) == 0:  # Verifica se não há produtos cadastrados

        print("Nenhum produto cadastrado.")  # Exibe mensagem

        return  # Encerra a função

    print("\n=== LISTA DE PRODUTOS ===")  # Título da listagem

    for indice, produto in enumerate(produtos):  # Percorre a lista mostrando índice e produto

        print(f"{indice} - {produto.nome} - R$ {produto.preco:.2f}")  # Exibe os dados do produto


# Função para comprar um produto
def comprar_produto():

    try:  # Tenta executar o código

        if len(produtos) == 0:  # Verifica se existem produtos cadastrados

            print("Não existem produtos cadastrados.")  # Exibe mensagem

            return  # Encerra a função

        listar_produtos()  # Mostra os produtos disponíveis

        indice = int(input("\nDigite o número do produto: "))  # Solicita o índice do produto

        if indice < 0 or indice >= len(produtos):  # Verifica se o índice existe

            print("Produto inexistente!")  # Exibe mensagem de erro

            return  # Encerra a função

        quantidade = int(input("Digite a quantidade: "))  # Solicita a quantidade

        if quantidade <= 0:  # Verifica se a quantidade é inválida

            print("Quantidade inválida!")  # Exibe mensagem

            return  # Encerra a função

        produto = produtos[indice]  # Obtém o produto escolhido

        total = produto.preco * quantidade  # Calcula o valor total

        print("\nResumo da compra")  # Exibe título

        print(f"Produto: {produto.nome}")  # Mostra o nome do produto

        print(f"Quantidade: {quantidade}")  # Mostra a quantidade

        print(f"Total a pagar: R$ {total:.2f}")  # Mostra o total da compra

    except ValueError:  # Captura erro caso digite letras

        print("Erro: Digite apenas números!")  # Exibe mensagem de erro

    except IndexError:  # Captura erro de índice inexistente

        print("Erro: Índice inexistente!")  # Exibe mensagem de erro


# Loop principal do sistema
while True:

    print("\nSistema de cadastro e compra")  # Exibe título do sistema

    print("1 - Cadastrar produto")  # Opção 1

    print("2 - Listar produtos")  # Opção 2

    print("3 - Comprar produto")  # Opção 3

    print("4 - Sair")  # Opção 4

    opcao = input("Escolha uma opção: ")  # Solicita a opção do usuário

    if opcao == "1":  # Verifica se escolheu cadastrar produto

        cadastrar_produto()  # Chama a função de cadastro

    elif opcao == "2":  # Verifica se escolheu listar produtos

        listar_produtos()  # Chama a função de listagem

    elif opcao == "3":  # Verifica se escolheu comprar produto

        comprar_produto()  # Chama a função de compra

    elif opcao == "4":  # Verifica se escolheu sair

        print("Encerrando o sistema...")  # Mensagem de encerramento

        break  # Encerra o loop

    else:  # Caso escolha uma opção inválida

        print("Opção inválida!")  # Exibe mensagem de erro
