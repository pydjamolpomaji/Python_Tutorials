# Function to print words which can be created
# using given set of characters

def count_character(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict


def possible_words(string, char_set):
    for word in string:
        flag = 1
        count = 0
        chars = count_character(word)
        for key in chars:
            if key not in char_set:
                flag = 0
                count = count + 1
            else:
                if char_set.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)


if __name__ == "__main__":
    string = ['python', 'django', 'java', 'html', 'css', 'javascript']
    char_set = ['p', 'o', 'v', 'a', 'j', 't', 's',
                'c', 'y', 'h', 'm', 'l', 'n', 'd', 'g']
    possible_words(string, char_set)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
