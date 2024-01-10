from datetime import date
import timedelta

data_atual = date.today()
print(data_atual)

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)
print(data_em_texto)
data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)
