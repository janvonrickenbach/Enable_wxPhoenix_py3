#  Copyright (c) 2007-2014 by Enthought, Inc.
#  All rights reserved.
""" A multi-platform object drawing library.
    Part of the Enable project of the Enthought Tool Suite.
"""
from ._version import full_version as __version__

__requires__ = ['numpy', 'traits==4.7.0+ansys.ch', 'traitsui==5.2.0+ansys.ch', 'pyface==5.2.0+ansys.ch', 'six', 'fonttools']

# Do not force installation of pillow if PIL is already available.
try:
    import PIL
except ImportError:
    __requires__.append('pillow')
