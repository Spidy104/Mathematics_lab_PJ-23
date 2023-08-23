import numpy as np

I = np.array([[25, 1], [1, 3]])
w, v = np.linalg.eig(I)

print("Eigen values: ", w)
print("Eigen Vectors")
print(v)
