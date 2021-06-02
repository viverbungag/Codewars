# def getFib(n):    
#     first = 1
#     second = 1
#     res = 1
#     for x in range(3, n+1):
#         first = second
#         second = res
#         res = first + second
#     return res

# def getFib(n):
#     first = 0
#     second = 1
#     for x in range(n):
#         first, second = second, first + second
#     return first

def getFib(n):
    v1, v2, v3 = 1, 1, 0    
    for rec in bin(n)[3:]:  
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def fib(n):
    if not n:
        return 0
    if n < 0:
        if n%2 == 1:
            return -getFib(-n)   
        return getFib(-n)
    return getFib(n)



print (fib(-200000))

"1, 1, 2, 3, 5, 8, 13"