# importamdo as bibliotecas necessárias
import tensorflow as tf
import pandas as pd 

from sklearn.datasets import load_iris #
from sklearn.model_selection import train_test_split #
from sklearn.preprocessing import StandardScaler 

#carreganso o cojunto de dados Iris 
iris = load_iris()

# separando as caracteristicas e os resutados 
x = iris.data
y = iris.target

print("dados caregados com sucesso")
print("quantidade de amostra ", len (x))

 #mostrando as primeiras caracteristicads 
print(x[:5])

# Mostrando as primeiras classificaçãos
print(y[:5])

# dividindo os dados em treinamento de teste
x_treino, x_teste, y_treino , y_teste = train_test_split(x,y,test_size=0.2,random_state=42)

print("dados de treinamento", len(x_treino))
print( "dados de teste", len(x_teste))

# criando o normalizador 
scaler = StandardScaler()
scaler.fit(x_treino)
x_treino = scaler.transform(x_treino)
x_teste = scaler.transform(x_teste)
print("dados normalizados com sucesso")

# criando o modelo de rede neural
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu", input_shape=(4,)),
     tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")

    
])

#mostrando a estrutura de dados do modelo
modelo.summary()

# configurando o modelo para o treinamento 
modelo.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("modelo configurado com sucesso ")
# treinando o modelo 
historico = modelo.fit(
    x_treino,
    y_treino,
    epochs=50,
    batch_size=10,
    verbose=1
)
# avaliando o modelo com os dados de teste 
perda, acuracia = modelo.evaluate(x_teste,y_teste, verbose=0)
print("perda", perda)
print("acuracia", acuracia)
print(f"acuracia:{acuracia * 100:.2f}%")

#fazendo previsões com o modelo treinado
previsoes = modelo.predict(x_teste)
classes_previstas = previsoes.argmax(axis=1)
print("classes previstas:")
print(classes_previstas)

print("\nclasses reais:")
print(y_teste)

# mostrando alguns resutados com os nomes dsa especies 
for i in range(10):
    print(
        "prevista:", iris.target_names[classes_previstas[i]],
        "| real:", iris.target_names[y_teste[i]]
    )

