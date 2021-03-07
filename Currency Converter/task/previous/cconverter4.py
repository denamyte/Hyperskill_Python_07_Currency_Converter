currencies = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
coni_sum = float(input())

for curr, rate in currencies.items():
    value = round(rate * coni_sum, 2)
    print(f'I will get {value} {curr} from the sale of {coni_sum} conicoins.')
