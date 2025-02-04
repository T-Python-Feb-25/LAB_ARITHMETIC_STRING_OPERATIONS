
sentence ="The vibrant flowers bloom beautifully, spreading joy and fragrance in the garden"
title ="flowers"
print(sentence)
print("\nthe length of the sentence: ",len(sentence))
print(f"the word {title} exist at index: ",sentence.find(title))
print(f"The word {title} appears", sentence.count(title), "time.\n")
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(title,"blossoms"))
print("the last character is: ",sentence[-1])