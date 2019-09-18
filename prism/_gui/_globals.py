# -*- coding utf-8 -*-

"""
GUI Globals
===========
Provides a collection of all global variables for the Projection GUI that must
be available.

"""


# %% IMPORTS
# Package imports
from os import path

# All declaration
__all__ = ['APP_NAME', 'DIR_PATH']


# %% GUI GLOBALS
APP_NAME = "PRISM Projection Viewer"                # Name of application
DIR_PATH = path.abspath(path.dirname(__file__))     # Path to GUI directory
