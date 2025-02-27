import pandas as pd

# Чтение Excel-файла
df_excel = pd.read_excel('Book1.xlsx')

# Посмотреть первые 5 строк
print("Первые 5 строк таблицы:")
print(df_excel.head())

# Посмотреть информацию о таблице
print("\nИнформация о таблице:")
print(df_excel.info())


# Функция для просмотра выбранной строки
def view_selected_row(df):
    try:
        # Запрос номера строки у пользователя
        row_number = int(input("\nВведите номер строки, которую хотите просмотреть: "))

        # Проверка, что номер строки находится в допустимых пределах
        if 0 <= row_number < len(df):
            print(f"\nСтрока {row_number}:")
            print(df.iloc[row_number])
        else:
            print("Ошибка: Номер строки вне диапазона.")
    except ValueError:
        print("Ошибка: Введите целое число.")


# Вызов функции для просмотра строки
view_selected_row(df_excel)