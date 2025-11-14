# ============================================================
# DATETIME – MOST COMMON METHODS AND FUNCTIONS (FULL EXAMPLE)
# ============================================================

from datetime import datetime, date, time, timedelta


# ------------------------------------------------------------
# 1. Current date and time (datetime.now)
# ------------------------------------------------------------
print("=== Current datetime ===")
now = datetime.now()
print(now)


# ------------------------------------------------------------
# 2. Current date only (date.today)
# ------------------------------------------------------------
print("\n=== Today's date ===")
today = date.today()
print(today)


# ------------------------------------------------------------
# 3. Combining date and time (datetime.combine)
# ------------------------------------------------------------
print("\n=== Combine date and time ===")
d = date(2025, 11, 5)
t = time(14, 30)
combined_dt = datetime.combine(d, t)
print(combined_dt)


# ------------------------------------------------------------
# 4. Replacing parts of a datetime (replace)
# ------------------------------------------------------------
print("\n=== Replace datetime components ===")
new_time = now.replace(hour=9, minute=0, second=0)
print(new_time)


# ------------------------------------------------------------
# 5. Formatting datetime -> string (strftime)
# ------------------------------------------------------------
print("\n=== Formatting with strftime ===")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%A, %B %d, %Y"))  # Day and month name


# ------------------------------------------------------------
# 6. Parsing string -> datetime (strptime)
# ------------------------------------------------------------
print("\n=== Parsing with strptime ===")
date_str = "2025-11-05 15:30"
parsed_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
print(parsed_dt)


# ------------------------------------------------------------
# 7. Date arithmetic with timedelta
# ------------------------------------------------------------
print("\n=== Timedelta arithmetic ===")
future = today + timedelta(days=10)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(weeks=1)

print("10 days later:", future)
print("Yesterday:", yesterday)
print("One week later:", next_week)


# ------------------------------------------------------------
# 8. Weekday and ISO weekday
# ------------------------------------------------------------
print("\n=== Weekday ===")
print("weekday():", today.weekday())         # Mon=0 ... Sun=6
print("isoweekday():", today.isoweekday())   # Mon=1 ... Sun=7


# ------------------------------------------------------------
# 9. ISO format (isoformat)
# ------------------------------------------------------------
print("\n=== ISO format ===")
print(now.isoformat())


# ------------------------------------------------------------
# 10. Timestamp and fromtimestamp
# ------------------------------------------------------------
print("\n=== Timestamp conversion ===")
ts = now.timestamp()       # Convert datetime → UNIX timestamp
print("Timestamp:", ts)

dt_from_ts = datetime.fromtimestamp(ts)  # UNIX timestamp → datetime
print("From timestamp:", dt_from_ts)


# ------------------------------------------------------------
# 11. Timedelta total_seconds()
# ------------------------------------------------------------
print("\n=== Timedelta total seconds ===")
delta = timedelta(days=1, hours=2)
print("Total seconds:", delta.total_seconds())


# ------------------------------------------------------------
# 12. Practical usage examples
# ------------------------------------------------------------
print("\n=== Practical examples ===")

# Logging
print(now.strftime("[LOG %Y-%m-%d %H:%M:%S] Action completed"))

# Reminder 3 days later
reminder = now + timedelta(days=3)
print("Reminder set for:", reminder.strftime("%A, %B %d"))

# Parsing another custom date format
parsed_date = datetime.strptime("2025/11/05", "%Y/%m/%d")
print("Parsed date:", parsed_date.date())


# ------------------------------------------------------------
# 13. Your original formatting examples (preserved + commented)
# ------------------------------------------------------------
print("\n=== Your formatting examples ===")

print(datetime(2020, 10, 10).strftime('%Y-%m-%d'))      # 2020-10-10
print(datetime(2020, 10, 10).strftime('%d/%m/%Y'))      # 10/10/2020
print(datetime(2020, 10, 10).strftime('%B %d, %Y'))     # October 10, 2020
