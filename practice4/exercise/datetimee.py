#1
from datetime import datetime , timedelta
today = datetime.now()
n_d = today - timedelta(days=5)
print(n_d)

#2
from datetime import datetime , timedelta
today = datetime.now()
yest = today - timedelta(days=1)
tommo = today + timedelta(days=1)
print(f"Yesterday : {yest}")
print(f"Today : {today}")
print(f"Tomorrow : {tommo}")

#3
from datetime import datetime , timedelta
rn = datetime.now()
micro = rn.replace(microsecond=0)
print(micro)

#4
from datetime import datetime
date1 = datetime(2026, 3, 1, 12, 0, 0)
date2 = datetime(2026, 3, 2, 12, 0, 0)
diff = date2 - date1
print(diff.total_seconds())