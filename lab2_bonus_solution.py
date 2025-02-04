"""

## Bonus, create a new python file and do the following:

- Define a string variable containing a sentence with at least 10 words.
- Define a string variable containing a word that appears in the sentence.
- Print the length of the sentence.
- Print the index of the first occurrence of the word in the sentence.
- Print the number of times the word appears in the sentence.
- Print the sentence in all uppercase letters.
- Print the sentence in all lowercase letters.
- Replace the word in the sentence with a new word of your choice.
- Print the last character of the sentence.
"""
sentence="My name is Sabreen , i have a bachler degree in software engineering from university of jeddah"

word= "software"

print(f"-The sentence length is : {sentence.__len__()}")
print(f"-The index of the first occurrence of the word software is : {sentence.index(word)}")
print("-The number of times the word software appears in the sentence is".format(sentence.count(word)))
print("-The sentence in all uppercase letters:\n"+sentence.upper())
print("-The sentence in all lowercase letters:\n"+sentence.lower())
sentence=sentence.replace(word,"Computer")
print("-After replacing the word software to computer the updated sentence is :\n"+sentence)
print("=The last character of the sentence is :"+sentence[-1])
