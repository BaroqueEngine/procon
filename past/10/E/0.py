import datetime

S = input()
Y, M, D = map(int, S.split("/"))
time = datetime.datetime(Y, M, D)

while True:
    str_time = time.strftime("%Y/%m/%d")
    st = set(list(str_time))
    if len(st) == 3:
        print(str_time)
        break
    time += datetime.timedelta(days=1)
