""" Test Suite
"""

import pytest
import os
import sys
import datetime
import logging
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from energy_shaper import split_into_intervals
from energy_shaper import split_into_daily_intervals, split_into_profiled_intervals


MONTH_RECORDS = [
    (datetime.datetime(2017, 1, 1, 0, 0),
     datetime.datetime(2017, 2, 1, 0, 0), 5 * 31),
    (datetime.datetime(2017, 2, 1, 0, 0),
     datetime.datetime(2017, 2, 9, 0, 0), 5 * 8),
    (datetime.datetime(2017, 2, 9, 0, 0),
     datetime.datetime(2017, 3, 1, 0, 0), 5 * 20),
    (datetime.datetime(2017, 3, 1, 0, 0),
     datetime.datetime(2017, 3, 1, 12, 0), 5 * 0.5),
    (datetime.datetime(2017, 3, 1, 12, 0),
     datetime.datetime(2017, 3, 2, 0, 0), 5 * 0.5),
]


def test_interval_splitting():
    """ Test num of intervals is returned correctly """
    start_date = datetime.datetime(2017, 1, 1, 0, 0)
    end_date = datetime.datetime(2017, 1, 2, 0, 0)
    vals = list(split_into_intervals(start_date, end_date, interval_m=30))
    assert len(vals) == 48


def test_interval_splitting_uneven():
    """ Test where intervals are uneven """
    start_date = datetime.datetime(2017, 1, 1, 0, 0)
    end_date = datetime.datetime(2017, 1, 1, 2, 30)
    vals = list(split_into_intervals(start_date, end_date, interval_m=60))
    assert len(vals) == 3  # Two hours and a half hour
    assert vals[-1][1] == end_date


def test_hourly_splitting():
    """ Test breaking into hourly profiles """
    test_records = MONTH_RECORDS
    start_date = test_records[0][0]
    end_date = test_records[-1][1]
    daily = list(split_into_daily_intervals(test_records))
    hourly = list(split_into_profiled_intervals(daily))
    assert start_date == hourly[0][0]
    assert end_date == hourly[-1][1]
