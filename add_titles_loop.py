#Вводим заметки
titles = []
while True:
    title = input(f'Введите заголовок заметки (или оставьте пустым или введите "стоп" для завершения): ')
    if title == "" or title == "стоп":
        break
    elif title in titles:
        print("Такой заголовок существует, повторите ввод.")
        continue
    else:
        titles.append(title)


# Выводим собранные данные
print("\nЗаголовки заметки:")
print(*titles , sep = "\n")


