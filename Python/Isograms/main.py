def is_isogram(string):
    word = string.lower()
    letters = []
    for x in word:
        if x not in letters:
            letters.append(x)
    if len(word) == len(letters):
        return True
    else:
        return False
        
        


is_isogram("HelloWorld")