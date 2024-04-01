import numpy as np

from mynympy import Matrix

if __name__ == '__main__':
    np.random.seed(0)

    a = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    b = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    with open('artifacts/3.1/matrix_add.txt', 'w') as f:
        (a + b).dump(f)

    with open('artifacts/3.1/matrix_mul.txt', 'w') as f:
        (a * b).dump(f)

    with open('artifacts/3.1/matrix_matmul.txt', 'w') as f:
        (a @ b).dump(f)
