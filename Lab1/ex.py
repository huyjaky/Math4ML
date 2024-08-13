import numpy as np
import matplotlib.pyplot as plt

A = np.arange(stop=10)  # pyright: ignore[]

# NOTE: ex1
for element_location in range(len(A)):
    A[element_location] = np.random.randint(-21, 21)  # ID = 21

# NOTE: ex2
A = np.sort(A)

# NOTE: ex3
plt.plot(A,2*A+1, label='2*x+1')
plt.plot(A,A*A, label='x^2') 

plt.show()

print(A)
