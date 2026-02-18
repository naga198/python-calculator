from calculator import Calculator

calc = Calculator()

print('=' * 50)
print('BASIC OPERATIONS')
print('=' * 50)
print(f'Addition: 1 + 2 = {calc.add(1, 2)}')
print(f'Subtraction: 4 - 2 = {calc.subtract(4, 2)}')
print(f'Multiplication: 2 x 3 = {calc.multiply(2, 3)}')
print(f'Division: 10 / 2 = {calc.divide(10, 2)}')
print(f'Modulo: 10 % 3 = {calc.modulo(10, 3)}')

print('\n' + '=' * 50)
print('FINANCIAL FUNCTIONS')
print('=' * 50)

# Simple Interest
principal = 1000
rate = 5
time = 2
si = calc.simple_interest(principal, rate, time)
print(f'\nSimple Interest:')
print(f'  Principal: ${principal}, Rate: {rate}%, Time: {time} years')
print(f'  Interest: ${si}')

# Compound Interest
principal = 1000
rate = 10
time = 2
ci = calc.compound_interest(principal, rate, time, 1)
amount = principal + ci
print(f'\nCompound Interest:')
print(f'  Principal: ${principal}, Rate: {rate}%, Time: {time} years')
print(f'  Interest: ${ci:.2f}')
print(f'  Total Amount: ${amount:.2f}')

# Compound Interest Monthly
principal = 1000
rate = 12
time = 1
ci_monthly = calc.compound_interest(principal, rate, time, 12)
amount_monthly = principal + ci_monthly
print(f'\nCompound Interest (Monthly):')
print(f'  Principal: ${principal}, Rate: {rate}%, Time: {time} year, Compounds: 12x/year')
print(f'  Interest: ${ci_monthly:.2f}')
print(f'  Total Amount: ${amount_monthly:.2f}')

# IRR
cash_flows = [-1000, 400, 400, 400]
irr = calc.irr(cash_flows)
print(f'\nInternal Rate of Return (IRR):')
print(f'  Cash Flows: {cash_flows}')
print(f'  IRR: {irr*100:.2f}%')
