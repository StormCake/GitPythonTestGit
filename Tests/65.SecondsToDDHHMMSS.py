# Write a Python program to convert seconds to day, hour, minutes and seconds.

seconds = int(input())
hours = days = 0
print(seconds, "seconds is:")

if seconds:
    minutes = seconds // 60
    seconds = seconds % 60
if minutes:
    hours = minutes // 60
    minutes = minutes % 60
if hours:
    days = hours // 24
    hours = hours % 24
print(days, 'days', hours, 'hours', minutes, 'minutes and ', seconds, ' seconds')
