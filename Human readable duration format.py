
def format(current, next1, next2, next3, next4):
    addFormat = ""
    if current > 1:
        addFormat += "s"
    if next2 or next3 or next4:
        addFormat += ", "
    elif next1:
        addFormat += " and "
    
    return addFormat


def format_duration(seconds):
    #your code here
    ans = ""
    hour = 0
    mins = 0
    days = 0
    years = 0

    while seconds >= 31536000:
        years += 1
        seconds -= 31536000

    while seconds >= 86400:
        days += 1
        seconds -= 86400

    while seconds >= 3600:
        hour += 1
        seconds -= 3600

    while seconds >= 60:
        mins += 1
        seconds -= 60

    if years:
        ans += str(years) + " year" + format(years, days, hour, mins, seconds)
    if days:
        ans += str(days) + " day" + format(days, hour, mins, seconds, 0)
    if hour:
        ans += str(hour) + " hour" + format(hour, mins, seconds, 0, 0)
    if mins:
        ans += str(mins) + " minute" + format(mins, seconds, 0, 0, 0)
    if seconds:
        ans += str(seconds) + " second" + format(seconds, 0, 0, 0, 0)

    if ans:
        return ans
    return "now"

print (format_duration(3662))