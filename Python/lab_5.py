str_1 = input("Введите слова, разделяя их запятой: ")
words_1 = str_1.split(", ")

print("Количество слов в списке: ", len(words_1))
str_2 = input("Введите столько же слов, разделяя их запятой: ")
words_2 = str_2.split(", ")

dct = {key: value for key, value in list(zip(words_1, words_2))}
print(dct)