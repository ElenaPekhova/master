per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input ("введите сумму вклада"))
deposit = []
for key in per_cent:
    deposit.append(per_cent[key]*money/100)
max_deposit = max (deposit)
print (deposit)
print ("максимальная сумма, котоую вы можете заюрать - "+ str (max_deposit))