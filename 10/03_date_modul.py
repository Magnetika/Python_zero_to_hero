# ============================================================
# DATETIME MODULE – COMPLETE EXAMPLE FILE
# Covers: current date/time, creating dates, formatting,
# parsing, timedelta arithmetic, comparisons, weekdays,
# and practical usage examples.
# ============================================================

from datetime import datetime, date, time, timedelta


# ------------------------------------------------------------
# 1. Getting the current date and time
# ------------------------------------------------------------
print("=== Current datetime ===")
current_datetime = datetime.now()      # Current local date and time
print(current_datetime)
print("Type:", type(current_datetime))


# ------------------------------------------------------------
# 2. Accessing individual components
# ------------------------------------------------------------
print("\n=== Datetime components ===")
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)
print("Microsecond:", current_datetime.microsecond)


# ------------------------------------------------------------
# 3. Getting only the current date
# ------------------------------------------------------------
print("\n=== Today's date ===")
today = date.today()
print(today)


# ------------------------------------------------------------
# 4. Creating specific date/time/datetime objects
# ------------------------------------------------------------
print("\n=== Creating date/time/datetime ===")
birthday = date(2000, 5, 17)
meeting_time = time(14, 30)
event_datetime = datetime(2025, 1, 15, 10, 45)

print("Birthday:", birthday)
print("Meeting time:", meeting_time)
print("Event datetime:", event_datetime)


# ------------------------------------------------------------
# 5. Formatting datetime with strftime()
# ------------------------------------------------------------
print("\n=== Formatting datetime (strftime) ===")
formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Additional examples:
print("Day name:", current_datetime.strftime("%A"))
print("Month name:", current_datetime.strftime("%B"))


# ------------------------------------------------------------
# 6. Parsing (string → datetime) with strptime()
# ------------------------------------------------------------
print("\n=== Parsing date strings (strptime) ===")
date_str = "2025-11-05 15:30:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed)


# ------------------------------------------------------------
# 7. Date arithmetic with timedelta
# ------------------------------------------------------------
print("\n=== Date arithmetic (timedelta) ===")
next_week = current_datetime + timedelta(days=7)
yesterday = current_datetime - timedelta(days=1)

print("Next week:", next_week)
print("Yesterday:", yesterday)

# Add hours, minutes, etc.
in_two_hours = current_datetime + timedelta(hours=2)
print("Two hours later:", in_two_hours)


# ------------------------------------------------------------
# 8. Comparing dates
# ------------------------------------------------------------
print("\n=== Date comparison ===")
a = date(2025, 5, 17)
b = date(2025, 11, 5)

if b > a:
    print("b is later than a")
else:
    print("a is later or equal")


# ------------------------------------------------------------
# 9. Weekday examples
# ------------------------------------------------------------
print("\n=== Weekday ===")
print("Number (Mon=0):", today.weekday())
print("Day name:", today.strftime("%A"))


# ------------------------------------------------------------
# 10. Practical examples
# ------------------------------------------------------------
print("\n=== Practical examples ===")

# Logging timestamps
print("Log entry at:", datetime.now().strftime("%H:%M:%S"))

# Calculating a deadline
deadline = datetime.now() + timedelta(days=14)
print("Deadline:", deadline)

# Human readable format
print(datetime.now().strftime("Today is %A, %B %d, %Y"))


# ------------------------------------------------------------
# 11. Your original code, kept and commented
# ------------------------------------------------------------
print("\n=== Your original code (with comments) ===")

current_datetime = datetime.now()
print(current_datetime)              # full datetime
print(type(current_datetime))        # class type
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
