def make_readable(seconds):
    sec1 = sec2 = min1 = min2 = hr1 = hr2 = 0
    for _ in range(seconds):
        sec1+=1
        if sec1 == 10:
            sec2 +=1
            sec1 = 0
        
        if sec2 == 6:
            min1+=1
            sec2 = 0
        
        if min1 == 10:
            min2 +=1
            min1 = 0
        
        if min2 == 6:
            hr1 += 1
            min2 = 0

        if hr1 == 10:
            hr2 += 1
            hr1 = 0
        
        if hr2 == 10:
            break

    return str(hr2) + str(hr1) + ":" + str(min2) + str(min1) + ":" + str(sec2) + str(sec1)