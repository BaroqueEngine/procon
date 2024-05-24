import datetime
S = input()
start_year, start_month, start_day = map(int, S.split("-"))
T = input()
end_year, end_month, end_day = map(int, T.split("-"))

cnt = 0
dt = datetime.datetime(start_year, start_month, start_day)
dt2 = datetime.datetime(end_year, end_month, end_day)

while True:
    if dt.weekday() in [5, 6]:
        cnt += 1
    if dt == dt2:
        break
    dt += datetime.timedelta(days=1)

print(cnt)