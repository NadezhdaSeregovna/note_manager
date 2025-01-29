"""Загрузка заметок из файла"""

def load_notes_from_file(filename):
    try:
       with open(filename, 'r', encoding='utf-8') as file:  # Открыть файл в режиме чтения
        info = file.read() # чтение строк в файле
        # print(info)
        notes = []  # соднание списка для хранения словарей
        if info:
            note_blocks = info.split('---')  # разделение текста из файла на заметки по разделителю
            # print(note_blocks)
            for block in note_blocks:
                note_lines = block.strip().split('\n')
                note_lines = list(filter(None, note_lines))#удаление пустых строк
                # print(note_lines)
                note = {}  # соднание словаря для хранения заметки

                for line in note_lines:
                    #разбиение строки на ключ и значение
                    key, value = line.split(': ', 1)
                    note[key] = value
                notes.append(note)
            # print(notes)

    except FileNotFoundError: #отработка исключения, если файла не существует
        print(f'Файл {filename} не найден')
        return []

    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

    return notes


if __name__ == "__main__":
    notes = load_notes_from_file('filename.txt')
    for note in (notes):
        print(note)

