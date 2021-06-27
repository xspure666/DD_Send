import time
import pytz
import datetime

# data_time = time.strftime("2021-06-26T18:07:52.697Z", "%Y-%m-%dT%H:%M:%SZ")


abc = datetime.datetime.strptime('2021-06-26T18:07:52.697Z', "%Y-%m-%dT%H:%M:%S.%fZ")
print(type(abc))
# now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(type(now_time))
# print(now_time)

startsAt = (datetime.datetime.strptime("2021-06-26T18:07:52.697Z", "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(hours=8)).strftime(
    '%Y-%m-%d %H:%M:%S')
print(type(startsAt))


print(datetime.datetime.now())
print(type(datetime.datetime.now()))


now = datetime.datetime.now()
abc = datetime.datetime.strptime('2021-06-26T18:07:52.697Z', "%Y-%m-%dT%H:%M:%S.%fZ")


print(type(str(abc)))