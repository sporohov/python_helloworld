# Классический способ

sales_lines = [
    {"name": "Ноутбук", "price": 95000, "quantity": 2},
    {"name": "Мышь", "price": 1500, "quantity": 5},
    {"name": "Клавиатура", "price": 3000, "quantity": 5}
]


prices = []

for line in sales_lines:
    prices.append(line["price"])

print(f"Список цен (классический способ): {prices}")

# List comprehension
# [ <что_положить> | <откуда_взять> | <если_условие_верно> ]
# [ line["price"] | for line in sales_lines | if line["price"] > 5000 ]

prices_comp = [line["price"] for line in sales_lines]

expensive_prices_comp = [ line["price"] for line in sales_lines if line["price"] > 5000 ]

# Функции
# def - ключевое слово для определения функции
# name - имя функции (глагол)
# (line: dict) - имя переменной и тип
# -> float - мы обещаем, что вернем float

def get_total_line_price(line: dict) -> float:
    """
    рассчитываем общую стоимость по одной строке документа.
    это docstring
    """

    price = line.get("price", 0)
    quantity = line.get("quantity", 0)

    result = price * quantity
    
    return result

# Вызов функции
sales_line_1 = sales_lines[0]
sales_line_2 = sales_lines[1]

total_1 = get_total_line_price(sales_line_1)
total_2 = get_total_line_price(sales_line_2)

print(f"сумма по строке 1: {total_1}")
print(f"сумма по строке 2: {total_2}")