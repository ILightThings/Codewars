vowel = "aeiouAEIOU"

def disemvowel(string):
    neword = string
    for vow in vowel:
        neword = neword.replace(vow,"")
    return(neword)


print(disemvowel("You are the biggest person I have every seen"))

