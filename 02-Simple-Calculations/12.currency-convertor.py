amount = float(input())
input_currency = input().upper()
output_currency = input().upper()
usd = 1.79549
eur = 1.95583
gbp = 2.53405
result = amount

if input_currency == 'USD':
    result *= usd
elif input_currency == 'EUR':
    result *= eur
elif input_currency == 'GBP':
    result *= gbp

if output_currency == 'USD':
    result /= usd
elif output_currency == 'EUR':
    result /= eur
elif output_currency == 'GBP':
    result /= gbp

print('{0:.2f} {1}'.format(result, output_currency))
