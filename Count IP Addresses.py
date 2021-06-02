def ips_between(start, end):
    start = start.split(".")
    end = end.split(".")
    ans = 0
    ans += int(end[3]) - int(start[3])
    ans += (int(end[2]) - int(start[2]))*256
    ans += ((int(end[1]) - int(start[1]))*256)*256
    ans += (((int(end[0]) - int(start[0]))*256)*256)*256
    return ans




print (ips_between("20.0.0.10", "20.0.1.0"))