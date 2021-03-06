# EnergyShaper

Split and group energy billing data to analyse usage and apply load profiles

[![Build Status](https://travis-ci.org/aguinane/EnergyShaper.svg?branch=master)](https://travis-ci.org/aguinane/EnergyShaper) [![Coverage Status](https://coveralls.io/repos/github/aguinane/EnergyShaper/badge.svg)](https://coveralls.io/github/aguinane/EnergyShaper) [![PyPI version](https://badge.fury.io/py/energy-shaper.svg)](https://badge.fury.io/py/energy-shaper)

## Split into intervals based on load profile

Given a bunch of energy readings:

```
<Reading start=2017-01-01 00:00:00, end=2017-02-01 00:00:00, usage 155.00>
<Reading start=2017-02-01 00:00:00, end=2017-02-09 00:00:00, usage 40.00>
<Reading start=2017-02-09 00:00:00, end=2017-03-01 00:00:00, usage 100.00>
<Reading start=2017-03-01 00:00:00, end=2017-03-01 12:00:00, usage 2.50>
<Reading start=2017-03-01 12:00:00, end=2017-03-02 00:00:00, usage 2.50>
```

Split them up based on a user-specified load profile.
First split them so each reading is at most a day.
The input readings can be at varying read intervals.

```python
daily = list(split_into_daily_intervals(records))
```

Then split into required interval.

```python
minute = list(split_into_profiled_intervals(daily, interval_m=1,
                                            profile=[1, 1, 1, 1]))
```

The profile is a list indicating a daily profile at whatever resolution you desire. It will adjust the ratios so they add to 100%.

```python
profile=[0.05, 0.07, 0.12, 0.11, 0.14, 0.14, 0.27, 0.10]
```

The load will then be split up based on the profile:
```
<Reading start=2017-01-01 00:00:00, end=2017-01-01 00:01:00, usage 0.00>
<Reading start=2017-01-01 00:01:00, end=2017-01-01 00:02:00, usage 0.00>
<Reading start=2017-01-01 00:02:00, end=2017-01-01 00:03:00, usage 0.00>
...
<Reading start=2017-03-01 23:57:00, end=2017-03-01 23:58:00, usage 0.00>
<Reading start=2017-03-01 23:58:00, end=2017-03-01 23:59:00, usage 0.00>
<Reading start=2017-03-01 23:59:00, end=2017-03-02 00:00:00, usage 0.00>
```

## Grouping intervals

The splitting functions will keep smaller interval lengths if available, so we may want to group them back up again to get a consistent interval across all readings. This will automatically split readings passed to it first.

```python
half_hourly = list(group_into_profiled_intervals(minute, interval_m=30,
                                                 profile=[1, 1, 1, 1])
                                                 )
```

```
<Reading start=2017-01-01 00:00:00, end=2017-01-01 00:30:00, usage 0.10>
<Reading start=2017-01-01 00:30:00, end=2017-01-01 01:00:00, usage 0.10>
<Reading start=2017-01-01 01:00:00, end=2017-01-01 01:30:00, usage 0.10>
...
<Reading start=2017-03-01 22:30:00, end=2017-03-01 23:00:00, usage 0.10>
<Reading start=2017-03-01 23:00:00, end=2017-03-01 23:30:00, usage 0.10>
<Reading start=2017-03-01 23:30:00, end=2017-03-02 00:00:00, usage 0.10>
```                                              

## Daily stats

Finally, you can group back up to daily values again.
There are a bunch of optional keyword arguments that lets you calculate
what the usage is during peak and shoulder periods.

```python
days = list(group_into_daily_summary(MONTH_RECORDS))
```

```
<DaySummary 2017-01-01 Usage:5.00>
<DaySummary 2017-01-02 Usage:5.00>
<DaySummary 2017-01-03 Usage:5.00>
...
<DaySummary 2017-02-27 Usage:5.00>
<DaySummary 2017-02-28 Usage:5.00>
<DaySummary 2017-03-01 Usage:5.00>
```
