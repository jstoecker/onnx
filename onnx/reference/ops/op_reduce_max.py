# SPDX-License-Identifier: Apache-2.0
# pylint: disable=E1123,W0221

import numpy as np

from ._op import OpRunReduceNumpy


class ReduceMax_1(OpRunReduceNumpy):
    def _run(self, data, axes=None, keepdims=None):  # type: ignore
        axes = tuple(axes) if axes is not None else None
        return (np.maximum.reduce(data, axis=axes, keepdims=keepdims == 1),)


class ReduceMax_18(OpRunReduceNumpy):
    def _run(self, data, axes=None, keepdims=1, noop_with_empty_axes=0):  # type: ignore
        if self.is_axes_empty(axes) and noop_with_empty_axes != 0:  # type: ignore
            return (data,)

        axes = self.handle_axes(axes)
        keepdims = keepdims != 0  # type: ignore
        return (np.maximum.reduce(data, axis=axes, keepdims=keepdims),)
