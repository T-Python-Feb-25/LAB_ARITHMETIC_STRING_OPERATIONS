
# LAB_ARITHMETIC_STRING_OPERATIONS

#1. Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price:float= 15.7

#2. Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity:int= 4

#3. Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).

tax_rate:float= 0.15

#4. Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".

subtotal= price*quantity

#5. Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".

tax=subtotal*tax_rate

#6. Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".

total = subtotal+tax

#7. Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).
print("**Bill information**")
print(f"Price of item: {price} SAR \nQuantity: {quantity} \nTax rate: {tax_rate*100} %")
print(f"\nSubtotal: {subtotal} SAR \nTax: {tax} SAR \nTotal: {total} SAR")
