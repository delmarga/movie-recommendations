import numpy as np

ratings = np.array([
    5,
    2,
    3,
    3,
    4,
    5,
    5,
    1,
    5,
    1,
    3,
    4
])

# Convert to a 10 point ratings using NumPy
ratings = ratings * 2
print(ratings)
