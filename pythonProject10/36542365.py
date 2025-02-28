import matplotlib.pyplot as plt

# Шаг 2: Подготовка данных
x = ['Яблоки', 'Бананы', 'Апельсины', 'Груши']
y = [18, 15, 7, 12]

# Шаг 3: Построение столбчатой диаграммы
plt.bar(x, y, color='red')

# Шаг 4: Добавление подписей и заголовка
plt.xlabel('Фрукты')
plt.ylabel('Количество')
plt.title('Продажи фруктов')

# Шаг 5: Добавление сетки
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Шаг 6: Отображение диаграммы
plt.show()