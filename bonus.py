# Declare Variables
phrase: str = "My Name Nawaf Mansour Eid Alahmadi and I Am 23 Years Old"
appear: str = "Nawaf"

# Length of String
print(len(phrase))
# Finding The Lowest Index of the Searched Word
print(phrase.find(appear))
# How Many Times the Searched Word Occurs
print(phrase.count(appear))
# Convert All Words to Uppercase
print(phrase.upper())
# Convert All Words to Lowercase
print(phrase.lower())
# Replace the Word with Another Word
print(phrase.replace(appear, "Naif"))
# Get the Last Character of the String
print(phrase[-1])