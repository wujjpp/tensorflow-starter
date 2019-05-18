from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2019, 5, 17, 12, 34, 56)
print(dt)

ts = dt.timestamp()
print(ts)  # float,单位: 秒

print(datetime.fromtimestamp(ts))  # 当前时区

print(datetime.utcfromtimestamp(ts))  # UTC-0

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

dt = now + timedelta(hours=10, days=1)

print(dt)

tz_utc8 = timezone(timedelta(hours=8))
now = datetime.now()

print(now)

now_utc8now = now.replace(tzinfo=tz_utc8)
print(now_utc8now)

# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
