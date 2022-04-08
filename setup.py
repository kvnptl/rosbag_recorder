#!/usr/bin/env python3

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rosbag_recorder'],
    package_dir={'rosbag_recorder': 'ros/src/rosbag_recorder'}
)

setup(**d)
