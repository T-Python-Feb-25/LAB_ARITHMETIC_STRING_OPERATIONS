# Define a string variable containing a sentence with at least 10 words
sentence = "The quick brown fox jumps over the lazy dog multiple times."

# Define a string variable containing a word that appears in the sentence
word = "the"

# Print the length of the sentence
print("Length of the sentence:", len(sentence))

# Print the index of the first occurrence of the word in the sentence
print("First occurrence of the word:", sentence.lower().find(word))

# Print the number of times the word appears in the sentence
print("Number of occurrences of the word:", sentence.lower().count(word))

# Print the sentence in all uppercase letters
print("Uppercase sentence:", sentence.upper())

# Print the sentence in all lowercase letters
print("Lowercase sentence:", sentence.lower())

# Replace the word in the sentence with a new word of your choice
new_sentence = sentence.replace("the", "a")
print("Modified sentence:", new_sentence)

# Print the last character of the sentence
print("Last character of the sentence:", sentence[-1])