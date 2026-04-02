from datetime import datetime, timedelta, timezone

expire = datetime.now(timezone.utc) + timedelta(minutes=10)
to_encode = {"exp": expire, }
print(expire)