from datetime import datetime, date , timedelta

t4 = timedelta(2022, 9, 11, 20, 2, 33)
t5 = timedelta(2004, 6, 14, 6, 20, 33)
t6 = t4 - t5
print(t6)
print(t6.total_seconds())
print('abs = ', abs(t6))