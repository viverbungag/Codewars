from collections import Counter
def scramble(s1, s2):
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    for x in cnt2:
        if cnt2[x] > cnt1[x]:
            return False
    return True


print (scramble('scriptixcvdfasfasfdsfsdfsdfsdfdsvdsxfsvdsvsdngjava', 'javascript'))