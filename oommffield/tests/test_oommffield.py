import os
import pytest
import random
import numpy as np
from oommffield import Field, read_oommf_file
import matplotlib


class TestField(object):
    def setup(self):
        self.vector_fs = self.create_vector_fs()
        self.constant_values = [0, -5., np.pi,
                                1e-15, 1.2e12, random.random()]
        self.tuple_values = [(0, 0, 1),
                             (0, -5.1, np.pi),
                             [70, 1e15, 2*np.pi],
                             [5, random.random(), np.pi],
                             np.array([4, -1, 3.7]),
                             np.array([2.1, 0.0, -5*random.random()])]

    def create_vector_fs(self):
        cmin_list = [(0, 0, 0), (-5, -8, -10), (10, -5, -80)]
        cmax_list = [(5, 8, 10), (11, 4, 4), (15, 10, 85)]
        d_list = [(1, 1, 1), (1, 2, 1), (5, 5, 2.5)]

        vector_fs = []
        for i in range(len(cmin_list)):
            f = Field(cmin_list[i], cmax_list[i], d_list[i], dim=3)
            vector_fs.append(f)

        return vector_fs

    def test_write_read_oommf_file(self):
        tol = 1e-12
        filename = 'test_write_oommf_file.omf'
        value = (1e-3 + np.pi, -5, 6)
        for f in self.vector_fs:
            f.set(value)
            f.write_oommf_file(filename)

            f_loaded = read_oommf_file(filename)

            assert f.cmin == f_loaded.cmin
            assert f.cmax == f_loaded.cmax
            assert f.d == f_loaded.d
            assert f.d == f_loaded.d
            assert np.all(abs(f.f - f_loaded.f) < tol)

            os.system('rm {}'.format(filename))
