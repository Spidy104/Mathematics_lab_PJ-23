import numpy as np

I = np.array([[25, 1, 2], [1, 3, 0], [2, 0, -4]])
print("The given matrix is:")
print(I)
w, v = np.linalg.eig(I)
print("Eigen values: ", w)
print("Eigen vectors")
print(v)
