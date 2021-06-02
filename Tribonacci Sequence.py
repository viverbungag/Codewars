def tribonacci(signature, n):
    p = 0
    while len(signature) < n:
        signature.append(signature[p] + signature[p+1] + signature[p+2])
        p += 1
    return signature[:n]

print (tribonacci([300, 200, 100], 5))
