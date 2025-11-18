

def filter_valid_items(items: list) -> list:

    result = [item for item in items if item.get("price", 0) > 0 and item.get("quantity", 0) > 0]

    for item in items:
        if item not in result:
            print(f"Проблема с товаров {item.get("product_name", "[Товар не найден]")} некорректное количество или цена")

    return result

def calculate_totals(items: list) -> dict:
    
    grand_total = 0    grand_quantity = 0

    for item in items:
        sum_line = item.get("quantity", 0) * item.get("price", 0)

        item["sum"] = sum_line

        grand_total = grand_total + sum_line
        grand_quantity = grand_quantity + item.get("quantity", 0)

    result = {
        "grand_total": grand_total,
        "grand_quantity": grand_quantity}

    return result

def print_receipt(items: list, totals: dict):

    print("--- Ваша корзина ---")

    for index, item in enumerate(items, start=1):
        print(f"{index}. {item.get("product_name", "")} - {item.get("quantity", 0)} шт., стоимость: {item.get("sum", 0)}")

    print("-----------------------")

    print(f"""Общее количество товаров: {totals["grand_quantity"]} шт.
Общая стоимость: {totals["grand_total"]}""")

# Список словарей, представляющий корзину
cart_items = [
    {"product_name": "Молоко", "price": 80, "quantity": 2},
    {"product_name": "Хлеб", "price": 35, "quantity": 1},
    {"product_name": "Масло", "price": 150, "quantity": 0}, # Некорректное количество
    {"product_name": "Сыр", "price": 300, "quantity": 1},
    {"product_name": "Картофель", "price": -40, "quantity": 10}, # Некорректная цена
]

valid_items = filter_valid_items(cart_items)

totals = calculate_totals(valid_items)

print_receipt(valid_items, totals)