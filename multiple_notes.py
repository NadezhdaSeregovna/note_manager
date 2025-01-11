"""Работа с несколькими заметками"""
# добавление библиотеки для работы с датами
from datetime import datetime

# Создаем список для хранения информации о заметках
notes = []

print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.')

while True:
    # Сбор данных от пользователя
    username = input("Введите имя пользователя: ")
    while username == '':  # проверка чтобы поле было непустым
        print("Имя пользователя не может быть пустым: ")
        username = input("Введите имя пользователя: ")

    title = input("Введите заголовок заметки: ")
    while title == '':  # проверка чтобы поле было непустым
        print("Заголовок заметки не может быть пустым: ")
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

    #ввод и проверка корректности ввода даты 
    while True:
        created_date = input("Введите дату создания заметки в формате (день-месяц-год): ")
        try:
            datetime.strptime(created_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Введен неверный формат даты: ")
            print("Введите дату в формате (день-месяц-год, например, 01-01-2025: ")
            continue

    # ввод и проверка корректности ввода даты дэдлайна
    while True:
        issue_date = input("Введите дату истечения заметки в формате (день-месяц-год): ")
        try:
            datetime.strptime(issue_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Введен неверный формат даты: ")
            continue

    # создание словаря для новой заметки
    note = {'user': username, 'titles': title, 'content': content, 'status': status,
            'created_date': created_date,  'issue_date':  issue_date
            }

    # добавление записки в список
    notes.append(note)

    # предложение ввести новую заметку
    ans = input('Хотите добавить ещё одну заметку? (да/нет): ').lower().strip()
    if ans == "да":
        continue
    else:
        break

# Выводим собранные данные
print("\nСписок заметок:")
for note in notes:
    print(f"\n Имя пользователя: {note['user']}")
    print(f" Заголовок заметки: {note['titles']}")
    print(f" Описание заметки:: {note['content']}")
    print(f" Статус заметки: {note['status']}")
    print(f" Дата создания заметки: {note['created_date']}")
    print(f" Дата истечения заметки: {note['issue_date']}")
