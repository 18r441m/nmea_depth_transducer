#!/usr/bin/env python
"""Unit test for NmeaDepthTransducer."""

import unittest

from nmea_depth_transducer.nmea_depth_transducer_serial \
    import NmeaDepthTransducer

class CaseDepth(unittest.TestCase):
    """Test for a depth sentence."""

    def runTest(self):
        nmea_sentence = "$SDDBT,008.8,f,002.7,M,001.4,F*06"
        depth_transducer = NmeaDepthTransducer()
        depth_transducer.nmea_sentence = nmea_sentence
        depth_transducer.parse_nmea_sentence()

        from pynmea2.types.talker import DBT # Depth.
        self.assertTrue(isinstance(depth_transducer.nmea_object, DBT))

class CaseTemperature(unittest.TestCase):
    """Test for a temperature sentence."""

    def runTest(self):
        nmea_sentence = "$SDMTW,025.5,C*36"
        depth_transducer = NmeaDepthTransducer()
        depth_transducer.nmea_sentence = nmea_sentence
        depth_transducer.parse_nmea_sentence()

        # do some things to my_var which might change its value...
        from pynmea2.types.talker import MTW # Temperature.
        self.assertTrue(isinstance(depth_transducer.nmea_object, MTW))

class NmeaTestSuite(unittest.TestSuite):
    """Test a set of sentences."""

    def __init__(self):
        super(NmeaTestSuite, self).__init__()
        self.addTest(CaseDepth())
        self.addTest(CaseTemperature())

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('nmea_depth_transducer', 'test_nmea', NmeaTestSuite)


    import rostest
    rostest.rosrun('nmea_depth_transducer', 'test_nmea', NmeaTestSuite)
