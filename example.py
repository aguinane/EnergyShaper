import datetime
from energy_shaper import Reading
from energy_shaper import split_into_daily_intervals
from energy_shaper import split_into_profiled_intervals
from energy_shaper import group_into_profiled_intervals
from energy_shaper import group_into_daily_summary


MONTH_RECORDS = [
    Reading(datetime.datetime(2017, 1, 1, 0, 0),
     datetime.datetime(2017, 2, 1, 0, 0), 5*31),
    Reading(datetime.datetime(2017, 2, 1, 0, 0), datetime.datetime(2017, 2, 9, 0, 0), 5*8),
    Reading(datetime.datetime(2017, 2, 9, 0, 0),
     datetime.datetime(2017, 3, 1, 0, 0), 5*20),
    Reading(datetime.datetime(2017, 3, 1, 0, 0),
     datetime.datetime(2017, 3, 1, 12, 0), 5*0.5),
    Reading(datetime.datetime(2017, 3, 1, 12, 0),
     datetime.datetime(2017, 3, 2, 0, 0), 5*0.5),
]


def main():

    print('Printing Input')
    for row in MONTH_RECORDS:
        print(row)

    print('\nPrinting output')
    daily = list(split_into_daily_intervals(MONTH_RECORDS))
    hourly = list(split_into_profiled_intervals(daily, interval_m=1,
                                                profile=[1, 1, 1, 1]))
    for row in hourly[0:3]:
        print(row)
    print('...')
    for row in hourly[-3:]:
        print(row)

    print('\nRe-grouping output')
    hourly2 = list(group_into_profiled_intervals(hourly, interval_m=30,
                                                 profile=[1, 1, 1, 1]))
    for row in hourly2[0:3]:
        print(row)
    print('...')
    for row in hourly2[-3:]:
        print(row)


    print('\nDaily Summaries')
    days = list(group_into_daily_summary(MONTH_RECORDS))
    for row in days[0:3]:
        print(row)
    print('...')
    for row in days[-3:]:
        print(row)


if __name__ == "__main__":
    main()
