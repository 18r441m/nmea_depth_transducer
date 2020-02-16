# -*- coding: utf-8 -*-
"""RS232 Driver for the NMEA0183 depth sensor.

Reading values following the NMEA 0183 standard.

More details at:
.. CruzPro guide:
   http://www.cruzpro.com/active.html

"""

import pynmea2
import serial
import time

from default_values import *
from nmea_depth_transducer import NmeaDepthTransducer

class NmeaDepthTransducerSerial(NmeaDepthTransducer):
    """Interface for reading the NMEA0183 depth sensor data through RS232.

    Attributes:
        serial (serial.Serial): serial port object.
    """

    def __init__(self, serial_port=SERIAL_PORT, baudrate=BAUDRATE):
        """Initialization of the serial port and parameters."""

        super(NmeaDepthTransducerSerial, self).__init__()

        # Initialization of the serial port.
        self.serial = serial.Serial(serial_port, baudrate,
            timeout=SERIAL_TIMEOUT)
        time.sleep(1)

    def read_data(self):
        """Reading a NMEA0183 sentence."""
        if self.serial.inWaiting() > 0:
            # Read from sensor.
            self.nmea_sentence = self.serial.readline()
            try:
                self.parse_nmea_sentence()
            except pynmea2.nmea.ParseError as e:
                return None

            return self.nmea_object
