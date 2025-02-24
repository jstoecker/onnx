# SPDX-License-Identifier: Apache-2.0
# pylint: disable=W0221

import numpy as np

from ._op import OpRunUnaryNum


class Exp(OpRunUnaryNum):
    def _run(self, x):  # type: ignore
        return (np.exp(x).astype(x.dtype),)
