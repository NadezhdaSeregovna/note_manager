"""update_status.py: Проверка и обновление статуса заметки"""
from greetings import status

#Запрос статуса заметки у пользователя
print('Текущий статус заметки: ', status)
print('Выберите новый статус заметки (ввести номер): \n 1. выполнено \n 2. в процессе \n 3. отложено')

#ввод нового статуса пользователем в переменную num
num = int(input())

print('Ваш выбор: ', num) #вывод выбранного варианта на экран

#запись нового значения статуса в переменную status
if num == 1:
    status = '"выполнено"'
elif num == 2:
    status = '"в процессе"'
elif num == 3:
    status = '"отложено"'
else:
    print("некорректный ввод")

print('Статус заметки успешно обновлён на: ', status)

