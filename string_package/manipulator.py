import string

reverse_string = lambda s: s[::-1]
capitalize_words = lambda s: s.title()
remove_punctuation = lambda s: ''.join(c for c in s if c not in string.punctuation)

if __name__ == "__main__":
    test = "hello world"
    print("original:", test)
    print("reversed:", reverse_string(test))
    print("capitalized:", capitalize_words(test))
    print("no punctuation:", remove_punctuation(test))
