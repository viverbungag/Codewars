def xo(s):
    s = s.lower()
    Xcount = s.count("x")
    Ycount = s.count("o")
    if Xcount == Ycount:
        return True
    else:
        return False