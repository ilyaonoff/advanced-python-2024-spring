from . import validation
from . import mixins


class Matrix(mixins.DumpMixin):
    @staticmethod
    def _check_type_compatible(other):
        if not isinstance(other, Matrix):
            raise ValueError(f'{type(other)} cannot be added to matrix')

    def __init__(self, values):
        super().__init__()
        self._rows = len(values)
        self._columns = len(values[0])
        self._values = values

        validation.validate(self._rows, self._columns, self._values)

    @property
    def values(self):
        return self._values

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def __add__(self, other):
        self._check_type_compatible(other)

        if self._rows != other._rows or self._columns != other._columns:
            raise ValueError('Incorrect matrix shape')

        result = []
        for rows in zip(self._values, other._values):
            result.append(
                list(map(lambda x: x[0] + x[1], zip(*rows)))
            )

        return Matrix(result)

    def __mul__(self, other):
        self._check_type_compatible(other)

        if self._rows != other._rows or self._columns != other._columns:
            raise ValueError('Incorrect matrix shape')

        result = []
        for rows in zip(self._values, other._values):
            result.append(
                list(map(lambda x: x[0] * x[1], zip(*rows)))
            )

        return Matrix(result)

    def __matmul__(self, other):
        self._check_type_compatible(other)

        if self._columns != other._rows:
            raise ValueError('Incorrect matrix shape')

        result = []
        for i in range(self._rows):
            result_row = []
            for j in range(other._columns):
                result_value = self._values[i][0] * other._values[0][j]
                for k in range(1, self._columns):
                    result_value += self._values[i][k] * other._values[k][j]
                result_row.append(result_value)
            result.append(result_row)

        return Matrix(result)
