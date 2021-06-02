import re

def encode_rail_fence_cipher(string, n):
    pass
    # n = len(string)//n
    # print (re.findall('.{1,' + str(n//2) + '}', string))

    
def decode_rail_fence_cipher(string, n):
    arr = ["" for x in range(n*2)]
    cnt = 0
    for x in string:
        
        
        cnt += 1


encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3)

decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3)