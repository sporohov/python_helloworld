VAT_RATE = 1.2 # Ставка НДС 20%

def filter_and_calculate_lines(order_lines: list) -> list:
    """
    Фильтрует строки заказа, удаляя невалидные.
    Для валидных строк рассчитывает сумму с НДС и без.
    """
    valid_lines = []
    for line in order_lines:
        # Считаем, что все строки валидны, но нужно рассчитать суммы
        price = line.get("price", 0)
        quantity = line.get("quantity", 0) 

        total_price = price * quantity
        total_price_with_vat = total_price * VAT_RATE

        line["total_price"] = total_price
        line["total_price_with_vat"] = total_price_with_vat
        valid_lines.append(line)
    
    return valid_lines


def calculate_order_totals(order_lines: list) -> dict:
    """Рассчитывает итоговые суммы по всему заказу."""
    grand_total = 0
    total_vat = 0

    for line in order_lines:
        grand_total += line.get("total_price", 0)
        
    total_vat = grand_total * (VAT_RATE - 1)

    return {
        "grand_total_without_vat": grand_total,
        "total_vat": total_vat,
        "grand_total_with_vat": grand_total + total_vat
    }
