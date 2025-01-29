"""Удаление заметок"""
# Список из заметок
notes = [{'Имя пользователя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'},
         {'Имя пользователя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}]

# Выводим существующие заметки
print("\nТекущие заметки:")
i = 0
for item in notes:
    print(f'{i + 1}.')
    i += 1
    print(*item.items(), sep='\n')
    print('')

# запрос критерия для удаления заметки
ans = input('Введите имя пользователя или заголовок заметки которую хотите удалить: ').strip()

# Проверка на совпадение заголовков

for j in range(len(notes)):
    try:
        if notes[j]['Заголовок'] == ans or notes[j]['Имя пользователя'] == ans:
            # Предложение подтвердить удаление в случае совпадения
            answer = input('Заметка найдена. Подтвердите удаление(да/нет): ').lower()
            if answer == 'да':
                del notes[j]
                print('Заметка успешно удалена.')
                break
            else:
                break
        else:
            print('Заметок с таким именем пользователя или заголовком не найдено.')

    except ValueError:
        print('Заметок с таким именем пользователя или заголовком не найдено.')


# Выводим список заметок после удаления
print('Остались следующие заметки:')
b = 0
for item in notes:
    print(f'{b + 1}.')
    b += 1
    print(*item.items(), sep='\n')
