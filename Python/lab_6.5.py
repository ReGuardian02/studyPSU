str_1 = input("Введите слова, разделяя их запятой: ")
words_1 = str_1.split(", ")

print("Количество слов в списке: ", len(words_1))

str_2 = input("Введите столько же слов, разделяя их запятой: ")
words_2 = str_2.split(", ")

def dictionary(s1, s2):
    dct = {key: value for key, value in list(zip(s1, s2))}
    return dct

d = dictionary(words_1, words_2)
print(d)