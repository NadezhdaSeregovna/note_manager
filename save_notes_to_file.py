"""Сохранение заметок в файл"""

# создание файла
filename = open('filename.txt', 'a+', encoding='utf-8')
filename.close()

#функция записи заметок в файл
def save_notes_to_file(notes, filename):
    # Открытие файла в режиме записи
    with open('filename.txt', "w", encoding='utf-8') as filename:
        #Запись каждой заметки из списка в файл
        for i, notes in enumerate(notes, start=1):
            filename.write(f"\nЗаметка {i}:")

            filename.write(f"\nИмя пользователя: {notes['username']} \nЗаголовок: {notes['title']} "
                  f"\nОписание: {notes['content']} \nСтатус: {notes['status']} "
                  f"\nДата создания: {notes['created_date']} \nДедлайн: {notes['issue_date']}")
            filename.write('\n---')
        filename.close()
    return filename

# Пример использования функции
notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
         'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
         'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект',
         'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]

save_notes_to_file(notes, filename="filename.txt")

