# Define a sentence with at least 10 words
weather = "today's weather is colder than usual, earlier in the morning it was 7 celsius which i believe is not very common in riyadh"

# Define a word that appears in the sentence
degree = "7 celsius"

# Print the length of the sentence
print(f"Length of sentence: {len(weather)} characters.")

# Print the index of the first occurrence of the word in the sentence
# We'll find the first occurrence of 'degree' in the sentence
print(f"Index of the first occurrence of '{degree}': {weather.index(degree)}")

# Print the number of times the word appears in the sentence
print(f"The word '{degree}' appears {weather.count(degree)} times.")

# Print the sentence in all uppercase letters
print("Uppercase sentence:", weather.upper())

# Print the sentence in all lowercase letters
print("Lowercase sentence:", weather.lower())

# Replace the word in the sentence with a new word
new_sentence = weather.replace("today's", "yesterday's")
print("Sentence after replacement:", new_sentence)

# Print the last character of the sentence
print(f"The last character of the sentence is: {weather[-1]}")