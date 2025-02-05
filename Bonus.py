# Bonus
AI = "Artificial intelligence is a set of technologies that enable computers to perform a set of advanced functions"
Word = "set"

# length of the sentence
print(f"Length of the sentence: {len(AI)}")

# Index of first occurrence
print(f"Index of first occurrence of '{Word}': {AI.lower().find(Word)}")
# print(AI[29:32])

# number of times the word appears in the sentence
print(f"Number of appearances: {AI.count(Word)}")

# sentence in all uppercase letters
print("Sentence in uppercase: "+ AI.upper())

# sentence in all lowercase letters
print("Sentence in lowercase: ", AI.lower())

# Replace the word with new word
updat_AI = AI.replace(Word, "group")
print(f"Replace the word in the sentence: {updat_AI}")
# print(Word.replace(Word, "group"))

# last character of the sentence
print(f"Last character of the sentence: {AI[-1]}")

