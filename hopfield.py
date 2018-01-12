import numpy as np
data = [[0,1,0,
         1,0,1,
         0,1,0],
        [0,1,0,
         1,1,1,
         0,1,0],
        [1,0,1,
         0,1,0,
         1,0,1]]
size = len(data[0])
data = np.array(data)
N = len(data)

X = [1,0,1,
     0,1,1,
     1,0,1]
X = np.array(X)

def learning(data, size):
  w = np.zeros((size,size))
  for i in range(len(w)):
    w[i][i] = 0
    for j in range(i+1,len(w)):
      tmp = 0
      for n in range(N):
        tmp += (2*data[n][i]-1)*(2*data[n][j]-1)
      w[i][j] = tmp
      w[j][i] = tmp
  return w

w = learning(data, size)
print("w:")
print(w)

def recognizing(x):
  loop = 10
  for i in range(loop):
    Epre = energy(w,x)
    x1 = np.sign(w.dot(x))
    Eafter = energy(w,x1)
    if (np.abs(Epre - Eafter) < 0.0001):
      return x
    x = x1
  return x

def energy(w, x):
  return -0.5*(np.dot(np.dot(x,w),x))

print(recognizing(X))
