price:float=2.99
quantity:int=3
tax_rate:float=7.5
sub_total=price*quantity
tax=sub_total*(tax_rate/100)
total=tax+sub_total
print(f"Price of item: ${price} \nQuantity: {quantity} \nTax rate: {tax_rate}%\n\nSubtotal: ${sub_total} \nTax: ${round(tax,2)} \nTotal: ${round(total,2)}") 