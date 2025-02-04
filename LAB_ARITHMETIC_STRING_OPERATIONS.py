#Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = 1200.50
#Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity= 3
#Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
tax_rate=0.15
#Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".
subtotal = price *quantity
#Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
tax = subtotal*tax_rate
#Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
total=subtotal+tax
#Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost)
print (f"Price of item: ${price}")
print (f"Quantity: {quantity} unites")
print (f"Tax rate: {tax_rate*100}%")
print (f"Subtotal : ${round(subtotal,2)}")
print (f"tax: ${round(tax,2)}")
print ("The total: ${}".format(round(total,2)))

'''
############## Bonus###################
'''
print("\n ############## Bonus Round ###################\n")


#Define a string variable containing a sentence with at least 10 words.
intro= "My Name is Mohammed Albushaier. I have graduated from Kwantlen polytechnic university with a bachelor degree in Information technology"

#Define a string variable containing a word that appears in the sentence.
strVar= "Kwantlen"

#Print the length of the sentence.
print (len(intro))

#Print the index of the first occurrence of the word in the sentence.
print (intro.find(strVar))

#Print the number of times the word appears in the sentence.
print (intro.count(strVar))

#Print the sentence in all uppercase letters.
print (intro.upper())

#Print the sentence in all lowercase letters.
print (intro.lower())

#Replace the word in the sentence with a new word of your choice.
print(intro.replace(strVar, "Canadian"))

#Print the last character of the sentence.
print(intro[-1])


'''
this is the Second Python lab in the Course
Feb4, 2025
By Mohammed Albushaier
'''
