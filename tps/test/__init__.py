from unittest import TestSuite

import test_tps

def test_suite():
    suite = TestSuite()
    suite.addTest(test_tps.test_suite())
    return suite

