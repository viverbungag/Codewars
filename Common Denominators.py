# def convertFracts(lst):
#     if not lst:
#         return []
#     maxim = max(lst, key = lambda x: x[1])
#     minim = min(lst, key = lambda x: x[1])
#     upto = 1
#     boole = False
#     ans = []
#     for x in lst:
#         upto *= x[1]

#     for x in range(maxim[1], upto+1, minim[1]):
#         for y in lst:
#             if x % y[1]  == 0:
#                 boole = True
#             else:
#                 boole = False
#                 break
#         if boole:
#             for y in lst:
#                 ans.append([(x//y[1])*y[0], x])
#             break      
#     return ans

# def convertFracts(lst):
#     if not lst:
#         return []
#     lst.sort(key = lambda x: x[1])
#     boole = False
#     ans = []
#     lstDenom = []


#     for x in range(len(lst)):
#         for y in range(x+1, len(lst)):
#             denom = lst[x][1] * lst[y][1]
#             for z in lst:
#                 if denom % z[1] == 0:
#                     boole = True
#                 else:
#                     boole = False
#                     break
#             if boole:
#                 lstDenom.append(denom)
#     denom = min(lstDenom)
#     for w in lst:
#         ans.append([(denom//w[1])*w[0], denom])
#     return ans

from math import gcd
def convertFracts(lst):
    if not lst:
        return []
    arr = []
    ans = []
    for x in lst:
        arr.append(x[1])
    denom = arr[0]
    for x in arr[1:]:
        denom = denom * x // gcd(denom, x)
    
    for y in lst:
        ans.append([(denom//y[1])*y[0], denom])
    return ans




print (convertFracts([[1, 2], [1, 3], [1, 4]]))