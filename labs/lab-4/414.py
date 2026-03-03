from datetime import datetime, timedelta

def parse(line):
    date_part, tz_part = line.split()

    dt = datetime.strptime(date_part, "%Y-%m-%d")

    sign = 1 if '+' in tz_part else -1
    hh, mm = map(int, tz_part[3:].split('+')[1].split(':')
                 if '+' in tz_part
                 else tz_part[3:].split('-')[1].split(':'))

    offset = timedelta(hours=hh, minutes=mm) * sign

    utc_time = dt - offset
    return utc_time

a = input().strip()
b = input().strip()

t1 = parse(a)
t2 = parse(b)

days = abs((t1 - t2).total_seconds()) // 86400

print(int(days))