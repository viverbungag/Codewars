from itertools import permutations as permute

def permutations(string):
    perm = set(permute(string))
    ans = []
    for x in perm:
        wrd = ""
        for y in x:
            wrd += y
        ans.append(wrd)
    return ans


print (permutations('aabb'))