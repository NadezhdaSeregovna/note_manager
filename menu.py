"""Меню действий"""

from datetime import datetime
from datetime import date
from colorama import Fore, Back, init  # импорт библиотеки colorama для визуального оформления

init(autoreset=True)  # сброс оформления текста после вызова


# Функция создания заметки
def create_note():
    username = input("Введите имя пользователя: ")
    while username == '':  # проверка чтобы поле было непустым
        print(Fore.RED + "Имя пользователя не может быть пустым: ")
        username = input("Введите имя пользователя: ")

    title = input("Введите заголовок заметки: ")
    while title == '':  # проверка чтобы поле было непустым
        print(Fore.RED + "Заголовок заметки не может быть пустым: ")
        title = input("Введите заголовок заметки: ")

    content = input("Введите описание заметки: ")
    while content == '':  # проверка чтобы поле было непустым
        print("Заголовок заметки не может быть пустым: ")
        content = input("Введите описание заметки: ")

    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    # проверка правильности введенного статуса
    while status not in ['новая', 'в процессе', 'выполнено']:
        print("Выбран несушествующий статус: ")
        status = input("Введите статус заметки (новая, в процессе, выполнено): ")

    # ввод и проверка корректности ввода даты дэдлайна
    while True:
        issue_date = input("Введите дату истечения заметки в формате (день-месяц-год): ")
        try:
            datetime.strptime(issue_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Введен неверный формат даты: ")
            continue

    # дата создания определяется автоматически
    created_date = date.today()
    created_date.strftime('%d-%m-%Y')

    # создание словаря из собранных данных
    note = {'username': username, 'title': title, 'content': content, 'status': status,
            'created_date': created_date, 'issue_date': issue_date
            }
    return note

# функция для вывода заметок
def display_notes(notes):
    if len(notes) == 0:
        print(Fore.RED + 'У вас нет сохранённых заметок.')
    else:
        for i, note in enumerate(notes, start=1):
            print(Fore.YELLOW + f"\nЗаметка {i}:")
            print(Fore.GREEN + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(Fore.CYAN + f"Имя пользователя: {note['username']} \nЗаголовок: {note['title']} "
                              f"\nОписание: {note['content']} \nСтатус: {note['status']} "
                              f"\nДата создания: {note['created_date']} \nДедлайн: {note['issue_date']}")

    return notes

# функция для обновления заметки
def update_note(notes):
    while True:
        print(Back.WHITE + Fore.BLACK + 'Выберите замеку, которую желаете изменить.')
        print(Fore.YELLOW + 'Вы можете вернуться в главное меню и посмотреть все заметки или '
                                        'ввести номер заметки, которую желаете изменть')
        ans = input('Дла возврата в гланое меню введите 1, для продолжения нажмите Enter: ')
        if ans == '1':
            break

        num = int(input(Back.WHITE + Fore.BLACK + f'Введите номер заметки от 1 до {len(notes)}: '))
        ans = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')
        # if ans in note[num]['username', 'title', 'content', 'status', 'issue_date']:
        #     break
        # else:
        #     print('Введены некорректные данные. Повторите ввод')
        #     continue

        if ans == 'username':
            username = input('Введите новое значение для username: ')
            while username == '':  # проверка чтобы поле было непустым
                print("Имя пользователя не может быть пустым: ")
                username = input("Введите имя пользователя: ")
            notes[num-1]['username'] = username

        elif ans == 'title':
            title = input('Введите новое значение для title: ')
            while title == '':  # проверка чтобы поле было непустым
                print("Заголовок заметки не может быть пустым: ")
                title = input("Введите заголовок заметки: ")
            notes[num-1]['title'] = title

        elif ans == 'content':
            content = input('Введите новое значение для content: ')
            while content == '':  # проверка чтобы поле было непустым
                print("Заголовок заметки не может быть пустым: ")
                content = input("Введите описание заметки: ")
            notes[num-1]['content'] = content

        elif ans == 'status':
            status = input('Введите новое значение для status: ')
            # проверка правильности введенного статуса
            while status not in ['новая', 'в процессе', 'выполнено']:
                print("Выбран несушествующий статус: ")
                status = input("Введите статус заметки (новая, в процессе, выполнено): ")
            notes[num-1]['status'] = status

        elif ans == 'issue_date':
            while True:  # проверка корректности ввода даты
                issue_date = input('Введите значение для issue_date в формате (день-месяц-год): ')
                try:
                    issue_date = datetime.strptime(issue_date, "%d-%m-%Y").date()
                    break
                except ValueError:
                    print("Введен неверный формат даты: ")
                    continue
            notes[num-1]['issue_date'] = datetime.strftime(issue_date, "%d-%m-%Y")
        break

    return notes

# функция для удаления заметки
def delete_note(notes):
    ans = input(Back.WHITE + Fore.BLACK + 'Введите имя пользователя или заголовок заметки которую хотите удалить: ').strip()
    for j in range(len(notes)):
        if notes[j]['title'] == ans or notes[j]['username'] == ans:
            # Предложение подтвердить удаление в случае совпадения
            answer = input(f'В заметке № {j+1} найдено совпадение. Подтвердите удаление(да/нет): ').lower()
            if answer == 'да':
                del notes[j]
                print('Заметка успешно удалена.')
                break
            else:
                break
        else:
            print(Fore.RED + f'В заметке № {j+1} совпадений не найдено.')

    return notes

# функция для поиска заметки
def search_notes(notes, keyword=None, status=None):
    # обработка пустого списка
    if len(notes) == 0:
        print(Fore.YELLOW + "Заметки отсутствуют")
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
        print(Fore.YELLOW + "Заметки, соответствующие запросу, не найдены.")

    return notes_search


# Список заметок
notes = []
while True:
    print('\n---------------------')
    print(Back.WHITE + Fore.BLACK + 'Меню действий:')
    print('1. Создать новую заметку')
    print('2. Показать все заметки')
    print('3. Обновить заметку')
    print('4. Удалить заметку')
    print('5. Найти заметки')
    print('6. Выйти из программы')
    ans = input(Back.WHITE + Fore.BLACK + 'Введите цифру: ')
    print('\n---------------------')
    if ans == '1':
        while True:
            ans = input(Back.WHITE + Fore.BLACK + 'Хотите ввести заметку? (да/нет): ').lower().strip()
            if ans == 'да':
                note = create_note()
                notes.append(note)
                print('Новая заметка создана!')

            elif ans == 'нет':
                break
            else:
                continue

    elif ans == '2':
        display_notes(notes)

    elif ans == '3':
        update_note(notes)

    elif ans == '4':
        delete_note(notes)

    elif ans == '5':
        if __name__ == "__main__":
            while True:
                print(Back.WHITE + Fore.BLACK + 'Выберите тип поиска')
                print('1 - поиск по ключевому слову '
                      '\n2 - поиск по статусу \n3 - поиск по ключевому полю и статусу: ')
                ans = input(Back.WHITE + Fore.BLACK + 'Введите цифру: ')
                if ans == '1':
                    keyword = input('Введите имя пользователя, название или описание заметки для поиска: ')
                    keyword = search_notes(notes, keyword)
                    break
                elif ans == '2':
                    status = input('Введите статус заметки для поиска (новая, в процессе, выполнено: ')
                    status = search_notes(notes=notes, keyword=None, status=status)
                    break
                elif ans == '3':
                    keyword = input('Введите имя, название или описание заметки для поиска: ')
                    status = input('Введите статус заметки для поиска: ')
                    notes = search_notes(notes, keyword, status)
                    break
                else:
                    print('Ошибка ввода.')
                    continue

    elif ans == '6':
        print("Работа с заметками завершена")
        break

    else:
        print(Fore.RED + "Ошибка ввода! Повторите выбор действия")
        continue
