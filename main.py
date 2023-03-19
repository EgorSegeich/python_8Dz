# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text_list = file.read().splitlines()
#         print(text_list)
#         for i in range(-1, -lines-1, -1):
#             print(text_list[i])
#
# a = int(input("введите число "))
# if a > 0:
#     read_last(a, 'article.txt')
# else:
#     print('введено не положительное число')




# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt
# слово, имеющее максимальную длину (или список слов, если таковых несколько).
# 
# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text_list = file.read().split()
#         max_len = int(len(text_list[0]))
#         max_text = text_list[0]
#         for i in range(len(text_list)):
#             if len(text_list[i]) > max_len:
#                 max_len = int(len(text_list[i]))
#                 max_text = text_list[i]
#         print(max_text)
#         with open('result.txt', 'w', encoding='utf-8') as res:
#             res.write(max_text)
#
# longest_words('article.txt')