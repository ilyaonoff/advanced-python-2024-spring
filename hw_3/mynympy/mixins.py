from . import validation


class DumpMixin:
    def dump(self, f):
        for row in self.values:
            f.write(' '.join(str(value) for value in row) + '\n')

    @classmethod
    def load(cls, f):
        values = []
        for line in f.readlines():
            values.append(list(int(value) for value in line.strip().split(' ')))
        return cls(values)


class StrMixin:
    def __str__(self):
        result = []
        result.extend([
            f'Shape: {self.rows}x{self.columns}',
            'Data:'
        ])
        for row in self.values:
            result.append(' '.join(str(value) for value in row))
        return '\n'.join(result)


class PropertyMixin:
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, new_values):
        validation.validate(len(new_values), len(new_values[0]), new_values)
        self._values = new_values
        self._rows = len(new_values)
        self._columns = len(new_values[0])

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns
