from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)

if __name__ == "__main__":
    sentence = input("enter a sentence: ")

    print("reversed:", reverse_string(sentence))
    print("capitalized:", capitalize_words(sentence))

    clean = remove_punctuation(sentence)
    print("without punctuation:", clean)
    print("character count :", count_characters(clean))
    print("word count:", count_words(clean))
    print("average word length:", average_word_length(clean))
