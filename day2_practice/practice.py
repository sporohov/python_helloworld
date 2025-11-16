"""Обрабатывает данные csv и выводит нормализованные данные в вывод"""

# Исходная строка с данными о товаре
# Формат: "  НАИМЕНОВАНИЕ ;  АРТИКУЛ ; КАТЕГОРИЯ ; ЦЕНА (float) ; КОЛИЧЕСТВО (int)  "
raw_data = "  ноутбук игровой MSI GF63   ;   MSI-GF63-123   ;   Игровые ноутбуки ;  95000.50   ; 15    "

raw_data = raw_data.strip()

list_data = raw_data.split(";")

name = list_data[0].strip().title()
art = list_data[1].strip().upper()
category = list_data[2].strip().title()
count = float(list_data[3].strip())
price = int(list_data[4].strip())

print(f"""--- Обработанный товар ---
Наименование: {name}
Артикул: {art}
Категория: {category}
Цена: {count}
Количество: {price}""")
