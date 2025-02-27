import pandas as pd
import matplotlib as plt

# Чтение Excel-файла
df_excel = pd.read_excel('Book2.xlsx')

# Посмотреть первые 5 строк
print(df_excel.head())

# Посмотреть информацию о таблице
print(df_excel.info())



plt.grid(True)

plt.legend()

plt.show()