from datetime import datetime, timedelta
import calendar

result = []
interval = input()
start, end = [datetime.strptime(date, '%Y-%m-%d') for date in input().split()]
if start == end:
    print(1)
    print(start.strftime('%Y-%m-%d') + ' ' + end.strftime('%Y-%m-%d'))
else:
    while True:
        after = start
        if interval == 'MONTH':
            after = after.replace(
                day=list(calendar.monthrange(start.year, start.month))[1])
        elif interval == 'WEEK':
            while after.isoweekday() != 7:
                after += timedelta(days=1)
        elif interval == 'YEAR':
            after = after.replace(day=31, month=12)
        elif interval == 'QUARTER':
            while not ((after.day == 31 and after.month == 3)
                       or (after.day == 30 and after.month == 6)
                       or (after.day == 30 and after.month == 9)
                       or (after.day == 31 and after.month == 12)):
                after += timedelta(days=1)
        elif interval == 'REVIEW':
            while not ((after.day == 31 and after.month == 3)
                       or (after.day == 30 and after.month == 9)
                       or (after.day == 31 and after.month == 3)):
                after += timedelta(days=1)
        if after < end:
            result.append(start.strftime('%Y-%m-%d') +
                          ' ' + after.strftime('%Y-%m-%d'))
            start = after
            start += timedelta(days=1)
        else:
            result.append(start.strftime('%Y-%m-%d') +
                          ' ' + end.strftime('%Y-%m-%d'))
            break

    print(len(result))
    print('\n'.join(result))
