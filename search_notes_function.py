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
            search_keyword = (keyword in note['username'].lower() or
                              keyword in note['title'].lower() or
                              keyword in note['content'].lower()
                              )

        # поиск в статусах
        if status is not None:
            search_status = status.lower() == note["status"]


        # поиск с учётом обоих условий
        if search_keyword and search_status:
            notes_search.append(note)

    # вывод результата
    if notes_search:
        print("Найдены заметки:")
        for i, note in enumerate(notes_search, 1):
            print(f"\nЗаметка {i}:")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f"Имя пользователя: {note['username']} \nЗаголовок: {note['title']} "
                  f"\nОписание: {note['content']} \nСтатус: {note['status']} "
                  f"\nДата создания: {note['created_date']} \nДедлайн: {note['issue_date']}")
    else:
        print("Заметки, соответствующие запросу, не найдены.")

    return notes_search



# Список заметок
# notes = []
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
     'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
     'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект',
     'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
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

