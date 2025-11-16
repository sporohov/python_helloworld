# инициализация списка (массива)
products = ["Молоко", "Хлеб", "Масло"]
print(f"Исходный список {products}")

# Доступ к элементам
first_product = products[0]
second_product = products[2]

# Изменение
products[1] = "Батон"

# добавление
products.append("Сыр")

# Вставка
products.insert(1, "Кефир")
print(products)

# Удаление по индексу
removed_product = products.pop(2)
print(f"Удаляемый элемент - {removed_product}")
print(f"Список после удаления - {products}")

# .remove(value) - удаляет ПЕРВЫЙ найденный элемент с указанным значением
products.remove("Масло")
print(f"После ремув - {products}")

# Len() - количество элементов
list_lenght = len(products)
print(f"длина списка: {list_lenght}")

# Проверка на вхождение
if "Сыр" in products:
    print("Сыр есть в списке!")

users = ["Иван", "Сергей", "Мария", "Ольга"]

print("---Цикл Для Каждого---")

for user in users:
    print(f"привет {user}!")

# enumetate()
for index, user in enumerate(users):
    print(f"Номер - {index + 1}, имя - {user}")


# Словари

# Создание
product = {
    "name": "Ноутбук",
    "price": 99000,
    "quantity": 15,
    "available": True
}
print(product)

# Получение значений по ключу
print(f"Наименование - {product["name"]}")
print(f"Наименование - {product.get("nameee", "Н/Д")}")

# изменение
product["name"] = "Новое Имя"

# Добавление
product["newValue"] = "Какое то новое значение"

print(product)


# Перебор словаря

User_profile = {
    "name": "Семен",
    "city": "Москва",
    "role": "Developer"
}

# По ключам (по умолчанию)
for key in User_profile:
    print(key)

# По ключам - явно
for key in User_profile.keys():
    print(key)

# По значениям
for val in User_profile.values():
    print(val)

# По паре ключ - значение
for key, val in User_profile.items():
    print(f"кей - {key}, значение - {val}")

# Список словарей
sales_lines = [
    {"name": "клавиатура", "price": 9500, "quantity": 2},
    {"name": "мышь", "price": 950, "quantity": 2},
    {"name": "Ноутбук", "price": 95000, "quantity": 2},
    {"name": "Тетрадь", "price": 95, "quantity": 42},
    {"name": "Ручка", "price": 9, "quantity": 1},
]

# рассчитываем сумму 

total_sum = 0

for line in sales_lines:
    line_sum = line.get("price", 0) * line.get("quantity", 0)

    print(f"Сумма по по строке - {line_sum}")

    total_sum = total_sum + line_sum

print(f"Общая сумма - {total_sum}")