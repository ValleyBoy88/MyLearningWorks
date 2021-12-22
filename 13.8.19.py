# Стоимость билетов
price_child = 0
price_young = 990
price_old = 1390
sum = 0

# Количество билетов
count_ticket = None

# Запрос ввода
count_ticket = int(input("Введете количество билетов: "))

# Запрос возраста для каждого билета
for i in range(count_ticket):
    h = int(input(f"Введете возраст для {i + 1} посетителя: "))
    if h < 18:
        sum = sum + price_child
    elif h < 25:
        sum = sum + price_young
    else:
        sum = sum + price_old

# Пересчет суммы со скидкой
if count_ticket >= 3:
    sum = sum - sum / 10

# Вывод итоговой суммы
print(f"Итоговая сумма: {sum}")
