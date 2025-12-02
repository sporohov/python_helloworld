
def print_order_report(order_lines: list, totals: dict):
    """Печатает финальный отчет по заказу."""
    print("="*40)
    print("Отчет по заказу".center(40))
    print("="*40)

    for line in order_lines:
        print(
            f"- {line['name']}: {line['quantity']} шт. x {line['price']} руб. "
            f"| Итого: {line['total_price_with_vat']} руб." # !!! Потенциальная ошибка №3 (в форматировании)
        )

    print("-"*40)
    print(f"Итого без НДС: {totals['grand_total_without_vat']:.2f} руб.")
    print(f"Сумма НДС: {totals['total_vat']:.2f} руб.")
    print(f"ИТОГО К ОПЛАТЕ: {totals['grand_total_with_vat']:.2f} руб.")
    print("="*40)
