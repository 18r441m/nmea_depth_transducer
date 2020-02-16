# -*- coding: utf-8 -*-
"""NMEA0183 depth transducer driver.

Reading values following the NMEA 0183 standard.

More details at:
.. CruzPro guide:
   http://www.cruzpro.com/active.html

"""

import pynmea2

from default_values import *

class NmeaDepthTransducer(object):
    """Base class for reading the NMEA0183 depth transducer data.
    """

    def __init__(self):
        """Initialization to get the NMEA0183 sentences."""
        self.nmea_sentence = None
        self.nmea_object = None

    def parse_nmea_sentence(self):
        """Parse NMEA0183 sentence."""
        self.nmea_object = pynmea2.parse(self.nmea_sentence)
