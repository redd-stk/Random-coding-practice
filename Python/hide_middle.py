

def hide_middle_of_words(words_list):
    for i in words_list:
        method = word[0] + '-' * (len(word) - 2) + word[-1]
        word = i



words_list = ["Adriana", "Ann", "Angela"]
hidden_words = hide_middle_of_words(words_list)
print(hidden_words)


def get_max_value_and_key(a_dict):
    max_value = max(ages.values())