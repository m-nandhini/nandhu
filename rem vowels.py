def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
def anti_vowel(c):
    newstr = ""
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            newstr = c.replace(x, "")        
    return newstr
