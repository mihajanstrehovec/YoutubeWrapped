from datetime import date, datetime
date_time = "2021-11-26T21:16:16Z"

if "." in date_time:
    date_time = date_time.replace("T", " ").split(".", 1)
else:
    date_time = date_time.replace("T", " ").split("Z", 1)
print(date_time[0])

time = datetime.strptime(date_time[0], "%Y-%m-%d %H:%M:%S")

print(time.hour)


