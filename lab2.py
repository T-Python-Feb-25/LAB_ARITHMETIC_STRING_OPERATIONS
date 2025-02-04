price:float = 10
quantity:int = 5
tax_rate:int = 15


subtotal:float = price * quantity
tax:float = (tax_rate / 100) * subtotal

total:float = subtotal + tax

print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%\n")

print(f"Subtotal: ${round(subtotal,2)}")
print(f"Tax: ${round(tax,2)}")
print(f"Total: ${round(total,2)}")

