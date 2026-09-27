#importa a biblioteca matplotlib para criar gráficos
import matplotlib.pyplot as plt

# classe Livro para representar os livros cadastrados
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

# lista que armazenará os livros cadastrados
livros = []
# Livros já cadastrados
livros.append(Livro("Harry Potter", "J.K. Rowling", "Fantasia", 5))
livros.append(Livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 3))
livros.append(Livro("Dom Casmurro", "Machado de Assis", "Romance", 4))
livros.append(Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Aventura", 6))
livros.append(Livro("1984", "George Orwell", "Ficção", 2))

#função para cadastrar um novo livro
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade de exemplares: "))

    novo_livro = Livro(titulo, autor, genero, quantidade)

    livros.append(novo_livro)

    print("Livro cadastrado com sucesso!")

# função para listar todos os livros cadastrados
def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        print("\n--- Lista de livros cadastrados ---")

        for livro in livros:
            print(
                f"Título: {livro.titulo}, "
                f"Autor: {livro.autor}, "
                f"Gênero: {livro.genero}, "
                f"Quantidade: {livro.quantidade}"
            )

# função para buscar um livro pelo título
def buscar_livro():
    titulo_busca = input("Digite o título do livro que deseja buscar: ")

    for livro in livros:
        if livro.titulo.lower() == titulo_busca.lower():
            print("\nLivro encontrado!")
            print("Título:", livro.titulo)
            print("Autor:", livro.autor)
            print("Gênero:", livro.genero)
            print("Quantidade disponível:", livro.quantidade)
            return

    print("Livro não encontrado.")

#função para gerar um gráfico de barras com a quantidade de livros por gênero
def gerar_grafico():
    generos = {}

    for livro in livros:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade

    plt.bar(generos.keys(), generos.values())
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de livros")
    plt.title("Quantidade de livros por gênero")
    plt.show()


# Programa principal

cadastrar_livro()
listar_livros()
buscar_livro()
gerar_grafico()