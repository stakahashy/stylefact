import numpy as np
from numpy.testing import assert_allclose,assert_almost_equal,assert_array_equal,assert_equal
import sys
sys.path.append('..')
import finance


def test_gaussian():
    series = np.random.normal(size=100000)



