def get_count(input_str):
    num_vowels = 0
    vowel = "aeiouAEIOU"
    for vow in vowel:
        for x in input_str:
            if vow == x:
                num_vowels = num_vowels + 1
            
    # your code here
    
    return num_vowels

print (get_count("Hello world"))