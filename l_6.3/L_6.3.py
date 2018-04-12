#!/usr/bin/env python3.6
dividends = []
divisors = []

# waiting for correct input of number of pairs
pair_amount = 0
while not pair_amount:
    try:
        pair_amount = int(input('Number of pairs> '))
    except ValueError:
        print('Incorrect number of pairs entered (should be integer greater than 0).')

# waiting for correct inputs for all pairs
while len(dividends) < pair_amount:
    try:
        a, b = input('Pairs> ').split(' ')
    except ValueError:
        print('Incorrect pair: should be only one space in entered line.')
        continue
    dividends.append(a)
    divisors.append(b)

result_to_print = []  # stores result of division or error message
for dividend, divisor in zip(dividends, divisors):
    try:
        dividend, divisor = int(dividend), int(divisor)
    except ValueError as error:
        result_to_print.append(f'Error code: {error}')
        continue
    try:
        result_to_print.append(dividend / divisor)
    except ZeroDivisionError as error:
        result_to_print.append(f'Error code: {error}')

for result in result_to_print:
    print(result)
