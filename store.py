price = 2.99 
quantity = 3
tax_rate = 7.6

subtotal = price * quantity

tax = subtotal * (tax_rate/ 100)

total = subtotal + tax

print(f"Price of item: ${price: .2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%\n")

print(f"suptotal: ${subtotal:.2f}")
print(f"Tax: ${tax: .2f}")
print(f"Total:${total: .2f}")