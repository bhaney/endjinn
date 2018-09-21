import numpy as np
from endjinn.state_block import Series


def test_series():
    s = Series([100, 101, 102, 103, 111, 108, 115, 132, 104])
    mean = s.get_mean()
    variance = s.get_variance()
    std = s.get_standard_deviation()
    dispersion = s.get_dispersion_index()
    assert np.isclose(mean, 108.444444)
    assert np.isclose(variance, 91.35802469135803)
    assert np.isclose(std, 9.558139185602919)
    assert np.isclose(dispersion, 0.8424408014571949)

    val = s.get_and_tick()
    assert s.index == 1
    assert val == 100

    slc = s.get_slice(2, 5)
    assert slc == [102, 103, 111]
