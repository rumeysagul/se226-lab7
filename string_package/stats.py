count_characters = lambda s: len(s)
count_words = lambda s: len(s.split())
average_word_length = lambda s: (sum(len(word) for word in s.split()) / len(s.split())) if s.split() else 0

if __name__ == "__main__":
    test = "hello world"
    print("characters:", count_characters(test))
    print("words:", count_words(test))
    print("average word length:", average_word_length(test))
