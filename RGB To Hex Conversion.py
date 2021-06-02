def hex(color):
    if color < 0:
        color = 0
    if color > 255:
        color = 255
    ans = ""
    first = 0
    second = 0
    first = color//16
    second = color % 16
    if first > 9:
        first = chr(first+55)
    if second > 9:
        second = chr(second+55)
    return str(first)+str(second)


def rgb(r, g, b):
    if r < 0:
        return hex(r)+hex(g)+hex(b)
    if r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0:
        return "000000"
    #your code here :)
    return hex(r)+hex(g)+hex(b)

print (rgb(255, 255, 255))