# LAB_ARITHMETIC_STRING_OPERATIONS

price = 11.21
quantity = 2
tax_rate = 0.075

subtotal = price*quantity

tax = subtotal*tax_rate

total = subtotal+tax


print(f"Price of item: {price} SR")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%")
print(f"Subtotal: {round(subtotal,2)} SR")
print(f"Tax: {round(tax, 2)} SR")
print(f"Total:{total:.2f} SR")
