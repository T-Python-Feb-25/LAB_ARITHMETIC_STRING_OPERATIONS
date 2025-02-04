price=2.99
quantity = 3
tax_rate = 0.075
subtotal=price * quantity
tax= subtotal * tax_rate
total = subtotal + tax 
print("price = 2.99")
print("quantity = 3")
print("tax_rate= 0.075")
print (f"subtotal:${subtotal:.2f}")
print(f"Tax ({tax_rate*100:.1f}%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
