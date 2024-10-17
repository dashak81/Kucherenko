text = input("Введите строку: ")
words = text.split()
found_words = []
for word in words:
    if ('з' in word) or ('к' in word) and word.endswith('я'):
        found_words.append(word)
if found_words:
    print("Слова, содержащие буквы 'з' или 'к' и оканчивающиеся на 'я':")
    for word in found_words:
        print(word)
else:
    print("Таких слов нет")

