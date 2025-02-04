
price = 5.99
quantity = 2

tax_rate = 0.075

print(f"Price of item: ${price} \nQuantity: {quantity} \nTax rate: 7.5% ")

subtotal = price * quantity

tax =round((subtotal * tax_rate),2)

total = round((subtotal + tax),2)

print(f"\nSubtotal: ${subtotal} \nTax: ${tax} \nTotal: ${total}")


