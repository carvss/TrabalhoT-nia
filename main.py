'''
Multiplicação de matrizes
'''

print("Botões         Camisa A    Camisa B    Camisa C"
      "\n---------------------------------------------"
      "\nBotões p        3           1         3"
      "\nBotões g        6           5         5 \n")


print("                Maio        Junho"
      "\n----------------------------------"
      "\nCamisa A        100         50"
      "\nCamisa B        50          100"
      "\nCamisa C        50          50 \n")


matrizA = [[3, 1, 3],
           [6, 5, 5]]

matrizB = [[100, 50],
          [50, 100],
          [50, 50]]

# MatrizA 2x3 * MatrizB 3x2, condição verdade: C MatrizA = L MatrizB -> Matriz resultante = LMatrizA x CMatrizB: Matriz 2x2
# C -> Coluna, L -> Linha

result = [[0, 0],
          [0, 0]]

# Jeito comum:

def multiplica1():
    matrizA = [[3, 1, 3],
               [6, 5, 5]]

    matrizB = [[100, 50],
               [50, 100],
               [50, 50]]
    
    result = [[0, 0],
              [0, 0]]
    
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            for k in range(len(matrizB)):
                result[i][j] += matrizA[i][k] * matrizB[k][j]

    for r in result:
        print(r)


multiplica1()

# Usando numpy
def multilica2():
    import numpy as np


    matrizA = [[3, 1, 3],
               [6, 5, 5]]

    matrizB = [[100, 50],
               [50, 100],
               [50, 50]]

    result = [[0, 0],
              [0, 0]]

    result = np.dot(matrizA, matrizB)

    for r in result:
        print(r)

#multiplica2() -> Descomentar se tiver instalado o numpy: pip instal numpy
