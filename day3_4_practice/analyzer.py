# Список словарей, представляющий корзину
cart_items = [
    {"product_name": "Молоко", "price": 80, "quantity": 2},
    {"product_name": "Хлеб", "price": 35, "quantity": 1},
    {"product_name": "Масло", "price": 150, "quantity": 0}, # Некорректное количество
    {"product_name": "Сыр", "price": 300, "quantity": 1},
    {"product_name": "Картофель", "price": -40, "quantity": 10}, # Некорректная цена
]

print("--- Ваша корзина ---")

valid_items = []

for item in cart_items:
    
    if item.get("price", 0) > 0 and item.get("quantity", 0) > 0:
        valid_items.append(item)
    else:
        print(f"Проблема с товаров {item.get("product_name", "[Товар не найден]")} некорректное количество или цена")
        continue

grand_total = 0
grand_quantity = 0

for index, item in enumerate(valid_items):
    print(f"{index + 1}. {item["product_name"]} - {item["quantity"]} шт., стоимость: {item["price"]}")
    grand_total = grand_total + item.get("price", 0)
    grand_quantity = grand_quantity + item.get("quantity", 0)

print("-----------------------")

print(f"""Общее количество товаров: {grand_quantity} шт.
Общая стоимость: {grand_total}""")

