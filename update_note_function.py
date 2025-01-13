"""Функция обновления заметки"""
from datetime import datetime

print('Текущие данные заметки: ')
note = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
        'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
# вывод существующей заметки для ознакомления
for i, k in note.items():
    print(i, k)


def update_note(note):
    while True:
        ans = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')
        if ans in ['username', 'title', 'content', 'status', 'issue_date']:
            break
        else:
            print('Введены некорректные данные. Повторите ввод')
            continue

    while True:

            if ans == 'username':
                username = input('Введите новое значение для username: ')
                while username == '':  # проверка чтобы поле было непустым
                    print("Имя пользователя не может быть пустым: ")
                    username = input("Введите имя пользователя: ")
                note['username'] = username

            elif ans == 'title':
                title = input('Введите новое значение для title: ')
                while title == '':  # проверка чтобы поле было непустым
                    print("Заголовок заметки не может быть пустым: ")
                    title = input("Введите заголовок заметки: ")
                note['title'] = title

            elif ans == 'content':
                content = input('Введите новое значение для content: ')
                while content == '':  # проверка чтобы поле было непустым
                    print("Заголовок заметки не может быть пустым: ")
                    content = input("Введите описание заметки: ")
                note['content'] = content

            elif ans == 'status':
                status = input('Введите новое значение для status: ')
                # проверка правильности введенного статуса
                while status not in ['новая', 'в процессе', 'выполнено']:
                    print("Выбран несушествующий статус: ")
                    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
                note['status'] = status

            elif ans == 'issue_date':
                while True: #проверка корректности ввода даты
                    issue_date = input('Введите значение для issue_date в формате (день-месяц-год): ')
                    try:
                        issue_date = datetime.strptime(issue_date, "%d-%m-%Y").date()
                        break
                    except ValueError:
                        print("Введен неверный формат даты: ")
                        continue
                note['issue_date'] = datetime.strftime(issue_date, "%d-%m-%Y")
            break

    return note


# вызов функции, отработка ошибки ввода некорректных данных
update_note(note)

# печать заметки после обновления
print("\nЗаметка обновлена:")
for i, k in note.items():
    print(i, k)
