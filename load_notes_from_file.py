"""Загрузка заметок из файла"""

def load_notes_from_file(filename):
    try:
       with open(filename, 'r', encoding='utf-8') as file:  # Открыть файл в режиме чтения
            info = file.readlines() # чтение строк в файле
    except FileNotFoundError: #отработка исключения, если файла не существует
        print('Файл не найден')
        return []

    #удаление лишних символов, разделитей заметок
    symbols = "---"
    info= [line for line in info if line != symbols]

    notes = []  # соднание списка для хранения словарей

    #получение пары ключ - значение для словаря
    try:
        for line in info:
            note = {}  # соднание словаря для хранения заметки
            key, value = line.split(': ')
            note[key] = value
        notes.append(note)
    except:
        print("Проверьте содержимое файла")



    #вывод полученных заметок
    for i, note in (notes):
        print(f"Имя пользователя: {note['username']} \nЗаголовок: {note['title']} "
              f"\nОписание: {note['content']} \nСтатус: {note['status']} "
              f"\nДата создания: {note['created_date']} \nДедлайн: {note['issue_date']}")
    return notes

if __name__ == "__main__":
    filename = 'filename.txt'
    load_notes_from_file(filename)

