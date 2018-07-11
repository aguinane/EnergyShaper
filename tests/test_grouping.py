""" Test Suite
"""

import pytest
import os
import sys
import datetime
import logging
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from energy_shaper import group_into_daily_summary


MONTH_RECORDS = [
    (datetime.datetime(2017, 1, 1, 0, 0),
     datetime.datetime(2017, 2, 1, 0, 0), 5*31),
    ]


def test_interval_grouping():
    """ Test num of intervals is returned correctly """
    days = list(group_into_daily_summary(MONTH_RECORDS))

    for day in days:
        assert day.total == pytest.approx(5.0)

