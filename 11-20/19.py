from datetime import date, timedelta

start = date.fromisoformat("1901-01-01")
end = date.fromisoformat("2000-12-31")
cur = start 
ans = 0
while cur <= end:
    if cur.weekday() == 6 and cur.day == 1:
        ans += 1
    cur += timedelta(days=1)
print(ans)