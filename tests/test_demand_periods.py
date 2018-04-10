""" Test Suite
"""

import pytest
import os
import sys
import datetime
import logging
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from energy_shaper import in_peak_day, in_peak_time
from energy_shaper import in_peak_period


def test_peak_day():
    """ Test the day period matching is returned correctly """

    peak_months = [12,1,2]  # Summer
    peak_days = [1, 2, 3, 4, 5]  # Weekdays

    billing_time = datetime.datetime(2018, 1, 1, 0, 0, 0) # Mon
    assert in_peak_day(billing_time, peak_months, peak_days)

    billing_time = datetime.datetime(2018, 1, 6, 0, 0, 0) # Sat
    assert not in_peak_day(billing_time, peak_months, peak_days)

    billing_time = datetime.datetime(2018, 7, 1, 0, 0, 0) # Winter
    assert not in_peak_day(billing_time, peak_months, peak_days)


def test_peak_time():
    """ Test the time period matching is returned correctly """

    peak_start = datetime.time(15, 0, 0)
    peak_end = datetime.time(21, 30, 0)

    billing_time = datetime.datetime(2018, 1, 1, 11, 0, 0)
    assert not in_peak_time(billing_time, peak_start, peak_end)

    # Time is billing end so peak starts after the peak_start
    billing_time = datetime.datetime(2018, 1, 1, 15, 0, 0)
    assert not in_peak_time(billing_time, peak_start, peak_end)

    billing_time = datetime.datetime(2018, 1, 1, 15, 30, 0)
    assert in_peak_time(billing_time, peak_start, peak_end)

    # Time is billing end so end of peak is still in peak
    billing_time = datetime.datetime(2018, 1, 1, 21, 30, 0)
    assert in_peak_time(billing_time, peak_start, peak_end)

    billing_time = datetime.datetime(2018, 1, 1, 23, 30, 0)
    assert not in_peak_time(billing_time, peak_start, peak_end)


def test_peak_period():
    """ Test the time period matching is returned correctly """

    peak_months = [12,1,2]  # Summer
    peak_days = [1, 2, 3, 4, 5]  # Weekdays
    peak_start = datetime.time(15, 0, 0)
    peak_end = datetime.time(21, 30, 0)

    billing_time = datetime.datetime(2018, 1, 1, 16, 30, 0) # Mon
    assert in_peak_period(billing_time, peak_months, peak_days,
                              peak_start, peak_end)

    billing_time = datetime.datetime(2018, 1, 1, 23, 30, 0) # Mon Late
    assert not in_peak_period(billing_time, peak_months, peak_days,
                              peak_start, peak_end)

    billing_time = datetime.datetime(2018, 1, 6, 16, 30, 0) # Sat
    assert not in_peak_period(billing_time, peak_months, peak_days,
                              peak_start, peak_end)

    billing_time = datetime.datetime(2018, 1, 6, 23, 30, 0) # Sat Late
    assert not in_peak_period(billing_time, peak_months, peak_days,
                              peak_start, peak_end)
