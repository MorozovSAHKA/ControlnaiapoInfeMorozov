import pandas as pd


# Чтение Excel-файла
df_excel = pd.read_excel('Book1.xlsx')

# Посмотреть первые 5 строк
print(df_excel.head())

# Посмотреть информацию о таблице
print(df_excel.info())



# df = pd.read_excel('output.xlsx')

def view_select_row(df):
    try:
        row_number = int(input("Выбери строчку, которую хочешь просмотреть:"))

        if 0 <= row_number < len(df):
            print(f"Строка {row_number}:")
            print(df.iloc[row_number])
        else:
            print("Ошибка, повтори попытку")
    except ValueError:
        print("Ошибка, Введи целое число.")

view_select_row(df_excel)