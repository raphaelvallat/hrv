# conding: utf-8
import unittest

import numpy as np

from hrv.io import read_from_text
from hrv.utils import (_interp_cubic_spline,
                       _interp_linear,
                       _create_interp_time)

FAKE_RRI = [800, 810, 815, 750]
# TODO: recreate tests from files with errors


class InterpolationTestCase(unittest.TestCase):
    def setUp(self):
        self.real_rri = read_from_text('tests/test_files/real_rri.txt')

    def test_create_interp_time(self):
        time = [0, 1]

        expected = np.array([0, 0.25, 0.5, 0.75, 1.0])
        interp_time = _create_interp_time(time, 4.0)

        np.testing.assert_equal(interp_time, expected)

    def test_interpolate_rri_spline_cubic(self):
        rri = [800, 810, 790, 815]
        time = [0, 1, 2, 3]
        sf = 4.0

        rrix = _interp_cubic_spline(rri, time, sf)
        expected = [
            800., 809.4140625, 813.4375, 813.2421875, 810.,
            804.8828125, 799.0625, 793.7109375, 790., 789.1015625,
            792.1875, 800.4296875, 815.
        ]

        np.testing.assert_array_almost_equal(rrix, expected)

    def test_interpolate_rri_spline_linear(self):
        rri = [800, 810, 790, 815]
        time = [0, 1, 2, 3]
        sf = 4.0

        rrix = _interp_linear(rri, time, sf)
        expected = [
            800., 802.5, 805., 807.5, 810., 805., 800., 795., 790., 796.25,
            802.5, 808.75, 815.
        ]

        np.testing.assert_array_almost_equal(rrix, expected)
