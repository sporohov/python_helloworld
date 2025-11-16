user_name = "Semen"
age = 30

user_info = f"Пользователь: {user_name}, возраст - {age}"
print(user_info)

raw_fio = "  Порохов семен АЛЕКСАНДРОВИЧ   "
print(f"Исходная строка: '{raw_fio}'")

# .strip() - СокрЛП
clean_fio = raw_fio.strip()
print(clean_fio)

fio_lower = clean_fio.lower()
print(fio_lower)

# первую букву заглавной - остальные строчными.
fio_capitalized = clean_fio.capitalize()
print(fio_capitalized)

# заглавной каждую первую букву каждого слова
fio_title = fio_capitalized.title()
print(fio_title)

# стрЗаменить
phone = "+7 (999) 123-45-67"
clean_phone = phone.replace(" ", "").replace(")", "").replace("(", "").replace("-", "")
print(f"исходный телефон - {phone}, чистый - {clean_phone}")

# СтрРазделить
product_data = "ноутбук;150000;15.6"
product_list = product_data.split(";")
print(product_list)

#СтрСоединить
words = ["это", "пример", "предложения"]
sentence = " ".join(words)
print(sentence)