# Copyright (c) 2011, Omniscale GmbH & Co. KG
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import unittest

from tps import TPS, TPSError, from_control_points

class TestTPS(unittest.TestCase):
    def test_init_from_list(self):
        t = TPS([(0, 0, 50, 50), (10, 10, 100, 100)])
        self.assertEqual(t.transform(4, 5), (72.5, 72.5))
        t.add(0, 10, 70, 100)
        self.assertEqual(t.transform(4, 5), (72.0, 75.0))
    
    def test_simple(self):
        t = TPS()
        t.add(0, 0, 50, 50)
        t.add(10, 10, 100, 100)
        self.assertEqual(t.transform(4, 5), (72.5, 72.5))
        t.add(0, 10, 70, 100)
        self.assertEqual(t.transform(4, 5), (72.0, 75.0))
    
    def test_no_points(self):
        try:
            t = TPS()
            t.transform(0, 0)
        except TPSError:
            pass
        else:
            assert False
    
    def test_from_control_points_list(self):
        t = from_control_points([
            (0, 0, 50, 50),
            (10, 10, 100, 100),
            (0, 10, 70, 100)])
        
        self.assertEquals(t.transform(4, 5), (72.0, 75.0))

    def test_from_control_points_list_backwards(self):
        t = from_control_points([
            (0, 0, 50, 50),
            (10, 10, 100, 100),
            (0, 10, 70, 100)],
            backwards=True)
        
        results = t.transform(72, 75)
        self.assertAlmostEqual(results[0], 4.0)
        self.assertAlmostEqual(results[1], 5.0)

def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestTPS)

if __name__ == '__main__':
    unittest.main()
