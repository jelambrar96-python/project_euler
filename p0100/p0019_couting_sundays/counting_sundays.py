from datetime import datetime, timedelta



def countSundays(start, end):
    cur = start
    num_sundays = 0
    while cur <= end:
        if cur.weekday() == 6 and cur.day == 1:
            num_sundays += 1
        cur += timedelta(days=1)
    return num_sundays


print(countSundays(datetime(1901,1,1), datetime(2000, 12, 31)))