def xo(s):
    string = s.lower()
    x_array = []
    o_array = []
    for h in string:
        if h is "x":
            x_array.append(h)
        if h is "o":
            o_array.append(h)
    if len(x_array) == len(o_array):
        return True
    else:
        return False

print(xo("xxxoooxxxoo"))