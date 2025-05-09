import numpy as np

# Declare a list
a = [1,2,3,4,5]
print(f"Variable a: {a}, {type(a)}")

# create a numpy array
b = np.array(a)
print(f"Variable b: {b}, Type: {type(b)}")

# Check dim and shape of array
print(b.ndim)
print(b.shape)