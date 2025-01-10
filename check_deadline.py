"""check_deadline.py: Обработка дедлайнов"""
#импорт модуля для работы с датами
from datetime import datetime
from datetime import date

#определение текущей даты и запись в переменную issue_date
today = date.today()

# вывод текущей даты
print(today.strftime('%d-%m-%Y'))

while True:
    try:
        #запрос даты дэдлайна, преобразование в формат ДАТА
        issue_date_str = (input('Введите дату дедлайна (в формате день-месяц-год): '))
        issue_date =  datetime.strptime(issue_date_str, '%d-%m-%Y').date()

    #сравнение дат и вывод результата
        if today > issue_date:
            rez = today - issue_date
            print('Внимание! Дедлайн истёк ', rez.days , ' дня назад.')
        else:
            rez =  issue_date - today
            print('До дедлайна осталось ', rez.days, ' дня.')

        # Прерываем цикл после успешной обработки даты
        break

    except ValueError:
        #Обработка ошибки неверного формата даты
        print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
        print("Пример: 25-12-2024")

    except Exception as e:
        #Обработка прочих ошибок
        print(f"Произошла непредвиденная ошибка: {str(e)}")
        print("Пожалуйста, попробуйте снова.")
