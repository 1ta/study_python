import datetime

d_date = input("Enter the date(format YYYY,MM,DD): ")
d1 = datetime.datetime(2005, 9, 25)
d2 = datetime.datetime.strptime(d_date, "%Y,%m,%d")
delta = d2 - d1
time = delta.total_seconds() / 3600
time = int(time)
print("the time difference is",time,"hours")
