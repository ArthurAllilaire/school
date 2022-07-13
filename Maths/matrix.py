# Program to multiply two matrices (vectorized implementation)

# Program to multiply two matrices (vectorized implementation)
import numpy as np
matrices = {
    "A": [[0, 1],
          [1, 0]],
    "E": [[1, 0],
          [0, -1]],
    "G": [[-1, 0],
          [0, -1]],
    "T": [[0, -1],
          [1, 0]],
    "R": [[0, 1],
          [-1, 0]],
    "N": [[0, -1],
          [-1, 0]],
    "I": [[1, 0],
          [0, 1]],
    "L": [[-1, 0],
          [0, 1]],
}

changes = ["TRIANGLE",
           "INTEGRAL",
           "RELATING",
           "TRAIL",
           "RATING",
           "GRATIN"]
# take a 3x3 matrix


def matrix_multiplier(matrices, multiplications):
    if len(multiplications) == 2:
        # Multiply the result by i and make it the new result
        result = np.matmul(matrices[multiplications[0]],
                           matrices[multiplications[1]])

        return result

    # Go through the string backwards
    for i in range(len(multiplications)-1, 0, -1):
        # If this is not the first multiplication
        if i == len(multiplications)-1:
            # Multiply the two bottom ones together
            result = matrices[multiplications[i]]
        else:

            # Multiply the result by i and make it the new result
            result = np.matmul(result,
                               matrices[multiplications[i]])

    return result


# Test --> should output [[0, 1], [1, 0]]
# print(matrix_multiplier(matrices, "IA"))

# CODE TO GO THROUGH THE CHANGES
for change in changes:
    result = matrix_multiplier(matrices, change)
    for k, v in matrices.items():
        # print(np.array_equal(result, v))
        if np.array_equal(result, v):
            print(change, k)
vals1 = "ELAN"
vals2 = "TGRELAN"
for char1 in vals1:
    for char2 in vals2:
        result = matrix_multiplier(matrices, char1+char2)
        for k, v in matrices.items():
            # print(np.array_equal(result, v))
            if np.array_equal(result, v):
                print(char1+char2, k)
