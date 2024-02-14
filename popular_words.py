def popular_words(text, words):
    txt_lower = text.lower()
    wrd_dict = {}

    for word in words:
        wrd_dict[word] = txt_lower.split().count(word)
    return wrd_dict

assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')