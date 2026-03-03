from datetime import datetime, timedelta

def get_offset(tz):
    sign = 1 if '+' in tz else -1
    if sign == 1:
        hh, mm = map(int, tz.split('+')[1].split(':'))
    else:
        hh, mm = map(int, tz.split('-')[1].split(':'))
    return timedelta(hours=hh, minutes=mm) * sign


def parse_utc(line):
    date_part, time_part, tz_part = line.split()

    local_dt = datetime.strptime(
        date_part + " " + time_part,
        "%Y-%m-%d %H:%M:%S"
    )

    offset = get_offset(tz_part)

    return local_dt - offset

start_line = input().strip()
end_line = input().strip()

start_utc = parse_utc(start_line)
end_utc = parse_utc(end_line)

duration = int((end_utc - start_utc).total_seconds())

print(duration)