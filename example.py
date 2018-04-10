import datetime
from energy_shaper import split_into_daily_intervals
from energy_shaper import split_into_profiled_intervals

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


def main():

    print('Printing Input')
    for row in MONTH_RECORDS:
        print(row)

    print('Printing output')
    daily = list(split_into_daily_intervals(MONTH_RECORDS))
    hourly = list(split_into_profiled_intervals(daily, interval_m=30,
                                                profile=[1, 1, 1, 1]))
    for row in hourly[0:5]:
        print(row)
    print('...')
    for row in hourly[-5:]:
        print(row)


if __name__ == "__main__":
    main()
