""" Test Suite
"""

import pytest
from datetime import datetime
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from energy_shaper import group_into_profiled_intervals

PROFILE_A = [0.5, 1.0]

def test_profile_grouping():
    """ Test num of intervals is returned correctly """
    interval_lenghts = [1, 5, 30]
    for interval in interval_lenghts:
        num_intervals = 24 * (60/interval)
        day_read = [(datetime(2017, 1, 1, 0, 0),
                     datetime(2017, 1, 2, 0, 0),
                     num_intervals
                    ),
                    ]
        reads = list(group_into_profiled_intervals(day_read, interval_m=interval,
                                              profile=PROFILE_A))

        assert len(reads) == num_intervals
        total = 0
        for read in reads:
            total += read[2]
        assert total == pytest.approx(num_intervals)

        # Check first record is double last record
        assert reads[-1][2] == 2 * reads[0][2]
