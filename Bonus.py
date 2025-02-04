sentence = "The High-Level programming Language Python has two libraries Django and Flask and is also used in artificial intelligence"
word = "High-Level"

print("length of the sentence: ", len(sentence))
print("Index of the first" , sentence.lower().find(word.lower()))
print("Number of times the word appears : ", sentence.lower().count(word.lower()))
print(sentence.upper())
print(sentence.lower())
new_sentence = sentence.replace(word, "a")
print("Modified sentence:", new_sentence)


print("Last character of the sentence:" , sentence[-1])