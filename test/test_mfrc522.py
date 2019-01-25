'''
Created on Jan 14, 2019

@author: asiate
'''
import logging
import sys
import unittest

import unittest.mock as mock


# Mock RPi.GPIO and spidev
sys.modules['RPi'] = mock.MagicMock()
sys.modules['RPi.GPIO'] = mock.MagicMock()
sys.modules['spidev'] = mock.MagicMock()

# After mocking libraries import the system under test (sut)
from mfrc522 import MFRC522

logging.basicConfig(level=logging.DEBUG)

class TestMFRC522(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test__spi_transfer(self):
        # arrange
        sut = MFRC522()
        sut.spi.xfer2 = mock.MagicMock(return_value=[125,6,6,0])
        data = [1,2,3]
        
        # act
        actual = sut._spi_transfer(data)
        
        # assert


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestMFRC522.testName']
    unittest.main()