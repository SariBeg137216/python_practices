
def count_words(text):
    result = dict()
    words = text.split(' ')
    for word in words:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result


print(count_words(" Hello World "))
