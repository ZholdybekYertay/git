from datetime import datetime, timedelta
import calendar
import math

def get_offset(line):
    tz = line.split()[1] 

    sign = 1 if '+' in tz else -1
    if sign == 1:
        hh, mm = map(int, tz.split('+')[1].split(':'))
    else:
        hh, mm = map(int, tz.split('-')[1].split(':'))

    return timedelta(hours=hh, minutes=mm) * sign

def parse_utc(line):
    date_part = line.split()[0]
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    offset = get_offset(line)
    return dt - offset

def birthday_utc(year, month, day, offset):

    if month == 2 and day == 29 and not calendar.isleap(year):
        day = 28

    local_midnight = datetime(year, month, day)
    return local_midnight - offset

birth_line = input().strip()
current_line = input().strip()

birth_date = datetime.strptime(birth_line.split()[0], "%Y-%m-%d")
birth_month = birth_date.month
birth_day = birth_date.day
birth_offset = get_offset(birth_line)

current_utc = parse_utc(current_line)

year = current_utc.year

next_birthday = birthday_utc(year, birth_month, birth_day, birth_offset)

if next_birthday < current_utc:
    next_birthday = birthday_utc(year + 1, birth_month, birth_day, birth_offset)

diff_seconds = (next_birthday - current_utc).total_seconds()

if diff_seconds <= 0:
    print(0)
else:
    print(math.ceil(diff_seconds / 86400))