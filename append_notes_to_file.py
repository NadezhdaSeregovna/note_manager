"""Добавление данных в файл"""
import os

def append_notes_to_file(notes, filename):
    if os.path.isfile("filename.txt"):
        # Открытие файла в режиме добавления
        with open('filename.txt', "a", encoding='utf-8') as filename:
            # Запись каждой заметки из списка в файл
            for i, notes in enumerate(notes, start=1):
                filename.write(f"Имя пользователя: {notes['username']}\n"
                               f"Заголовок: {notes['title']}\n"
                               f"Описание: {notes['content']}\n"
                               f"Статус: {notes['status']}\n"
                               f"Дата создания: {notes['created_date']}\n"
                               f"Дедлайн: {notes['issue_date']}\n")
                filename.write('---\n')
            print('Заметки в файл успешно добавлены.')

    else:  # создание файла
        filename = open('filename.txt', 'a+', encoding='utf-8')
        filename.close()
        print("Файл filename не найден. Создан новый файл.")

        with open('filename.txt', "a", encoding='utf-8') as filename:
            # Запись каждой заметки из списка в файл
            for i, notes in enumerate(notes, start=1):
                filename.write(f"Имя пользователя: {notes['username']}\n"
                               f"Заголовок: {notes['title']}\n"
                               f"Описание: {notes['content']}\n"
                               f"Статус: {notes['status']}\n"
                               f"Дата создания: {notes['created_date']}\n"
                               f"Дедлайн: {notes['issue_date']}\n")
                filename.write('---\n')
        print('Заметки в файл успешно добавлены.')

    return filename


if __name__ == "__main__":
    notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
              'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
             {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
              'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
             {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект',
              'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]

    append_notes_to_file(notes, filename="filename.txt")
