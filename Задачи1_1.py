text = input("Введите строку: ")
words = text.split()

unique_words = set(words)

print("Уникальные слова в строке:")
for word in unique_words:
    print(word)