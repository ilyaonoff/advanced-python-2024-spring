import numbers

import numpy as np

from .mixins import PropertyMixin, StrMixin, DumpMixin


class MixinedMatrix(PropertyMixin, StrMixin, DumpMixin, np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, values):
        super().__init__()
        self.values = values

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MixinedMatrix,)):
                return NotImplemented()

        inputs = tuple(np.asarray(x.values) if isinstance(x, MixinedMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.values if isinstance(x, MixinedMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)
