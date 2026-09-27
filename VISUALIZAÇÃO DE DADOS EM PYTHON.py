# Importando as bibliotecas
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Conectando ao banco de dados SQLite
conexao = sqlite3.connect('dados_vendas.db')

# Criando um cursor
cursor = conexao.cursor()


# Criando a tabela de vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda TEXT,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL,
    quantidade INTEGER
)
''')


# Inserindo os dados de vendas
cursor.execute('''
INSERT INTO vendas1 
(data_venda, produto, categoria, valor_venda, quantidade)
VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00, 1),
('2023-01-05', 'Produto B', 'Roupas', 350.00, 2),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00, 1),
('2023-03-15', 'Produto D', 'Livros', 200.00, 3),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00, 2),
('2023-04-02', 'Produto F', 'Roupas', 400.00, 2),
('2023-05-05', 'Produto G', 'Livros', 150.00, 1),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00, 1),
('2023-07-20', 'Produto I', 'Roupas', 600.00, 3),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00, 2),
('2023-09-30', 'Produto K', 'Livros', 300.00, 2),
('2023-10-05', 'Produto L', 'Roupas', 450.00, 1),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00, 1),
('2023-12-20', 'Produto N', 'Livros', 250.00, 2)
''')


# Confirmando as alterações
conexao.commit()

print("Dados inseridos com sucesso!")


# Carregando os dados do SQLite em um DataFrame
df_vendas = pd.read_sql_query(
    "SELECT * FROM vendas1",
    conexao
)


# Informações sobre o DataFrame
print("\nInformações do DataFrame:")
df_vendas.info()


# Estatísticas básicas dos valores de venda
print("\nEstatísticas:")
print(df_vendas.describe())


# Verificando valores ausentes
print("\nValores ausentes:")
print(df_vendas.isnull().sum())


# Calculando o total de vendas
total_vendas = df_vendas['valor_venda'].sum()

print(f"\nTotal de vendas: R$ {total_vendas:.2f}")


# Calculando a média das vendas
media_vendas = df_vendas['valor_venda'].mean()

print(f"Média das vendas: R$ {media_vendas:.2f}")


# Total de vendas por categoria
vendas_por_categoria = df_vendas.groupby(
    'categoria'
)['valor_venda'].sum()

print("\nVendas por categoria:")
print(vendas_por_categoria)


# Quantidade de vendas por categoria
quantidade_vendas_por_categoria = df_vendas["categoria"].value_counts()

print("\nQuantidade de vendas por categoria:")
print(quantidade_vendas_por_categoria)


# -----------------------------------
# GRÁFICO DO TOTAL DE VENDAS POR CATEGORIA
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    x=vendas_por_categoria.index,
    y=vendas_por_categoria.values
)

plt.title("Total de Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Total de Vendas (R$)")

plt.show()


# Convertendo a coluna de data para formato de data
df_vendas['data_venda'] = pd.to_datetime(
    df_vendas['data_venda']
)


# -----------------------------------
# GRÁFICO DE VENDAS AO LONGO DO TEMPO
# -----------------------------------

plt.figure(figsize=(10, 5))

sns.lineplot(
    data=df_vendas,
    x='data_venda',
    y='valor_venda',
    marker="o"
)

plt.title("Vendas ao Longo do Tempo")
plt.xlabel("Data da Venda")
plt.ylabel("Valor da Venda (R$)")

plt.xticks(rotation=45)

plt.show()


# -----------------------------------
# GRÁFICO DA QUANTIDADE DE VENDAS
# POR CATEGORIA
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_vendas,
    x="categoria"
)

plt.title("Quantidade de Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de Vendas")

plt.show()


# -----------------------------------
# ENCONTRANDO A MAIOR VENDA
# -----------------------------------

maior_venda = df_vendas.loc[
    df_vendas["valor_venda"].idxmax()
]

print("\nProduto com maior venda:")
print("Produto:", maior_venda["produto"])
print("Categoria:", maior_venda["categoria"])
print("Valor: R$", maior_venda["valor_venda"])


# -----------------------------------
# ENCONTRANDO A MENOR VENDA
# -----------------------------------

menor_venda = df_vendas.loc[
    df_vendas["valor_venda"].idxmin()
]

print("\nProduto com menor venda:")
print("Produto:", menor_venda["produto"])
print("Categoria:", menor_venda["categoria"])
print("Valor: R$", menor_venda["valor_venda"])


# Fechando a conexão com o banco
conexao.close()