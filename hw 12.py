per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму депозита:'))
deposit = max([v*money/100 for k, v in per_cent.items()])
print('Максимальная сумма,которую вы можете заработать- ', deposit)


