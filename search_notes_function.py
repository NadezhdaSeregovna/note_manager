"""Функция поиска заметок"""


def search_notes(notes, keyword=None, status=None):
    # обработка пустого списка
    if len(notes) == 0:
        print("Заметки отсутствуют")
        return []

    # если не указаны статус и ключевое слов
    if keyword is None and status is None:
        return notes

    notes_search = []  # новый список для найденных заметок

    for note in notes:
        search_status = True
        search_keyword = True

        # Поиск по ключевому слову
        if keyword is not None:
            keyword = keyword.lower()
            # поиск в имени пользователя, заголовке или содержании
            search_keyword = (keyword in note['Имя пользователя'].lower() or
                              keyword in note['Заголовок'].lower() or
                              keyword in note['Описание'].lower()
                              )

        # поиск в статусах
        if status is not None:
            status = status.lower()
            search_status = status in note['Статус'].lower()

        # поиск с учётом обоих условий
        if search_keyword and search_status:
            notes_search.append(note)

    # вывод результата
    if notes_search:
        print("Найдены заметки:")
        for i, note in enumerate(notes_search, 1):
            print(f"\nЗаметка {i}:")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f"Имя пользователя: {note['Имя пользователя']} \nЗаголовок: {note['Заголовок']} "
                  f"\nОписание: {note['Описание']} \nСтатус: {note['Статус']} "
                  f"\nДата создания: {note['Дата создания']} \nДедлайн: {note['Дедлайн']}")
    else:
        print("Заметки, соответствующие запросу, не найдены.")

    return notes_search



# Список заметок
# notes = []
notes = [
    {'Имя пользователя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю',
     'Статус': 'новая', 'Дата создания': '27-11-2024', 'Дедлайн': '30-11-2024'},
    {'Имя пользователя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену',
     'Статус': 'в процессе', 'Дата создания': '25-11-2024', 'Дедлайн': '01-12-2024'},
    {'Имя пользователя': 'Иван', 'Заголовок': 'План работы', 'Описание': 'Завершить проект',
     'Статус': 'выполнено', 'Дата создания': '20-11-2024', 'Дедлайн': '26-11-2024'}
]
# запуск поиска
while True:
    print('Выберите тип поиска  \n1 - поиск по ключевому слову '
          '\n2 - поиск по статусу \n3 - поиск по ключевому полю и статусу: ')
    ans = input('Введите цифру: ')
    if ans == '1':
        keyword = input('Введите имя, название или описание заметки для поиска: ')
        keyword = search_notes(notes, keyword)
        break
    elif ans == '2':
        status = input('Введите статус заметки для поиска (новая, в процессе, выполнено: ')
        status = search_notes(notes, status)
        break
    elif ans == '3':
        keyword = input('Введите имя, название или описание заметки для поиска: ')
        status = input('Введите статус заметки для поиска: ')
        notes = search_notes(notes, keyword, status)
        break
    else:
        print('Ошибка ввода.')
        continue
