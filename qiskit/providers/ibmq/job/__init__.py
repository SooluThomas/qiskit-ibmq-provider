# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
====================================================
IBMQ Provider Job (:mod:`qiskit.providers.ibmq.job`)
====================================================

.. currentmodule:: qiskit.providers.ibmq.job

Module representing IBM Quantum Experience jobs.

Classes
=========

.. autosummary::
    :toctree: ../stubs/

    IBMQJob
    QueueInfo

Exception
=========
.. autosummary::
    :toctree: ../stubs/

    IBMQJobError
    IBMQJobApiError
    IBMQJobFailureError
    IBMQJobInvalidStateError
    IBMQJobTimeoutError
"""

from .ibmqjob import IBMQJob
from .queueinfo import QueueInfo
from .exceptions import (IBMQJobError, IBMQJobApiError, IBMQJobFailureError,
                         IBMQJobInvalidStateError, IBMQJobTimeoutError)
