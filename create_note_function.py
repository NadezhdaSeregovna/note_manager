"""Функция создания заметки"""
from datetime import datetime
from datetime import date


# фукнция сбора данных о заметке от пользователя
def create_note():
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
    note = {'user': username, 'titles': title, 'content': content, 'status': status,
            'created_date': created_date, 'issue_date': issue_date
            }
    return note

# вызов функции
note = create_note()

# печать заметки
print("\nСозданная заметка:")
for i, k in note.items():
    print(i, k)
