import numpy as np

#2 numpy exercises 

#a
a = np.zeros(10)
a[4] = 1
print(a)
#b
b = np.random.randint(10,49, 100)
print(b)

#c
c = np.flip(b)
print(c)


#d

d = np.random.random((3,3))*8
print(d)

#e

e = np.array([1,2,0,0,4,0])

print(np.where(e != 0))


#f
print("f")
f = np.random.random(30)
print(f)
print(f.mean())



#g
print("g")

g = np.zeros((10,10))
g[0,:] = g[9,:] = 1
g[:, 0] = g[:, 9] = 1

print(g)


#h
print("h")
ha = np.arange(8).reshape(8,1)
hb = np.arange(8).reshape(1,8)
h = ha+hb

print(h % 2)


#i

print("i")

#i = np.tile(np.array([0,1]), 8*4).reshape(8,8)
#print(i)

i = np.tile(np.array([[0,1],[1,0]]), (4,4))#.reshape(8,8)
print(i)


#j
print("j")

j = np.random.random(10)*10
print(j)

j[((j > 3) & (j < 8))] *= -1

print(j)


#k
print("k")
Z = np.random.random(10)*10
Z.sort()
print(Z)


#L
print("L")

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.all(A==B)
print(equal)

#M
print("M")

Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z*Z.T
print(Z.dtype)
print(Z)


#N

print("N")

A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
indices = np.arange(C.shape[0])
print(indices)
D = C[indices, indices]
print(C)
print(D)
