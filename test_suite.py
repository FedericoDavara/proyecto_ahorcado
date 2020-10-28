import unittest
from test_ahorcado import TestAhorcado
from test_partida import TestPartida 

def suite():

    """
        Gather all the tests from this module in a test suite.
    """

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestAhorcado))
    test_suite.addTest(unittest.makeSuite(TestPartida))
    return test_suite
if __name__ == "__main__":

    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)