import numpy as np

from mynympy import MixinedMatrix

if __name__ == '__main__':
    np.random.seed(0)

    a = MixinedMatrix(np.random.randint(0, 10, (10, 10)).tolist())
    b = MixinedMatrix(np.random.randint(0, 10, (10, 10)).tolist())

    with open('artifacts/3.2/matrix_add.txt', 'w') as f:
        (a + b).dump(f)

    with open('artifacts/3.2/matrix_mul.txt', 'w') as f:
        (a * b).dump(f)

    with open('artifacts/3.2/matrix_matmul.txt', 'w') as f:
        (a @ b).dump(f)
