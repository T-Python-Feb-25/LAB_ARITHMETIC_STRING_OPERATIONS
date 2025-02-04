price= 2.99
print(f"price of item: ${price}")

quantity= 3
print(f"quantity of item: {quantity}")

tax_rate= 7.5
print(f"tax rate: %{tax_rate}")

subtotal = price * quantity
print(f"subtotal: ${round(subtotal, 2)}")

tax = subtotal * tax_rate / 100
print(f"tax:  ${round(tax, 2)}")

total = subtotal + tax
print(f"total: ${round(total, 2)}")


