# Program to multiply two matrices using nested loops
import random
import numpy as np

#class matrix:
#    def __init__(self):
#        pass

    

def generate_square_matrix(N=250):
    #N = 250
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])

    return X


def generate_random_matrix(N, M):
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(M)])

    return Y


def zeroes(N, M):
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (M))
    return result

def mul(X, Y):
    return np.dot(np.array(X), np.array(Y))
    result = zeroes(len(X), len(Y[0]))
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            result[i] = [X[i][k] * Y[k][j] for k in range(len(Y))]
            #for k in range(len(Y)):
            #    result[i][j] += X[i][k] * Y[k][j]
    return result


for a in range(4):
    X = generate_square_matrix(250)
    Y = generate_random_matrix(250, 251)

    result = mul(X,Y)

for r in result:
    print(r)
