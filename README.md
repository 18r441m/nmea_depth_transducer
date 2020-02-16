# nmea_depth_transducer

Driver for NMEA0183 depth transducers, which interface with the computer via RS232.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

[Dartmouth Reality and Robotics Lab](http://rlab.cs.dartmouth.edu/home/)

Authors: [Alberto Quattrini Li](https://sites.google.com/view/albertoq) - Dartmouth College.

## Installation

After configuring the hardware, the following will set the environment to make the ROS driver running.
`nmea_depth_transducer` has been tested under ROS kinetic and Ubuntu 16.04, and ROS melodic and Ubuntu 18.04. This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.

### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics),
- [pynmea2](https://pypi.org/project/pynmea2/) Library for NMEA 0183 protocol. E.g., in Ubuntu,
 
		sudo apt install python-nmea2


### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd catkin_workspace/src
	git clone https://github.com/dartmouthrobotics/nmea_depth_transducer.git
	cd ../
	catkin_make


## Usage
You can run the node with (the default values are for the serial)

	roslaunch nmea_depth_transducer nmea_depth_transducer.launch

Currently, this package has been tested with a CruzPro ATU120AT interfaced with a serial to USB.

See:
* [CruzPro ATU120](http://www.cruzpro.co.nz/active.html)


## Nodes

### nmea_depth_transducer_node

Publishes depth and temperature measurements of the depth transducer.


#### Published Topics

* **`<sensor_name>/nmea_raw`** ([nmea_msgs/Sentence])

	NMEA0183 raw message.

* **`<sensor_name>/depth`** ([sensor_msgs/Range])

	Depth values in meters.

* **`<sensor_name>/temperature`** ([sensor_msgs/Temperature])

	Temperature in Celsius.



