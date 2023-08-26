import time
from datetime import date

def get_difference(date1, date2):
    delta = date2 - date1
    return delta.days

bdate = list(map(int, input("Enter the Birth date (DD/MM/YYYY): ").split("/")))
bdate_day, bdate_month, bdate_year = bdate

while True:
    named_tuple = time.localtime()  # get struct_time
    d1 = date(named_tuple.tm_year, named_tuple.tm_mon, named_tuple.tm_mday)
    d2 = date(bdate_year, bdate_month, bdate_day)
    days = get_difference(d1, d2)

    current_time = time.strftime("%H:%M:%S", named_tuple)
    remaining_time = time.strptime(f"{23-named_tuple.tm_hour}:{59-named_tuple.tm_min}:{59-named_tuple.tm_sec}", "%H:%M:%S")

    print(f"{days} Days {remaining_time.tm_hour}:{remaining_time.tm_min}:{remaining_time.tm_sec} to go :)")
    time.sleep(1)
