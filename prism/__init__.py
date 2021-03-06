# -*- coding: utf-8 -*-

"""
PRISM
=====
A *Probabilistic Regression Instrument for Simulating Models* created by
**Ellert van der Velden** (@1313e).


Short description
-----------------
This package contains the *PRISM* pipeline, an efficient and rapid alternative
to MCMC methods for optimizing and analyzing scientific models.
The *PRISM* package provides two user classes: The :class:`~Pipeline` class and
the :class:`~ModelLink` class.

The :class:`~Pipeline` class provides the user with an environment with all the
tools one needs to utilize the full capabilities of *PRISM*, while the
:class:`~ModelLink` abstract base class allows for any model to be connected to
the *PRISM* pipeline and holds all information about this model.

"""


# %% IMPORTS
# Package imports
from e13tools import compare_versions as _compare_versions
from e13tools.utils import aux_char_set
from mpi4pyd import MPI as _MPI

# PRISM imports
from .__version__ import __version__
from . import emulator, modellink, utils
from ._gui import start_gui
from ._internal import get_bibtex, get_info
from ._pipeline import Pipeline

# All declaration
__all__ = ['emulator', 'modellink', 'utils', 'Pipeline', 'aux_char_set',
           'get_bibtex', 'get_info', 'start_gui']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"


# %% EXECUTE INITIALIZING CODE
# Check if MPI is being used and perform some checks on controller if size > 1
if(_MPI.__package__ == 'mpi4py' and _MPI.COMM_WORLD.Get_size() > 1 and
   _MPI.COMM_WORLD.Get_rank() == 0):  # pragma: no cover
    # Check if imported mpi4py package is at least 3.0.0
    from mpi4py import __version__ as _mpi4py_version
    if not _compare_versions(_mpi4py_version, '3.0.0'):
        raise ImportError("mpi4py v%s detected. PRISM requires mpi4py "
                          "v3.0.0 or later to work in MPI!"
                          % (_mpi4py_version))
