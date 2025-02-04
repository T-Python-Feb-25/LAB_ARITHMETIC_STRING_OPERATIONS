price:float = 2.99
quantity:int = 3
tax_rate:float = 7.5
subtotal = price * quantity

tax = subtotal * (tax_rate / 100)

total = subtotal + tax 

price1 = f"Price of item: ${price}"
quantity1 = f"Quantity : {quantity}"
tax_rate1 = f"Tax rate:{tax_rate}%"


subtotal1 = f"subtotal:${subtotal}"
tax1 = f"tax: ${tax:.2f}"
total1 = f"Total: ${total:.2f}"
print(price1)
print(quantity1)
print(tax_rate1)
print(subtotal1)
print(tax1)
print(total1)