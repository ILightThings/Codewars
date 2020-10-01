def spin_words(sentence):
    word_array = sentence.split(" ")
    for i in range(len(word_array)):
        if len(word_array[i]) > 4:
           word_array[i] = "".join(reversed(word_array[i]))
    new = " ".join(word_array)
    return(new)


spin_words("My name is gideon")


