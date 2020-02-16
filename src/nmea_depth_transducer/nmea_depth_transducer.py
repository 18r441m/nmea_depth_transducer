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

    nmea_sentence = None
    nmea_object = None
    def __init__(self):
        """Initialization to get the NMEA0183 sentences."""
        raise NotImplementedError

    def _parse_nmea_sentence(self):
        """Parse NMEA0183 sentence."""
        self.nmea_object = pynmea2.parse(self.nmea_sentence)
