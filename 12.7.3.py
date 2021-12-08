per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input()
per_cent_list = list(per_cent.values())
deposit = [int(i * float(money)/100) for i in per_cent_list]
print(deposit)
print("Максимальная сумма, которую вы можете заработать — " + str(max(deposit)))


