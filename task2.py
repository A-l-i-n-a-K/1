vowels = ('a', 'e', 'i', 'o', 'u','а','я','у','ю','о','е','ё','э','и','ы')

try:
    while True:
        text = input("Введите текст: ").lower()  # Преобразуем текст в нижний регистр для учета всех символов
        if all((ch.isalpha() or ch.isspace()) for ch in text):
            break
        else:
            print("Введите только буквы")

    vowel_count = 0
    consonant_count = 0

    for char in text:         #text-последовательность
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    print("Количество гласных букв: ", vowel_count)
    print("Количество согласных букв: ", consonant_count)

    if vowel_count == consonant_count:
        print("Гласные буквы в тексте:")
        for char in text:
            if char in vowels:
                print(char)

    words = text.split()
    word_count = len(words)
    print("Количество слов в тексте: ", word_count)

except Exception as e:
    print("Произошла ошибка:", e)
