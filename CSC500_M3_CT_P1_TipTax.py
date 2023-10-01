import decimal
from decimal import Decimal

#Calculate tax, pre-tax tip, and payment total for restaurant bill.

TAX_PERCENT = 7
TIP_PERCENT = 18

tax_multiplier = Decimal(TAX_PERCENT / 100)
tip_multiplier = Decimal(TIP_PERCENT / 100)


print('\nTax and Tip Calculator.')

bill = Decimal(input('\nEnter the bill amount (before tax): $'))
tax = tax_multiplier * bill
tip = tip_multiplier * bill
total = bill + tax + tip

print()
print('Bill:', str(bill.quantize(Decimal('1.00'))).rjust(12), sep = '')
print('Tax', ('@' + str(TAX_PERCENT) + '%:').rjust(6),
      str(tax.quantize(Decimal('1.00'))).rjust(8), sep = '')
print('Tip', ('@' + str(TIP_PERCENT) + '%:').rjust(6),
      str(tip.quantize(Decimal('1.00'))).rjust(8),'\n', sep = '')
print('Total:', ('$' + str(total.quantize(Decimal('1.00')))).rjust(11),
      sep = '')


