def highest_rank(arr):
    reoccurane = 0
    char = 0
    rank = []
    for i in arr:
        if arr.count(i) > reoccurane:
            reoccurane = arr.count(i)
    for x in arr:
        if arr.count(x) == reoccurane:
            if x not in rank:
                rank.append(x)
    for o in rank:
        if o > char:
            char = o
    return char        
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))