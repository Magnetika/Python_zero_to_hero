# 🎯 Lesson Objective:
# Understand how to unpack strings into individual variables,
# and learn how string unpacking relates to sequence unpacking in Python.

# ----------------------------------------------------------
# 📘 DATA SETUP
# ----------------------------------------------------------
abc = "abcef"

# ----------------------------------------------------------
# 🧩 1. Unpack a short string into separate variables
# ----------------------------------------------------------
word = "Hi"
a, b = word
print("📍 Basic unpacking:")
print(a, b)  # H i
print()

# ----------------------------------------------------------
# 🧩 2. Use * to capture multiple characters during unpacking
# ----------------------------------------------------------
a, *others, f = abc
print("📍 Using * to capture middle characters:")
print(a, others, f)
# a = 'a', others = ['b', 'c', 'e'], f = 'f'
print()

# ----------------------------------------------------------
# 🧩 3. Try unpacking with too few or too many variables
# ----------------------------------------------------------
print("📍 Unpacking with wrong number of variables:")
try:
    x, y, z = "Hi"  # only 2 characters available
except ValueError as e:
    print("Error:", e)
print()

# ----------------------------------------------------------
# 🧩 4. Combine string unpacking with f-strings or formatting
# ----------------------------------------------------------
first, *middle, last = "Python"
print("📍 Combine unpacking with f-string formatting:")
print(f"The first letter is '{first}', the last letter is '{last}', middle part: {''.join(middle)}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Strings can be unpacked just like lists or tuples
# - Use * to collect multiple characters
# - Make sure the number of variables matches the characters
# - Great for quickly splitting or analyzing characters in a string
